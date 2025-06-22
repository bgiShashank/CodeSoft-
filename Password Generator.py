import random
import string

print("==========Password Generator==========")
length = int(input("Enter the password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''
for a in range(length):
    password+=random.choice(characters) 

print("Your generated password is:", password)
