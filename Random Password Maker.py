import random

letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = letters.upper()
numbers = "0123456789"
symbols = "!@#$%^&*()?"
all_characters = letters + upper_letters + numbers + symbols

length = int(input("Enter password length: "))

password = ""
for i in range(length):
    password += random.choice(all_characters)

print("Your Password is:", password)
