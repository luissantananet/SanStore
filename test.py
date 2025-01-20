from database import Database

def test_database():
    # Cria uma instância do banco de dados
    db = Database('test_system.db')
    
    # Conecta ao banco de dados
    db.connect()
    
    
    
    # Insere um usuário para teste
    cursor = db.connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (user TEXT, password TEXT)')
    db.connection.commit()
    cursor.execute('INSERT INTO users (user, password) VALUES (?, ?)', ('test_user', 'test_password'))
    db.connection.commit()
    
    # Tenta fazer login com o usuário inserido
    result = db.login('test_user', 'test_password')
    assert len(result) != 0, "Login falhou, usuário não encontrado."
    
    # Tenta fazer login com um usuário inexistente
    result = db.login('nonexistent_user', 'wrong_password')
    assert len(result) == 0, "Login falhou, usuário inexistente encontrado."
    
    # Fecha a conexão com o banco de dados
    db.close_connection()
    
    print("Todos os testes passaram com sucesso.")

if __name__ == "__main__":
    test_database()