import string
import random

def generate_password(length):
    # Define character sets
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    # Combine all character sets into one list
    s = list(s1 + s2 + s3 + s4)

    # Shuffle the list to ensure randomness
    random.shuffle(s)

    # Generate the password by joining the required number of characters
    return "".join(s[:length])

def is_valid_password(password):
    # Define character sets
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_punctuation = any(c in string.punctuation for c in password)
    
    # Check if all criteria are met
    return has_lower and has_upper and has_digit and has_punctuation

def main():
    while True:
        try:
            # Get the password length from the user
            plen = int(input("Enter password length:\n"))
            
            # Check for invalid length values
            if plen <= 0:
                print("Password length must be a positive integer.")
            else:
                # Generate and print the password
                generated_password = generate_password(plen)
                print(f"Generated Password: {generated_password}")

                # Validate the generated password
                if is_valid_password(generated_password):
                    print("The generated password is valid.")
                else:
                    print("The generated password is invalid. It must include at least one lowercase letter, one uppercase letter, one digit, and one punctuation symbol.")

                # Ask for a specific string to compare with the generated password
                specific_string = input("Enter the string to compare with the generated password:\n")
                if generated_password == specific_string:
                    print("The generated password matches the specific string.")
                else:
                    print("The generated password does not match the specific string.")
                
                # Ask if the generated password should be searched in a text
                search_in_text = input("Do you want to search for the generated password in a text? (yes/no):\n").strip().lower()
                if search_in_text == 'yes':
                    text = input("Enter the text to search within:\n")
                    if generated_password in text:
                        print("The password was found within the text.")
                    else:
                        print("The password was not found within the text.")
                
                # Exit the loop
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
