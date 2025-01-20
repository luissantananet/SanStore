import sqlite3
from PyQt5.QtWidgets import QMessageBox
class Database:
    def __init__(self, name = 'system.db') -> None:        
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)
    
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    
    def create_login_table(self):
        cursor = self.connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS login (user TEXT, password TEXT)')
    
    def login(self, user, password):
        try:
            cursor = self.connect.cursor()
            cursor.execute('SELECT * FROM login WHERE login = ? AND password = ?', (user, password))
            logins = cursor.fetchall()
            return logins
        except:
            return "Erro ao tentar logar"

if __name__ == "__main__":
    db = Database()
    user = db.login("adm", "adm")
    users = "adm", "adm"
    if users == user:
        print('Teste de banco de dados realizado com sucesso')
        print(user)
        print(users)
    else:
        print('Erro logar')
        print(user)
        print(users)
    