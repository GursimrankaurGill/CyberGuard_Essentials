import re

def check_password(password):
    score = 0
    problems = []
    if len(password) >= 8:
        score = score + 1
    else:
        problems.append("Password is too short. Use at least 8 characters.")
    if re.search(r"[A-Z]", password):
        score = score + 1
    else:
        problems.append("Add at least one capital letter (A to Z).")
    if re.search(r"[a-z]", password):
        score = score + 1
    else:
        problems.append("Add at least one small letter (a to z).")
    if re.search(r"[0-9]", password):
        score = score + 1
    else:
        problems.append("Add at least one number (0 to 9).")
    if re.search(r"[!@#$%^&*()_+\-=\[\]{}]", password):
        score = score + 1
    else:
        problems.append("Add a special character like ! @ # $ % etc.")
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MODERATE"
    else:
        strength = "STRONG"
    return score, strength, problems

def show_password_result():
    print("\n  ╔════════════════════════════════════╗")
    print("  ║    PASSWORD STRENGTH CHECKER       ║")
    print("  ╚════════════════════════════════════╝")
    password = input("\n  Enter your password : ")
    if password == "":
        print("  You did not enter anything.")
        return 0, "WEAK"
    score, strength, problems = check_password(password)
    bar = ""
    for i in range(score):
        bar = bar + "█"
    for i in range(5 - score):
        bar = bar + "░"
    print(f"\n  Score    : {bar}  ({score} out of 5)")
    print(f"  Strength : {strength}")
    if len(problems) > 0:
        print("\n  Issues found :")
        for p in problems:
            print(f"    ✘  {p}")
    else:
        print("\n  ✔  Your password is very strong!")
    print("  " + "-" * 40)
    return score, strength