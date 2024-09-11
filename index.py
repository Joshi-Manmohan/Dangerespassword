import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    
    
    s = list(s1 + s2 + s3 + s4)
    
    
    random.shuffle(s)
    
    
    plen = int(input("Enter password length:\n"))
    
    
    password = "".join(s[:plen])
    
    # Print the generated password
    print("Your Password is:\n")
    print(password)
