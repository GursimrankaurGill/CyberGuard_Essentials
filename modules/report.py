# modules/report.py
# this module calculates the final security score
# and saves a report to a text file
# i give different weightage to each module result

from datetime import datetime


def calculate_score(pwd_score, url_risk, file_risk, privacy_issues):

    total = 0

    # password gives up to 30 points
    # pwd_score is 0 to 5, so i multiply by 6 to get max 30
    total = total + (pwd_score * 6)

    # URL gives up to 25 points
    if url_risk == "SAFE":
        total = total + 25
    elif url_risk == "MEDIUM RISK":
        total = total + 12
    else:
        total = total + 0

    # file gives up to 25 points
    if file_risk == "SAFE":
        total = total + 25
    elif file_risk == "CAUTION" or file_risk == "UNKNOWN":
        total = total + 10
    else:
        total = total + 0

    # privacy gives up to 20 points
    # deduct 5 for each problem found, minimum 0
    deduction = len(privacy_issues) * 5
    if deduction > 20:
        deduction = 20
    total = total + (20 - deduction)

    return total


def show_dashboard(pwd_score, url_risk, file_risk, privacy_issues):

    score = calculate_score(pwd_score, url_risk, file_risk, privacy_issues)

    bar = ""
    for i in range(round(score / 5)):
        bar = bar + "#"
    for i in range(20 - round(score / 5)):
        bar = bar + "-"

    if score >= 75:
        status = "LOW RISK - You are well protected!"
    elif score >= 45:
        status = "MEDIUM RISK - Some improvements needed."
    else:
        status = "HIGH RISK - Please take action immediately!"

    print("\n  " + "=" * 48)
    print("         SECURITY SCORE DASHBOARD")
    print("  " + "=" * 48)
    print(f"  Password Strength : {pwd_score} out of 5")
    print(f"  URL Risk Level    : {url_risk}")
    print(f"  File Risk Level   : {file_risk}")
    print(f"  Privacy Issues    : {len(privacy_issues)} problem(s) found")
    print("  " + "-" * 48)
    print(f"  Score  : [{bar}] {score}/100")
    print(f"  Status : {status}")
    print("  " + "=" * 48)

    return score


def give_tips(pwd_score, url_risk, file_risk, privacy_issues, score):

    tips = []

    if pwd_score < 3:
        tips.append("Your password is weak. Change it on all important accounts immediately.")

    if pwd_score < 5:
        tips.append("Make your password stronger : use capitals, numbers and special characters.")

    if url_risk == "HIGH RISK":
        tips.append("The URL you checked is dangerous. Do NOT visit it or enter any details there.")

    if url_risk == "MEDIUM RISK" or url_risk == "HIGH RISK":
        tips.append("Always check URLs carefully before clicking. Look for HTTPS and correct spelling.")

    if file_risk == "HIGH RISK":
        tips.append("The file you scanned is dangerous. Never open .exe or .bat files from strangers.")

    if len(privacy_issues) > 0:
        tips.append("You have sensitive data exposed. Remove it before sharing that text with anyone.")
        tips.append("Never type passwords, card numbers or Aadhaar numbers in messages or documents.")

    if score < 50:
        tips.append("Enable two-factor authentication (2FA) on your email and social media accounts.")
        tips.append("Keep your antivirus software updated and run a scan every week.")

    tips.append("Never use the same password on two different websites.")
    tips.append("Be careful of emails that say your account is suspended or you won a prize.")

    return tips


def show_tips(tips):

    print("\n  ╔══════════════════════════════════════════╗")
    print("  ║       YOUR SECURITY RECOMMENDATIONS      ║")
    print("  ╚══════════════════════════════════════════╝")

    for i in range(len(tips)):
        print(f"\n  {i+1}. {tips[i]}")

    print("\n  " + "=" * 44)
    print("  Remember : Cybersecurity is a daily habit.")
    print("  " + "=" * 44)


def save_report(filename, pwd_score, url_risk, file_risk, privacy_issues, score, tips):

    # get current date and time
    now = datetime.now()
    date_str = now.strftime("%d-%m-%Y")
    time_str = now.strftime("%H:%M:%S")

    # write everything to a text file
    # 'w' means write mode - creates file if it does not exist
    file = open(filename, 'w')

    file.write("=" * 55 + "\n")
    file.write("       CYBERGUARD ESSENTIALS - SECURITY REPORT\n")
    file.write("=" * 55 + "\n")
    file.write(f"  Date    : {date_str}\n")
    file.write(f"  Time    : {time_str}\n")
    file.write("=" * 55 + "\n\n")

    file.write("  RESULTS SUMMARY\n")
    file.write("  " + "-" * 40 + "\n")
    file.write(f"  Password Strength : {pwd_score} / 5\n")
    file.write(f"  URL Risk          : {url_risk}\n")
    file.write(f"  File Risk         : {file_risk}\n")
    file.write(f"  Privacy Issues    : {len(privacy_issues)} found\n")
    file.write(f"  Overall Score     : {score} / 100\n\n")

    file.write("  RECOMMENDATIONS\n")
    file.write("  " + "-" * 40 + "\n")
    for i in range(len(tips)):
        file.write(f"  {i+1}. {tips[i]}\n")

    file.write("\n" + "=" * 55 + "\n")
    file.write("  Generated by CyberGuard Essentials\n")
    file.write("  Developed by Gursimran Kaur\n")
    file.write("=" * 55 + "\n")

    file.close()

    return filename