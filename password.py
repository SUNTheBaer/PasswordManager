from string import ascii_letters, digits, punctuation
from random import choice
all_characters = ascii_letters + digits + punctuation


def generate_password(length) -> str:
    password = ""
    for i in range(int(length)):
        password += choice(all_characters)
    return password
