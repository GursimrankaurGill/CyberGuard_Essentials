# modules/privacy_check.py
# this module scans text to find if any personal or sensitive
# information is accidentally exposed in it
# i used regular expressions (re module) to find patterns

import re


def scan_text(text):

    found_items = []

    # check for email addresses
    # pattern means : some characters @ some characters . 2 or more letters
    emails = re.findall(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", text)
    if len(emails) > 0:
        found_items.append(
            f"Email address found : {', '.join(emails)}\n"
            f"      Risk : Others can use your email for spam or phishing."
        )

    # check for Indian mobile numbers
    # Indian numbers start with 6, 7, 8 or 9 and are 10 digits long
    phones = re.findall(r"\b[6-9][0-9]{9}\b", text)
    if len(phones) > 0:
        found_items.append(
            f"Phone number found : {', '.join(phones)}\n"
            f"      Risk : Can be used for SIM swap fraud."
        )

    # check for credit or debit card numbers
    # 16 digits, sometimes written in groups of 4
    cards = re.findall(r"\b[0-9]{4}[\s\-]?[0-9]{4}[\s\-]?[0-9]{4}[\s\-]?[0-9]{4}\b", text)
    if len(cards) > 0:
        found_items.append(
            "Card number found!\n"
            "      Risk : NEVER share card numbers. This is very dangerous."
        )

    # check for Aadhaar number (12 digits, sometimes in groups of 4)
    aadhaar = re.findall(r"\b[0-9]{4}\s?[0-9]{4}\s?[0-9]{4}\b", text)
    if len(aadhaar) > 0:
        found_items.append(
            "Possible Aadhaar number found.\n"
            "      Risk : Share Aadhaar only with trusted government services."
        )

    # check for PAN card number
    # format is 5 letters, 4 numbers, 1 letter like ABCDE1234F
    pan = re.findall(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b", text)
    if len(pan) > 0:
        found_items.append(
            f"PAN card number found : {', '.join(pan)}\n"
            f"      Risk : PAN numbers can be misused for financial fraud."
        )

    # check if someone wrote their password in plain text
    if re.search(r"\b(password|passwd|pwd)\s*[=:]\s*\S+", text, re.IGNORECASE):
        found_items.append(
            "Plain text password detected!\n"
            "      Risk : Never write passwords in plain text anywhere."
        )

    return found_items


def show_privacy_result():

    print("\n  ╔════════════════════════════════════╗")
    print("  ║    PRIVACY EXPOSURE CHECKER        ║")
    print("  ╚════════════════════════════════════╝")
    print("  Paste your text below.")
    print("  Press Enter on an empty line when done.\n")

    lines = []
    while True:
        line = input("  > ")
        if line == "":
            break
        lines.append(line)

    text = " ".join(lines)

    if text.strip() == "":
        print("  No text entered.")
        return []

    results = scan_text(text)

    print(f"\n  Scan complete. {len(results)} issue(s) found.")
    print("  " + "-" * 40)

    if len(results) > 0:
        for i in range(len(results)):
            print(f"\n  ⚠  Problem {i+1} : {results[i]}")
    else:
        print("\n  ✔  No sensitive data found in your text.")

    print("\n  " + "-" * 40)
    return results