import string
import random

def generate():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passwordLength = int(input("Enter the password length\n"))

    suggestedPassword = []
    suggestedPassword.extend(list(s1))
    suggestedPassword.extend(list(s2))
    suggestedPassword.extend(list(s3))
    suggestedPassword.extend(list(s4))

    random.shuffle(suggestedPassword)
    password = ("".join(suggestedPassword[0:passwordLength]))
    print(password)

generate()