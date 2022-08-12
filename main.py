"""
random password generator of a requested length


created by. Matt Toppi
"""

import random
import string


def generate_password(length):
    """
    Generates a random password of length 'length'
    :return:
    password: string
    """
    password = ""
    for i in range(0, length):
        password += random.choice(string.ascii_letters + string.digits)
    return password


def __main__():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print(password)


if __name__ == "__main__":
    __main__()
