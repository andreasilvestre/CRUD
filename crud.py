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
      
def criar_tabelas():
    ROOT_PATH = Path(__file__).parent
    conn = sqlite3.connect(ROOT_PATH / "loja.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sexo
        (id TEXT PRIMARY KEY,
        descricao TEXT NOT NULL)
        ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        id_sexo TEXT,
        nome TEXT NOT NULL,
        primeiroNome TEXT NOT NULL, 
        cpf TEXT NOT NULL, 
        contatos TEXT NOT NULL, 
        dataNascimento DATETIME, 
        versao INTEGER,   
        CONSTRAINT fk_IdSexo
        FOREIGN KEY (id_sexo) REFERENCES sexo(id))
    ''')
    
    
    # cursor.execute('''
    #     ALTER TABLE clientes
    #         ADD id_sexo TEXT
    #                ''')

    #cursor.execute("ALTER TABLE clientes DROP COLUMN COLLUMN")

    #cursor.execute('ALTER TABLE enderecos MODIFY (id) PRIMARY KEY AUTO INCREMENT')
    #cursor.execute("DROP TABLE enderecos")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enderecos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            CEP TEXT NOT NULL,
            logradouro TEXT NOT NULL,
            numero TEXT NOT NULL,
            complemento TEXT,
            bairro TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            id_cliente INTEGER,
            CONSTRAINT fk_IdCliente
            FOREIGN KEY (id_cliente) REFERENCES clientes(id)
            )
        ''')
    conn.commit()
    conn.close()

#criar_tabelas()

def save_sexo(id, descricao):
    ROOT_PATH = Path(__file__).parent
    conn = sqlite3.connect(ROOT_PATH / "loja.db")
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO sexo (id, descricao) VALUES(?, ?)', (id, descricao))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


# **************** TELA USUÁRIO INICIAL ***************************

# save_sexo("M","Masculino")
# save_sexo("F", "Feminino")

# cliente1 = Cliente ( nome = 'Pedro Augusto', primeiroNome = 'Pedro', cpf = '01234566789', contatos = 'Mãe', dataNascimento = "2010-10-12", versao = 5, id_sexo = "M")
# cliente1.save()
# cliente2 = Cliente( "Maria da Silva", "Maria", "0123456202316", "Marisa", "1990-11-05", 1, "F")
# cliente2.save()

# endereco1 = Endereco(2, "37950-000", "Rua Pedro José", "230", "apto 2", "Verona", "Paraiso", "MG")
# endereco1.save()
# endereco2 = Endereco(2, "37925-000", "Rua Oliveira Rezende", "22", "loja", "Verona", "Paraiso", "MG")
# endereco2.save()

#cliente1.update(19)
#cliente1.delete(3)

#endereco1.update(1)
#endereco1.delete(1)


# # Listar todos os clientes
# print('Clientes:')
# clientes = Cliente.get_all()
# #for cliente in clientes: - funciona assim também
# for cliente in Cliente.get_all():
#     print(f'Nome: {cliente.nome}, Data Nascimento: {cliente.dataNascimento}')

# cliente = Cliente.get_by_id(1)
# print (f'\nNome: {cliente.nome}, Data de Nascimento:{cliente.dataNascimento}')

# Listar todos os endereços:
# print ("Endereços:")
# enderecos = Endereco.get_all()
# for endereco in enderecos:
#     print(f"{endereco.id_cliente} {endereco.logradouro} {endereco.numero} {endereco.complemento} {endereco.bairro} {endereco.cidade} {endereco.estado} {endereco.CEP}")

# print ("Único Endereço:")
# endereco = Endereco.get_by_id(2)
# print(f"{endereco.id_cliente} {endereco.logradouro} {endereco.numero} {endereco.complemento} {endereco.bairro} {endereco.cidade} {endereco.estado} {endereco.CEP}")