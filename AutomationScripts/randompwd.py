#Lets generate a random password

import random
import string

#you can give any length

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


#now lets call the function and print the password

print("Your password: ", generate_password(16)) #you can change the length as needed


Your password:  x:!~Dpp~P2tzgbwi