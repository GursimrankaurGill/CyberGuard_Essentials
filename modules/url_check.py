# modules/url_check.py
# this module checks if a URL looks suspicious or safe
# i learned that phishing URLs have certain patterns
# so i check for those patterns using the re module

import re

# list of words that are common in fake/phishing websites
suspicious_words = [
    "login", "verify", "update", "secure", "account",
    "confirm", "password", "free", "prize", "urgent",
    "alert", "suspended", "signin", "recover", "banking",
    "wallet", "support", "billing", "invoice"
]


def check_url(url):

    warnings = []
    score = 0
    url_lower = url.lower()

    # check 1 - good websites use https not http
    if not url_lower.startswith("https://"):
        warnings.append("This URL does not use HTTPS. It is not secure.")
        score = score + 2

    # check 2 - some fake sites use IP address instead of a name
    if re.search(r"https?://\d+\.\d+\.\d+\.\d+", url_lower):
        warnings.append("Uses an IP address instead of a website name. Very suspicious.")
        score = score + 3

    # check 3 - check for suspicious words in the URL
    for word in suspicious_words:
        if word in url_lower:
            warnings.append(f"Suspicious word found in URL : '{word}'")
            score = score + 1

    # check 4 - very long URLs are sometimes used to hide the real address
    if len(url) > 75:
        warnings.append(f"URL is very long ({len(url)} characters). This can be suspicious.")
        score = score + 1

    # check 5 - @ symbol in URL is a trick to mislead users
    if "@" in url:
        warnings.append("URL contains @ symbol. This is a common trick used in phishing.")
        score = score + 3

    # check 6 - fake sites copy brand names with a hyphen like paypal-secure.com
    if re.search(r"(paypal|google|amazon|microsoft|apple|sbi|hdfc|icici)\-", url_lower):
        warnings.append("URL looks like it is copying a brand name. Possible fake site.")
        score = score + 2

    # decide risk level
    if score == 0:
        risk = "SAFE"
    elif score <= 3:
        risk = "MEDIUM RISK"
    else:
        risk = "HIGH RISK"

    return score, risk, warnings


def show_url_result():

    print("\n  ╔════════════════════════════════════╗")
    print("  ║    URL / PHISHING CHECKER          ║")
    print("  ╚════════════════════════════════════╝")

    url = input("\n  Paste the URL to check : ").strip()

    if url == "":
        print("  You did not enter a URL.")
        return 0, "UNKNOWN"

    score, risk, warnings = check_url(url)

    print(f"\n  URL       : {url}")
    print(f"  Risk      : {risk}  (score : {score})")

    if len(warnings) > 0:
        print(f"\n  ⚠  {len(warnings)} warning(s) found :")
        for w in warnings:
            print(f"    →  {w}")
    else:
        print("\n  ✔  No suspicious patterns found in this URL.")

    print("  " + "-" * 40)
    return score, risk