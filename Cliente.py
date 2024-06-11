import sqlite3
from pathlib import Path

class Cliente:
    def __init__(self, id, nome, primeiroNome, cpf, contatos, dataNascimento, versao, id_sexo):
        self.id = id
        self.nome = nome
        self.primeiroNome = primeiroNome
        self.cpf = cpf
        self.contatos = contatos
        self.dataNascimento = dataNascimento
        self.versao = versao
        self.id_sexo = id_sexo
    
    # def __init__(self):
    #     pass
    
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
        #self.id = id
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        # cursor.execute('UPDATE clientes SET nome = ?, primeiroNome = ?, cpf = ?, contatos = ? dataNascimento = ?, versao = ? WHERE id = ?', (self.nome, self.primeiroNome, self.cpf, self.contatos, self.dataNascimento, self.versao, id))
        # o update não aceitou atualizar o campo dataNascimento, não sei o motivo ainda
        cursor.execute('UPDATE clientes SET nome = ?, primeiroNome = ?, cpf = ?, contatos = ?, versao = ? WHERE id = ?', (self.nome, self.primeiroNome, self.cpf, self.contatos, self.versao, id))
        conn.commit()
        conn.close()

    def delete(id):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id =?", (id,))
        conn.commit()
        conn.close()
        print(f"Cliente {id} excluído com sucesso!")

    @staticmethod
    def get_all():
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, primeiroNome, cpf, contatos, dataNascimento, versao, id_sexo FROM clientes")
        clientes = cursor.fetchall()
        conn.close()
        return [Cliente (id=row[0], nome=row[1], primeiroNome=row[2], cpf=row[3], contatos=row[4], dataNascimento=row[5], versao=row[6], id_sexo=row[7]) for row in clientes]
    
    
    @staticmethod
    def get_by_id(id):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, primeiroNome, cpf, contatos, dataNascimento, versao, id_sexo FROM clientes WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close
        if row:
            return Cliente (id=row[0], nome=row[1], primeiroNome=row[2], cpf=row[3], contatos=row[4], dataNascimento=row[5], versao=row[6], id_sexo=row[7])
        return None