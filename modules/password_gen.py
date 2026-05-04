# modules/password_gen.py
# this module creates a strong random password for the user
# i used the random and string modules for this

import random
import string

def make_password(length):

    # minimum length should be 8
    if length < 8:
        length = 8

    # i am keeping one character from each type
    # so the password always has all types
    one_upper   = random.choice(string.ascii_uppercase)
    one_lower   = random.choice(string.ascii_lowercase)
    one_digit   = random.choice(string.digits)
    one_special = random.choice("!@#$%^&*()_+")

    # all characters combined in one string
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+"

    # fill the rest of the password randomly
    rest = []
    for i in range(length - 4):
        rest.append(random.choice(all_chars))

    # combine everything into one list
    final_list = [one_upper, one_lower, one_digit, one_special] + rest

    # shuffle so the forced characters are not always at start
    random.shuffle(final_list)

    # join the list into a string
    password = ""
    for char in final_list:
        password = password + char

    return password


def show_generator_result():

    print("\n  ╔════════════════════════════════════╗")
    print("  ║    STRONG PASSWORD GENERATOR       ║")
    print("  ╚════════════════════════════════════╝")

    try:
        length = int(input("\n  How many characters long? (minimum 8) : "))
    except ValueError:
        print("  That was not a number. Using length 12.")
        length = 12

    password = make_password(length)

    print(f"\n  Your new password : {password}")
    print(f"  Length            : {len(password)} characters")
    print("\n  ⚠  Save this in a safe place. Do not share it with anyone.")
    print("  " + "-" * 40)