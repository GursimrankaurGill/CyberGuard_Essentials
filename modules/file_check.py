# modules/file_check.py
# this module checks if a file extension is dangerous
# i made a dictionary of dangerous file types with reasons
# os.path.splitext helps me get the extension from filename

import os

# dictionary of file types that can be dangerous
# key = extension, value = reason it is dangerous
dangerous_files = {
    ".exe" : "This is a Windows program file. Can install malware.",
    ".bat" : "Batch script. Runs commands on your computer automatically.",
    ".vbs" : "Visual Basic Script. Often used in email viruses.",
    ".ps1" : "PowerShell script. Very powerful, dangerous from unknown source.",
    ".cmd" : "Command file. Similar to .bat, runs system commands.",
    ".sh"  : "Shell script. Runs commands on Linux or Mac systems.",
    ".js"  : "JavaScript file. Can run code on your system.",
    ".jar" : "Java program. Can execute code when opened.",
    ".dll" : "System file. Can be injected into other programs.",
    ".scr" : "Screen saver file. Often used to hide malware.",
    ".reg" : "Registry file. Can change important Windows settings.",
    ".msi" : "Windows installer. Installs software, sometimes silently.",
    ".hta" : "HTML application. Runs with full computer access.",
    ".lnk" : "Shortcut file. Can point to harmful programs.",
}

# file types that are generally safe
safe_files = [
    ".txt", ".pdf", ".docx", ".xlsx", ".pptx",
    ".jpg", ".jpeg", ".png", ".gif", ".mp3",
    ".mp4", ".doc", ".xls", ".ppt", ".wav"
]


def check_file(filename):

    # os.path.splitext splits filename into name and extension
    # example : "report.exe" -> ("report", ".exe")
    name, extension = os.path.splitext(filename)
    extension = extension.lower()

    if extension == "":
        return "UNKNOWN", "No file extension found. Cannot check this file."

    if extension in dangerous_files:
        return "HIGH RISK", dangerous_files[extension]

    if extension in [".zip", ".rar", ".7z"]:
        return "CAUTION", "Archive file. Contents could be dangerous. Scan before opening."

    if extension in safe_files:
        return "SAFE", "This file type is generally safe to open."

    return "UNKNOWN", f"Extension '{extension}' is not in my list. Be careful."


def show_file_result():

    print("\n  ╔════════════════════════════════════╗")
    print("  ║    FILE RISK SCANNER               ║")
    print("  ╚════════════════════════════════════╝")
    print("  Examples you can try : setup.exe  report.pdf  script.bat")

    filename = input("\n  Enter the file name : ").strip()

    if filename == "":
        print("  You did not enter a file name.")
        return "UNKNOWN"

    risk, reason = check_file(filename)

    print(f"\n  File      : {filename}")
    print(f"  Risk      : {risk}")
    print(f"  Reason    : {reason}")

    if risk == "HIGH RISK":
        print("\n  ⚠  Do NOT open this file from an unknown or untrusted source!")

    print("  " + "-" * 40)
    return risk