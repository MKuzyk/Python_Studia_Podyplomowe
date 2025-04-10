class Account:
    def __init__(self,name: str,opening_balance: float = 0.0):
        self.name=name
        self.balance=opening_balance
        print(f'Konto zostało utworzone dla {self.name} z balansem {self.balance}')

    def deposit(self, amount:float) -> float:
        if amount > 0:
            self.balance +=amount
            print(f'Na konto {self.name} zostało dodane {amount} PLN')
        return round(self.balance,2)

    def withdraw(self, amount:float) -> float:
        if amount < 0:
            self.balance -=amount
            print(f'Z konta {self.name} zostało wypłacone {amount} PLN')
        return round(self.balance,2)

if __name__ == 'main':
    account=Account ('Michal')
    account.deposit(10)
    account.deposit(0.1)
    balance = account.withdraw(5)
    print(balance)


