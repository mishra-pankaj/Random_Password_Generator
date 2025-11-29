import random
import string

def generate_password():
    length = int(input("Enter the length For you password: ").strip())
    include_uppercase = input("Include Upper Letter? (yes/no): ").strip().lower()
    include_special = input("Include special Letter? (yes/no): ").strip().lower()
    include_digit = input("Include digits ? (yes/no): ").strip().lower()

    if length<4:
        print("Password length must be atleast 4 Characters.")
        return

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digit = string.digits if include_special == "yes" else ""

    all_characters = lower + upper + special + digit

    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(upper))

    if include_special == "yes":
        required_characters.append(random.choice(special))

    if include_digit == "yes":
        required_characters.append(random.choice(digit))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)
    str_password = "".join(password)
    return str_password

password = generate_password()
print(password)