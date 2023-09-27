import random
import string

def generate_password(length):
    # Define the character pool for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the defined character pool
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("PASSWORD GENERATOR")
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Password length should be a positive integer.")
        else:
            password = generate_password(length)
            print("Generated Password: ", password)
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for password length.")

if __name__ == "__main__":
    main()
