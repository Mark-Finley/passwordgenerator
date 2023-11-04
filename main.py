import string
import random

def generate():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    password_length = int(input("Enter the password length\n"))

    suggested_password = []
    suggested_password.extend(list(s1))
    suggested_password.extend(list(s2))
    suggested_password.extend(list(s3))
    suggested_password.extend(list(s4))

    random.shuffle(suggested_password)
    password = ("".join(suggested_password[0:password_length]))
    print(password)

generate()