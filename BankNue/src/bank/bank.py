import secrets

from bank.account import Account
import bcrypt


class Bank:
    def __init__(self, name: str, sort_code: str):
        self._name = name
        self._sort_code = sort_code
        self._accounts: list[Account] = []

    def create_account(self, first_name: str, last_name: str, password: str, ):
        hashed_password = self.__encrypt(password)
        account_number = self.__generate_account_number()
        new_account = Account(first_name, last_name, hashed_password, account_number)
        self._accounts.append(new_account)
        return new_account

    def __encrypt(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def __generate_account_number(self) -> str:
        return ''.join(str(secrets.randbelow(10)) for _ in range(10))

    def find_account_by(self, account_number):
        found_account: Account = next(filter(lambda account: account.account_number == account_number, self._accounts))
        if found_account:
            return found_account
        raise ValueError(f'Account number {account_number} not found')

    def deposit(self, account: Account, amount: [int, float]):
        account.credit(amount)

    def withdraw(self, account: Account, password: str, amount: [int, float]):
        if self.__is_authenticated(account, password):
            account.debit(amount)
        else:
            raise ValueError("incorrect password")

    def __is_authenticated(self, account: Account, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), account.password)

    def transfer(self, from_account: Account, password: str, to_account: Account, amount: [int, float]):
        if from_account == to_account: raise ValueError("Cannot transfer to same account")
        if self.__is_authenticated(from_account, password):
            from_account.debit(amount)
            to_account.credit(amount)
            return None
        raise ValueError("incorrect password")
