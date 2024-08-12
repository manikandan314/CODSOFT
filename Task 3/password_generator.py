import random
import string

def main():
    print("Password Generator")
    len = int(input("Enter the length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = random.choices(characters, k = len)
    password = ''.join(password)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
