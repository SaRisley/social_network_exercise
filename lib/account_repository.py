from lib.account import Account

class AccountRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM accounts')
        accounts = []
        for row in rows:
            item = Account(row["id"], row["email"], row["username"])
            accounts.append(item)
        return accounts
    
    def find(self, username):
        rows = self._connection.execute('SELECT * FROM accounts WHERE username = %s', [username])
        row = rows[0]
        return Account(row["id"], row["email"], row["username"])

    def create(self, account):
        self._connection.execute('INSERT INTO accounts (email, username) VALUES (%s, %s)', [account.email, account.username])
    
    def delete(self, username):
        self._connection.execute('DELETE FROM accounts WHERE username = %s', [username])