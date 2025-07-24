import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4.")
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)


    remaining_length = length - 4
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = [random.choice(all_chars) for _ in range(remaining_length)]


    password_list = [lowercase, uppercase, digit, symbol] + remaining_chars
    random.shuffle(password_list)
    return ''.join(password_list)

def main():
    print("=== Pasword Generator ===")
    while True:
        try:
            length = int(input("Enter the desired password length (e.g., 8): "))
            if length < 4:
                print("Password length must be at least 4 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")


    try:
         password = generate_password(length)
         print(f"\nGenerated password: {password}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


    
