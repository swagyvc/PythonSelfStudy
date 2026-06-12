

class Account:
    def __init__(self,username, password, email, role):
        self.username = username
        self.password = password
        self.email = email
        self.role = role

class UserAccount(Account):
    pass

class OwnerAccount(Account):
    pass