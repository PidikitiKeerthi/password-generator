import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

generated_password = generate_password()
username = input("username: ")
print('Hello', username)
print('Here is your password for login:', generated_password)
password = input("Enter the password to login: ")

if password == generated_password:
    print("Login Success")
else:
    print("Wrong Password")
