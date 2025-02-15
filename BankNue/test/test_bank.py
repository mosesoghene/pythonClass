import unittest

from bank.account import Account
from bank.bank import Bank


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("BankNue", "1234")

    def tearDown(self):
        self.bank = None

    def test_accounts_length_zero_by_default(self):
        expected = 0
        actual = len(self.bank._accounts)
        self.assertEqual(expected, actual)

    def test_add_account_and_accounts_len_increases_by_one(self):
        self.bank.create_account("Moses", "Oghene", "1234")
        expected = 1
        actual = len(self.bank._accounts)
        self.assertEqual(expected, actual)

    def test_add_account_xy_find_account_x_by_first_name(self):
        x_account_num = self.bank.create_account("Moses", "Oghene", "1234").account_number
        y_account_num = self.bank.create_account("Esther", "Emmanuel", "4321").account_number
        actual = self.bank.find_account_by(x_account_num).first_name
        expected = "Moses"
        self.assertEqual(expected, actual)
        actual = self.bank.find_account_by(y_account_num).first_name
        expected = "Esther"
        self.assertEqual(expected, actual)

    def test_account_balance_is_zero_by_default(self):
        x_account_num = self.bank.create_account("Moses", "Oghene", "1234").account_number
        account: Account = self.bank.find_account_by(x_account_num)
        actual = account.balance
        expected = 0
        self.assertEqual(expected, actual)

    def test_deposit_increase_account_balance(self):
        x_account_num = self.bank.create_account("Moses", "Oghene", "1234").account_number
        account: Account = self.bank.find_account_by(x_account_num)
        actual = account.balance
        expected = 0
        self.assertEqual(expected, actual)

        self.bank.deposit(account, 2000)
        actual = account.balance
        expected = 2000
        self.assertEqual(expected, actual)

    def test_deposit_raises_error_for_negative_amount(self):
        x_account_num = self.bank.create_account("Moses", "Oghene", "1234").account_number
        account: Account = self.bank.find_account_by(x_account_num)
        actual = account.balance
        expected = 0
        self.assertEqual(expected, actual)

        self.assertRaises(ValueError, self.bank.deposit, account, -2000)

    def test_deposit_raises_error_for_zero_amount(self):
        x_account_num = self.bank.create_account("Moses", "Oghene", "1234").account_number
        account: Account = self.bank.find_account_by(x_account_num)
        actual = account.balance
        expected = 0
        self.assertEqual(expected, actual)

        self.assertRaises(ValueError, self.bank.deposit, account, 0)

    def test_withdrawal_raises_error_for_incorrect_password(self):
        x_account_num = self.bank.create_account("Moses", "Oghene", "1234").account_number
        account: Account = self.bank.find_account_by(x_account_num)
        actual = account.balance
        expected = 0
        self.assertEqual(expected, actual)

        self.bank.deposit(account, 2000)
        actual = account.balance
        expected = 2000
        self.assertEqual(expected, actual)

        self.assertRaises(ValueError, self.bank.withdraw, account, '1243', 2000)



    def test_withdrawal_raises_error_amount_greater_than_balance(self):
        x_account_num = self.bank.create_account("Moses", "Oghene", "1234").account_number
        account: Account = self.bank.find_account_by(x_account_num)
        actual = account.balance
        expected = 0
        self.assertEqual(expected, actual)

        self.assertRaises(ValueError, self.bank.withdraw, account, "1234", 2000)

        actual = account.balance
        expected = 0
        self.assertEqual(expected, actual)

    def test_withdrawal_decrease_account_balance(self):
        x_account_num = self.bank.create_account("Moses", "Oghene", "1234").account_number
        account: Account = self.bank.find_account_by(x_account_num)
        actual = account.balance
        expected = 0
        self.assertEqual(expected, actual)

        self.bank.deposit(account, 2000)
        actual = account.balance
        expected = 2000
        self.assertEqual(expected, actual)

        self.bank.withdraw(account, "1234", 999)
        actual = account.balance
        expected = 1001
        self.assertEqual(expected, actual)

    def test_withdrawal_raises_error_for_negative_amount(self):
        x_account_num = self.bank.create_account("Moses", "Oghene", "1234").account_number
        account: Account = self.bank.find_account_by(x_account_num)
        actual = account.balance
        expected = 0
        self.assertEqual(expected, actual)

        self.bank.deposit(account, 2000)
        actual = account.balance
        expected = 2000
        self.assertEqual(expected, actual)

        self.assertRaises(ValueError, self.bank.withdraw, account, "1234", -1000)

    def test_withdrawal_raises_error_for_zero_amount(self):
        x_account_num = self.bank.create_account("Moses", "Oghene", "1234").account_number
        account: Account = self.bank.find_account_by(x_account_num)
        actual = account.balance
        expected = 0
        self.assertEqual(expected, actual)

        self.bank.deposit(account, 2000)
        actual = account.balance
        expected = 2000
        self.assertEqual(expected, actual)

        self.assertRaises(ValueError, self.bank.withdraw, account, "1234", 0)

    def test_transfer_raises_error_for_zero_and_negative_amount(self):
        from_account_num = self.bank.create_account("Moses", "Oghene", "1234").account_number
        to_account_num = self.bank.create_account("Esther", "Emmanuel", "4321").account_number

        from_account: Account = self.bank.find_account_by(from_account_num)
        to_account: Account = self.bank.find_account_by(to_account_num)
        actual = from_account.balance
        expected = 0
        self.assertEqual(expected, actual)

        actual = to_account.balance
        expected = 0
        self.assertEqual(expected, actual)

        self.bank.deposit(from_account, 2000)
        actual = from_account.balance
        expected = 2000
        self.assertEqual(expected, actual)

        self.assertRaises(ValueError, self.bank.transfer, from_account, "1234", to_account, 0)

    def test_transfer_raises_error_for_same_account_transfer(self):
        from_account_num = self.bank.create_account("Moses", "Oghene", "1234").account_number
        to_account_num = from_account_num

        from_account: Account = self.bank.find_account_by(from_account_num)
        to_account: Account = self.bank.find_account_by(to_account_num)
        actual = from_account.balance
        expected = 0
        self.assertEqual(expected, actual)

        actual = to_account.balance
        expected = 0
        self.assertEqual(expected, actual)

        self.bank.deposit(from_account, 2000)
        actual = from_account.balance
        expected = 2000
        self.assertEqual(expected, actual)

        self.assertRaises(ValueError, self.bank.transfer, from_account, "1234", to_account, 100)

    def test_transfer_reduce_from_account_increase_to_account(self):
        from_account_num = self.bank.create_account("Moses", "Oghene", "1111").account_number
        to_account_num = self.bank.create_account("Esther", "Emmanuel", "4321").account_number

        from_account: Account = self.bank.find_account_by(from_account_num)
        to_account: Account = self.bank.find_account_by(to_account_num)
        actual = from_account.balance
        expected = 0
        self.assertEqual(expected, actual)

        actual = to_account.balance
        expected = 0
        self.assertEqual(expected, actual)

        self.bank.deposit(from_account, 2000)
        actual = from_account.balance
        expected = 2000
        self.assertEqual(expected, actual)

        self.bank.transfer(from_account, "1111", to_account, 300)

        actual = from_account.balance
        expected = 1700
        self.assertEqual(expected, actual)

        actual = to_account.balance
        expected = 300
        self.assertEqual(expected, actual)

    def test_transfer_raises_error_for_incorrect_from_account_password(self):
        from_account_num = self.bank.create_account("Moses", "Oghene", "1111").account_number
        to_account_num = self.bank.create_account("Esther", "Emmanuel", "4321").account_number

        from_account: Account = self.bank.find_account_by(from_account_num)
        to_account: Account = self.bank.find_account_by(to_account_num)
        actual = from_account.balance
        expected = 0
        self.assertEqual(expected, actual)

        actual = to_account.balance
        expected = 0
        self.assertEqual(expected, actual)

        self.bank.deposit(from_account, 2000)
        actual = from_account.balance
        expected = 2000
        self.assertEqual(expected, actual)

        self.assertRaises(ValueError, self.bank.transfer, from_account, "1279", to_account, 300)