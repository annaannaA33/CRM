import bcrypt
import csv

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __str__(self) -> str:
        return f'login: {self.username} - role: {self.role}'

    
    @staticmethod
    def hash_password(password):
        # Generate a random salt
        salt = bcrypt.gensalt()
        # Hash the password with the salt
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password.decode()

    
    def login(users):
        print("Welcome to the Online Store CRM System!")
        while True:
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            
            if not username or not password:
                print("Username and password cannot be empty. Try again.")
                continue
            
            for user in users:
                if user.username == username and bcrypt.checkpw(password.encode(), user.password.encode()):
                    return user.role
            
            print("Invalid username or password. Try again or press '0' to quit.")
            if input("Continue? (press '0' to quit): ").strip() == '0':
                print("Exiting the program. Goodbye!")
                return None


    

