import secrets
import string
import os

def password_gen(length):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    digit = string.digits
    punctuation = string.punctuation
    pwd = alphabet + digit + punctuation
    password = ''.join(secrets.choice(pwd) for i in range(length))
    return password


if __name__ == '__main__':
    os.system('clear') if os.name == 'posix' else os.system('cls')
    length = int(input("Enter the length of the password: "))
    password = password_gen(length)
    print("The random password is: ", password)