import sqlite3
from pathlib import Path

def criar_tabelas():
    ROOT_PATH = Path(__file__).parent
    conn = sqlite3.connect(ROOT_PATH / "loja.db")
    cursor = conn.cursor()

    #cursor.execute("DROP TABLE sexo")

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sexo
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
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

def save_sexo(descricao):
    ROOT_PATH = Path(__file__).parent
    conn = sqlite3.connect(ROOT_PATH / "loja.db")
    cursor = conn.cursor()
    try:
        print("erro")
        cursor.execute('INSERT INTO sexo (descricao) VALUES(?)', (descricao))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


# **************** TELA USUÁRIO INICIAL ***************************

from Cliente import Cliente
from Endereco import Endereco

#criar_tabelas()

# save_sexo("M")
# save_sexo("F")

cliente1 = Cliente ( nome = 'Vitoria', primeiroNome = 'Pedro', cpf = '01234566789', contatos = 'Mãe', dataNascimento = "2010-10-12", versao = 5, id_sexo = 1)
cliente1.save()
cliente2 = Cliente( "Amanda", "Maria", "0123456202316", "Marisa", "1990-11-05", 1, 2)
cliente2.save()

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