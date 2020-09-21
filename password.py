from string import ascii_letters, digits, punctuation
from random import choice
all_characters = ascii_letters + digits + punctuation


# Generates a new password consisting of letters, digits, and punctuations
def generate_password(length) -> str:
    password = ""
    for i in range(int(length)):
        password += choice(all_characters)
    return password


# Generates password and then rewrites all current lines into the file along with the new password
def add_password(lines: list, website_name: str, fo) -> str:
    password_length = input("How long would you like the password to be?\n")
    new_password = generate_password(password_length)
    # for i in lines:
    #     fo.write(i)
    fo.write(website_name + " " + new_password + "\n")
    return "Your new password for " + website_name + " is: " + new_password


# Finds a password already stored in the file
def find_password(lines: list, website_name: str) -> str:
    for i in lines:
        if website_name in i:
            return "Your current password for " + i.split()[0] + " is: " + i.split()[1]


# Changes a currently existing password and adds it to the end of the file
def change_password(lines: list, website_name: str, fo) -> str:
    password_length = input("How long would you like the password to be?\n")
    new_password = generate_password(password_length)
    for i in lines:
        if website_name not in i:
            fo.write(i)
    fo.write(website_name + " " + new_password + "\n")
    fo.truncate()

    return "Your new password for " + website_name + " is: " + new_password
