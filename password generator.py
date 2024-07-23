import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Password length must be greater than zero.")
            return
        password = generate_password(length)
        print(f"Generated password: {password}")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
main()
