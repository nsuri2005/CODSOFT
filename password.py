import random
import string
def generate_password(len):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(len))
    return password
def main():
     len = int(input("Enter the desired password length: "))
     password = generate_password(len)
     print("the password with desired lenth is:",password)
     
if __name__ == "__main__":
    main()
