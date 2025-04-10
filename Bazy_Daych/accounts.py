class Accounts:
    def __init__(self,name: str,opening_balance: float = 0.0):
        self.name=name
        self.opening_balance=opening_balance
        print(f'Konto zostało utworzone dla {self.name} z balansem {self.opening_balance}')

