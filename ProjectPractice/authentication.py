class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  

    def check_password(self, input_password):
        """Encapsulation: Keeps the password hidden, but allows validation."""
        return self.__password == input_password


class AuthSystem:
    def __init__(self):
        # Using a dictionary for O(1) constant-time user lookups
        self.users = {}  

    def register(self, username, password):
        if username in self.users:
            print("Error: Username already exists.")
            return False
        
        # Instantiate a new User object and store it in our dictionary
        new_user = User(username, password)
        self.users[username] = new_user
        print(self.users)
        print(f"Success: Account created for '{username}'.")
        return True

    def login(self, username, password):
        # Instant lookup using the dictionary key
        user = self.users.get(username)
        
        if user and user.check_password(password):
            print(f"Success: Welcome back, {username}!")
            return True
        
        print("Error: Invalid username or password.")
        return False


# --- Terminal Interface (The Execution Loop) ---
if __name__ == "__main__":
    system = AuthSystem()

    while True:
        print("\n--- Terminal Auth System ---")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            system.register(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            system.login(username, password)

        elif choice == "3":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Try again.")