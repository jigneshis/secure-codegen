import random
import string

def generate_code(length, strength):
    if strength == "easy":
        chars = string.digits
    elif strength == "hard":
        chars = string.ascii_letters + string.digits
    else:
        raise ValueError("Invalid strength selected.")
    
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    try:
        # Ask user for input
        length = int(input("Enter the number of digits/length for each code: "))
        strength = input("Enter the strength (easy/hard): ").strip().lower()
        count = int(input("Enter how many codes you want to generate: "))

        print("\nGenerated Codes:")
        for _ in range(count):
            print(generate_code(length, strength))

    except ValueError:
        print("Please enter valid input (numbers for digit/count, 'easy' or 'hard' for strength).")

if __name__ == "__main__":
    main()
