class Account:
    def __init__(self,username, password, email, role):
        ## private attributes
        self.__username = username
        self.__password = password
        self.__email = email
        self.__role = role


class UserAccount(Account):
    pass

class OwnerAccount(Account):
    pass