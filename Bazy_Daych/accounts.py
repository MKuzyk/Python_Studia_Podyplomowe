import datetime

from database_one import connection

class Account:
    def __init__(self,name: str,opening_balance: float = 0.0):
        self.name=name
        self.balance=opening_balance

        connection.execute("INSERT into accounts(name,balance) VALUES(?,?)",
                           (self.name,self.balance))
        cursor = connection.execute("SELECT @@IDENTITY as ID")

        self.id = cursor.fetchval()

        connection.commit()

        print(f'Konto zostało utworzone dla {self.name} z balansem {self.balance}')

    def deposit(self, amount:float,auto_commit:bool=True) -> float:
        if amount > 0:
            self.balance +=amount
            connection.execute("UPDATE accounts SET balance = ? WHERE account_id = ?",(self.balance,self.id))
            connection.execute("INSERT INTO transactions (account_id,transaction_time,amount) VALUES(?,?,?)",
                               (self.id,datetime.datetime.now(),amount))
            if auto_commit:
                connection.commit()

            print(f'Na konto {self.name} zostało dodane {amount} PLN')
        return round(self.balance,2)

    def withdraw(self, amount:float,auto_commit:bool=True) -> float:
        if 0 < amount <= self.balance:
            self.balance -=amount

            connection.execute("UPDATE accounts SET balance = ? WHERE account_id = ?", (self.balance, self.id))
            connection.execute("INSERT INTO transactions (account_id,transaction_time,amount) VALUES(?,?,?)",
                               (self.id, datetime.datetime.now(), -amount))
            if auto_commit:
                connection.commit()

            print(f'Z konta {self.name} zostało wypłacone {amount} PLN')
        else:
            raise ValueError('Nie masz wystarczających środków na koncie')
        return round(self.balance,2)


    def send_funds(self, amount: float, account):
        self.withdraw(amount,auto_commit=False)
        account.deposit(amount,auto_commit=False)
        connection.commit()


    def send_funds(self, amount: float, account):
        try:
            if amount <= 0:
                raise ValueError("Kwota przelewu musi być większa niż 0")

            self.withdraw(amount, auto_commit=False)

            if self.balance < 0:
                raise ValueError(f'Saldo konta {self.name} nie może być ujemne! Cofnięcie transakcji.')

            account.deposit(amount, auto_commit=False)

            connection.commit()
            print(f'Przelano {amount} PLN z konta {self.name} na konto {account.name}')

        except Exception as e:
            connection.rollback()
            print(f'Transakcja nieudana: {e}')

    def transaction_history(self):
        cursor = connection.execute("SELECT transaction_time, amount FROM transactions WHERE account_id = ? ORDER BY transaction_time DESC"
        , (self.id,))

        transactions = cursor.fetchall()

        print(f'\n Historia transakcji konta: {self.name}')
        if not transactions:
            print("Brak transakcji.")
            return

        for row in transactions:
            transaction_time = row.transaction_time
            amount = row.amount

            transaction_type = "Wpłata" if amount > 0 else "Wypłata"

            formatted_time = transaction_time.strftime('%Y-%m-%d %H:%M:%S')

            print(f"[{transaction_type}] {formatted_time} | Kwota: {amount:.2f} PLN")


if __name__ == '__main__':
    account_jan = Account('Jan',10)
    account_michal = Account('Michal', 10)
    account_jan.send_funds(5,account_michal)
    account_michal.transaction_history()




