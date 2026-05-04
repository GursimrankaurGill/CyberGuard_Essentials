# main.py
# CyberGuard Essentials - A Python Cybersecurity Toolkit
# This project uses 5 different modules to check security

from modules.password_check import show_password_result
from modules.password_gen   import show_generator_result
from modules.url_check      import show_url_result
from modules.file_check     import show_file_result
from modules.privacy_check  import show_privacy_result
from modules.report         import show_dashboard, give_tips, show_tips, save_report, calculate_score
from datetime import datetime


def main():

    print("\n  ╔══════════════════════════════════════════════╗")
    print("  ║                                              ║")
    print("  ║       CYBERGUARD ESSENTIALS  v1.0            ║")
    print("  ║       Python Cybersecurity Toolkit           ║")
    print("  ║                                              ║")
    print("  ║       Made by : Gursimran Kaur               ║")
    print("  ║       2nd Sem B.Tech CSE                     ║")
    print("  ║                                              ║")
    print("  ╚══════════════════════════════════════════════╝")

    # these variables store results from each tool
    # they are used later in the dashboard and report
    pwd_score      = 0
    url_risk       = "NOT CHECKED"
    file_risk      = "NOT CHECKED"
    privacy_issues = []
    final_score    = 0

    while True:

        print("\n  ┌──────────────────────────────────────────────┐")
        print("  │                MAIN MENU                     │")
        print("  ├──────────────────────────────────────────────┤")
        print("  │   1.  Check Password Strength                │")
        print("  │   2.  Generate Strong Password               │")
        print("  │   3.  Check URL for Phishing                 │")
        print("  │   4.  Scan File for Risk                     │")
        print("  │   5.  Check Text for Private Data            │")
        print("  │   6.  View My Security Score                 │")
        print("  │   7.  Get Security Tips                      │")
        print("  │   8.  Save Report to File                    │")
        print("  │   9.  Exit                                   │")
        print("  └──────────────────────────────────────────────┘")

        choice = input("\n  Enter your choice (1-9) : ").strip()

        if choice == "1":
            pwd_score, strength = show_password_result()

        elif choice == "2":
            show_generator_result()

        elif choice == "3":
            score, url_risk = show_url_result()

        elif choice == "4":
            file_risk = show_file_result()

        elif choice == "5":
            privacy_issues = show_privacy_result()

        elif choice == "6":
            final_score = show_dashboard(pwd_score, url_risk, file_risk, privacy_issues)

        elif choice == "7":
            if final_score == 0:
                final_score = calculate_score(pwd_score, url_risk, file_risk, privacy_issues)
            tips = give_tips(pwd_score, url_risk, file_risk, privacy_issues, final_score)
            show_tips(tips)

        elif choice == "8":
            if final_score == 0:
                final_score = calculate_score(pwd_score, url_risk, file_risk, privacy_issues)
            tips = give_tips(pwd_score, url_risk, file_risk, privacy_issues, final_score)

            # create filename with current date and time
            now = datetime.now()
            filename = "security_report_" + now.strftime("%d%m%Y_%H%M") + ".txt"

            saved = save_report(filename, pwd_score, url_risk, file_risk, privacy_issues, final_score, tips)
            print(f"\n  ✔  Report saved as : {saved}")

        elif choice == "9":
            print("\n  ╔══════════════════════════════════════════════╗")
            print("  ║   Thank you for using CyberGuard Essentials  ║")
            print("  ║   Stay safe online!                          ║")
            print("  ╚══════════════════════════════════════════════╝\n")
            break

        else:
            print("\n  ✘  Invalid choice. Please enter a number from 1 to 9.")


# this line makes sure main() only runs when we
# directly run this file, not when it is imported
if __name__ == "__main__":
    main()