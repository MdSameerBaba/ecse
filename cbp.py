import string
import random

class PasswordGenerator:
    """Generates random passwords based on specified character sets."""
    
    def __init__(self):
        """Initializes the password generator with an empty character set."""
        self.length = 0
        self.character_set = ""
    
    def set_length(self, length):
        """Sets the desired password length."""
        self.length = length
    
    def add_characters(self, choice):
        """Adds characters to the possible character set based on user choice."""
        if choice == 1:
            self.character_set += string.ascii_letters
        elif choice == 2:
            self.character_set += string.digits
        elif choice == 3:
            self.character_set += string.punctuation
    
    def generate_password(self):
        """Generates a random password from the defined character set."""
        if not self.character_set:
            print("Character set is empty. Please add character sets before generating password.")
            return ""
        
        password = [random.choice(self.character_set) for _ in range(self.length)]
        return "".join(password)

def main():
    """Prompts user for password length and character set, then generates a password."""
    pg = PasswordGenerator()

    length = int(input("Enter password length: "))
    pg.set_length(length)

    print('''Choose character set for password:
    1. Letters
    2. Digits
    3. Special characters''')
    
    while not pg.character_set:
        choice = int(input("Pick a number: "))
        if choice in [1, 2, 3]:
            pg.add_characters(choice)
        else:
            print("Please pick a valid option!")

    password = pg.generate_password()
    if password:
        print(f"The random password is: {password}")

if __name__ == "__main__":
    main()
