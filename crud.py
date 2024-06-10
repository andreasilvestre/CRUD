import sqlite3
from pathlib import Path

def criar_tabelas():
    ROOT_PATH = Path(__file__).parent
    conn = sqlite3.connect(ROOT_PATH / "loja.db")
    cursor = conn.cursor()

    #cursor.execute("DROP TABLE clientes")

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sexo
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL)
        ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        id_sexo INTEGER,
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
    

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorias(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            versao INTEGER,
            nome TEXT)
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dataCriacao DATETIME,
            dataUltimaAtualizacao DATETIME,
            nome TEXT NOT NULL, 
            descricao TEXT, 
            preco BIGDECIMAL,
            foto BYTE, 
            ativo BOOLEAN, 
            tags TEXT, 
            versao INTEGER, 
            id_categoria INTEGER,
            CONSTRAINT fk_idCategoria 
            FOREIGN KEY (id_categoria) REFERENCES categorias(id)   
                   )
                   ''')
    
    # # Obter informações sobre a estrutura da tabela
    # cursor.execute("PRAGMA table_info(clientes)")
    # colunas = cursor.fetchall()
    # # Exibir as informações das colunas
    # for coluna in colunas:
    #     cid, nome, tipo, notnull, dflt_value, pk = coluna
    #     print(f"Nome da Coluna: {nome}, Tipo: {tipo}")


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

def save_categoria(versao, nome):
    ROOT_PATH = Path(__file__).parent
    conn = sqlite3.connect(ROOT_PATH / "loja.db")
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO categorias (versao, nome) VALUES(?,?)', (versao, nome))
        #cursor.execute("UPDATE categorias SET nome = ? WHERE id=?", (nome, id))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


# **************** TELA USUÁRIO INICIAL ***************************

from Cliente import Cliente
from Endereco import Endereco
from Produto import Produto

#criar_tabelas()

# save_sexo("M")
# save_sexo("F")
#save_categoria(12, "Calcinha", 8)
# save_categoria(10, "Camiseta")
# save_categoria(5, "Cueca")
# save_categoria(4, "Moleton")


# cliente1 = Cliente ( nome = 'Vitoria', primeiroNome = 'Pedro', cpf = '01234566789', contatos = 'Mãe', dataNascimento = "2010-10-12", versao = 5, id_sexo = 1)
# cliente1.save()
# cliente2 = Cliente( "Amanda", "Maria", "0123456202316", "Marisa", "1990-11-05", 1, 2)
# cliente2.save()

# endereco1 = Endereco(2, "37950-000", "Rua Pedro José", "230", "apto 2", "Verona", "Paraiso", "MG")
# endereco1.save()
# endereco2 = Endereco(2, "37925-000", "Rua Oliveira Rezende", "22", "loja", "Verona", "Paraiso", "MG")
# endereco2.save()

#cliente1.update(19)
#cliente1.delete(3)

#endereco1.update(1)
#endereco1.delete(1)

produto1 = Produto(dataCriacao="2024-05-25", dataUltimaAtualizacao="2024-06-30", nome="Saia", descricao="Saia rosa bordada", preco=23.20, foto=2, ativo=False, tags="saia, rosa, bordada", versao=5, id_categoria=3)
# produto1.save()
#produto1.update(2)
#produto1.delete(3)


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

#Listar todos os produtos:
print ("Produtos:")
produtos = Produto.get_all()
for produto in produtos:
    print(f"{produto.dataCriacao}, {produto.dataUltimaAtualizacao}, {produto.nome}, {produto.descricao}, {produto.preco}, {produto.foto}, {produto.ativo}, {produto.tags}, {produto.versao}, {produto.id_categoria}")

print ("Único Produto:")
produto = Produto.get_by_id(2)
print(f"\n{produto.dataCriacao}, {produto.dataUltimaAtualizacao}, {produto.nome}, {produto.descricao}, {produto.preco}, {produto.foto}, {produto.ativo}, {produto.tags}, {produto.versao}, {produto.id_categoria}")
