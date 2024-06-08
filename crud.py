import sqlite3
from pathlib import Path

class Cliente:
    def __init__(self, nome, primeiroNome, cpf, contatos, dataNascimento, versao):
        #self.id = id
        self.nome = nome
        self.primeiroNome = primeiroNome
        self.cpf = cpf
        self.contatos = contatos
        self.dataNascimento = dataNascimento
        self.versao = versao

    def save(self):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO clientes (nome, primeiroNome, cpf, contatos, dataNascimento, versao) VALUES(?, ?, ?, ?, ?, ?)', (self.nome, self.primeiroNome, self.cpf, self.contatos, self.dataNascimento, self.versao))
            self.id = cursor.lastrowid
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
    
    def update(self, id):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        # cursor.execute('UPDATE clientes SET nome = ?, primeiroNome = ?, cpf = ?, contatos = ? dataNascimento = ?, versao = ? WHERE id = ?', (self.nome, self.primeiroNome, self.cpf, self.contatos, self.dataNascimento, self.versao, id))
        # o update não aceitou atualizar o campo dataNascimento, não sei o motivo ainda
        cursor.execute('UPDATE clientes SET nome = ?, primeiroNome = ?, cpf = ?, contatos = ?, versao = ? WHERE id = ?', (self.nome, self.primeiroNome, self.cpf, self.contatos, self.versao, id))
        conn.commit()
        conn.close()

    def delete(self, id):        
        conn = sqlite3.connect("loja.db")
        cursor = conn.cursor()
        conn.execute("DELETE FROM clientes WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect("loja.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        conn.close()
        return [Cliente (nome=row[1], primeiroNome=row[2], cpf=row[3], contatos=row[4], dataNascimento=row[5], versao=row[6]) for row in clientes]
    
    @staticmethod
    def get_by_id(id):
        conn = sqlite3.connect("loja.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close
        if row:
            return Cliente (nome=row[1], primeiroNome=row[2], cpf=row[3], contatos=row[4], dataNascimento=row[5], versao=row[6])
        return None
    
def criar_tabelas():
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL,
        primeiroNome TEXT NOT NULL, 
        cpf TEXT NOT NULL, 
        contatos TEXT NOT NULL, 
        dataNascimento DATETIME, 
        versao INTEGER)           
    ''')
    conn.commit()
    conn.close()

#criar_tabelas()

cliente1 = Cliente ( nome = 'Pedro Augusto', primeiroNome = 'Pedro', cpf = '01234566789', contatos = 'Mãe', dataNascimento = "2010-10-12", versao = 5)
cliente1.save()
cliente2 = Cliente( "Maria Silva", "Maria", "0123456202316", "Marisa", "1990-11-05", 1)
cliente2.save()

cliente1.update(19)
cliente1.delete(3)

# Listar todos os clientes
print('Clientes:')
clientes = Cliente.get_all()
#for cliente in clientes: - funciona assim também
for cliente in Cliente.get_all():
    print(f'Nome: {cliente.nome}, Data Nascimento: {cliente.dataNascimento}')

cliente = Cliente.get_by_id(19)
print (f'\nNome: {cliente.nome}, Data de Nascimento:{cliente.dataNascimento}')