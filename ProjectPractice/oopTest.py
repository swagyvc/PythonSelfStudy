class Wallet:
    def __init__(self) -> None:
        self.__balance: float = 0.0

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.__balance:
            raise ValueError("Insufficient funds.")

        self.__balance -= amount

