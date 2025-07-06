import secrets
import string


def generate_password(pwd_length):
    if pwd_length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password includes at least one character from each set
    password_chars = [
        secrets.choice(letters),
        secrets.choice(digits),
        secrets.choice(symbols),
        secrets.choice(letters.upper())
    ]

    # Fill the rest with random characters
    total_pool = letters + digits + symbols
    password_chars += [secrets.choice(total_pool) for _ in range(pwd_length - 4)]

    # Shuffle and join
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)


if __name__ == "__main__":
    try:
        user_input = input("Enter desired password length (minimum 4): ")
        user_length = int(user_input)
        final_password = generate_password(user_length)
        print("Generated Password:", final_password)
    except ValueError as e:
        print("Error:", e)
