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
        #if self.id is None:
        try:
            cursor.execute('INSERT INTO clientes (nome, primeiroNome, cpf, contatos, dataNascimento, versao) VALUES(?, ?, ?, ?, ?, ?)', (self.nome, self.primeiroNome, self.cpf, self.contatos, self.dataNascimento, self.versao))
            print(self.nome)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
        #self.id = cursor.lastrowid
        # else:
        #     cursor.execute('UPDATE clientes SET nome = ?, primeiroNome = ?, cpf = ?, contatos = ? dataNascimento = ?, versao = ? WHERE id = ?', (self.nome, self.primeiroNome, self.cpf, self.contatos, self.dataNascimento, self.versao, self.id))
        

    def delete(self):        
        if self.id is not None:
            conn = sqlite3.connect("loja.db")
            cursor = sqlite3.Cursor()
            conn.execute("DELETE FROM clientes WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()
            self.id = None

    @staticmethod
    def get_all(self):
        conn = sqlite3.connect("loja.db")
        cursor = sqlite3.Cursor()
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        conn.close()
        return [Cliente (id=row[0],nome=row[1], primeiroNome=row[2], cpf=row[3], contatos=row[4], dataNascimento=row[5], versao=row[6]) for row in clientes]
    
    @staticmethod
    def get_by_id(id):
        conn = sqlite3.connect("loja.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close
        if row:
            return Cliente (id=row[0],nome=row[1], primeiroNome=row[2], cpf=row[3], contatos=row[4], dataNascimento=row[5], versao=row[6])
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

criar_tabelas()

cliente1 = Cliente ( nome = 'Andrea Silvestre', primeiroNome = 'Andrea', cpf = '01234566789', contatos = 'Marisa', dataNascimento = '1980-10-12', versao = 5)
cliente1.save()
cliente2 = Cliente( "Tiago Silva", "Tiago", "0123456202316", "Pedro", "1990-11-05", 1)
cliente2.save()