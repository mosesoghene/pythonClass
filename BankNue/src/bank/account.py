class Account:
    def __init__(self, first_name: str, last_name: str, password: bytes, account_number: str) -> None:
        self._balance: float = 0.0
        self._first_name = first_name.title()
        self._last_name = last_name.title()
        self._password = password
        self._account_number: str = account_number

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    def __repr__(self) -> str:
        return f"{self._first_name} {self._last_name}: {self._account_number}"

    @property
    def balance(self):
        return self._balance

    def credit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    def debit(self, amount):
        if amount > self.balance:
            raise ValueError(f"Balance too low for amount: ${amount}")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance -= amount

    @property
    def password(self):
        return self._password


