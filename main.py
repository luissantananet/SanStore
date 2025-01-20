from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
#import mysql.connector
#import mysql.connector.errors
import sqlite3
from database import Database

def funcao_login():
    nome_user =frm_login.lineuser.text()
    key = frm_login.linekey.text()
    db = Database()
    
    senha_db = db.login(nome_user, key)
    #print(nome, senha_db)
    if key == senha_db[0][1] : 
        frm_login.close()
        frm_main.show()
    else:
        #frm_login.close()
        QMessageBox.about(frm_login, "Erro", "Usuário ou senha invalido!") 
    # chamando as telas

def funcao_cancela():
    frm_login.close()

if __name__ == "__main__":
    # chamando as telas
    app = QtWidgets.QApplication([])
    frm_login = uic.loadUi(r'.\frms\frm_login.ui')
    frm_main = uic.loadUi(r'.\frms\frm_principal.ui')

    # botões da tela login
    frm_login.linekey.setEchoMode(QtWidgets.QLineEdit.Password)
    frm_login.btnlogin.clicked.connect(funcao_login)
    frm_login.btnexit.clicked.connect(funcao_cancela)

    frm_login.show()
    app.exec()