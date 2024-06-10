import sqlite3
from pathlib import Path

class Cliente:
    def __init__(self, nome, primeiroNome, cpf, contatos, dataNascimento, versao, id_sexo):
        #self.id = id
        self.nome = nome
        self.primeiroNome = primeiroNome
        self.cpf = cpf
        self.contatos = contatos
        self.dataNascimento = dataNascimento
        self.versao = versao
        self.id_sexo = id_sexo
    
    def save(self):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO clientes (nome, primeiroNome, cpf, contatos, dataNascimento, versao, id_sexo) VALUES(?, ?, ?, ?, ?, ?, ?)', (self.nome, self.primeiroNome, self.cpf, self.contatos, self.dataNascimento, self.versao, self.id_sexo))
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
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        conn.execute("DELETE FROM clientes WHERE id = ?", (id,))
        #conn.execute("DELETE FROM clientes")
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        conn.close()
        return [Cliente (nome=row[1], primeiroNome=row[2], cpf=row[3], contatos=row[4], dataNascimento=row[5], versao=row[6]) for row in clientes]
    
    @staticmethod
    def get_by_id(id):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close
        if row:
            return Cliente (nome=row[1], primeiroNome=row[2], cpf=row[3], contatos=row[4], dataNascimento=row[5], versao=row[6])
        return None