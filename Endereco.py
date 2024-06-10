import sqlite3
from pathlib import Path

class Endereco:
    def __init__(self, id_cliente, CEP, logradouro, numero, complemento, bairro, cidade, estado):
        self.id_cliente = id_cliente
        self.CEP = CEP
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def save(self):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO enderecos(id_cliente, CEP, logradouro, numero, complemento, bairro, cidade, estado) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (self.id_cliente, self.CEP, self.logradouro, self.numero, self.complemento, self.bairro, self.cidade, self.estado))
        conn.commit()
        conn.close()
    
    def update(self, id):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn. cursor()
        cursor.execute ("UPDATE enderecos SET CEP = ?, logradouro = ?, numero = ?, complemento =?, bairro = ?, cidade = ?, estado =? WHERE id = ?",( self.CEP, self.logradouro, self.numero, self.complemento, self.bairro, self.cidade, self.estado, id))
        conn.commit()
        conn.close()
    
    def delete(self, id):        
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        conn.execute("DELETE FROM enderecos WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def get_all():
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM enderecos")
        clientes = cursor.fetchall()
        conn.close()
        return [Endereco (id_cliente = row[0], CEP = row[1], logradouro = row[2], numero = row[3], complemento = row[4], bairro = row[5],cidade = row[6], estado = row[7]) for row in clientes]
    
    
    def get_by_id(id):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM enderecos WHERE id =?", (id,))
        row = cursor.fetchone()
        conn.close
        if row:
            return Endereco (id_cliente = row[0], CEP = row[1], logradouro = row[2], numero = row[3], complemento = row[4], bairro = row[5], cidade = row[6], estado = row[7])
        return None