# TODO("Delete this 'TODO' and create your class here")
class Account:
    def __init__(self,balance:float):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self,money:float):
        self._balance += money

    def withdrawal(self,money_withdraw:float):
        if money_withdraw <=  self._balance:
            self._balance -= money_withdraw

    def fee(self):
        self._balance = 0.95* self._balance


if __name__ == '__main__':
    account = Account(10)
    account.deposit(100)
    account.withdrawal(40)
    account.fee()
    print(account.balance)