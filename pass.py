import random
import string


def generate_password(length=6, use_uppercase=True, use_digits=True, use_special=True):

    characters = string.ascii_lowercase


    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation


    if not characters:
        characters = string.ascii_lowercase


    password = ''.join(random.choice(characters) for _ in range(length))

    return password



if __name__ == "__main__":
    while True:
        try:
            length = int(input("Please enter the lenght : "))
            if length <= 0:
                print("Length should be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    use_uppercase = input("Include uppercase letters ? (yes/no): ").strip() == 'y'
    use_digits = input("Include digits ? (yes/no): ").strip() == 'y'
    use_special = input("Include special characters ? (yes/no): ").strip() == 'y'


    print("Generated Password:", generate_password(length, use_uppercase, use_digits, use_special))
