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
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS statusPedido(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL)
                   ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notaFiscal(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            xml BYTE,
            dataEmissao DATETIME,
            versao INTEGER)
                   ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS statusPagamento(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL)
                   ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS statusPagamento(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL)
                   ''')
   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagamentoBoleto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dataVencimento DATETIME,
            codigoBarras TEXT NOT NULL)
                   ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagamentoCartao(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numeroCartao TEXT NOT NULL)
                   ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagamento(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            versao INTEGER,
            id_statusPagamento INTEGER,
            id_pagamentoBoleto INTEGER,
            id_pagamentoCartao INTEGER,
            CONSTRAINT fk_idStatusPagamento
            FOREIGN KEY (id_statusPagamento) REFERENCES statusPagamento(id),
            CONSTRAINT fk_idPagamentoBoleto
            FOREIGN KEY (id_PagamentoBoleto) REFERENCES  pagamentoBoleto (id),
            CONSTRAINT fk_idPagamentoCartao
            FOREIGN KEY (id_PagamentoCartao) REFERENCES  pagamentoCartao (id)
                   )
                   ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dataCriacao DATETIME,
            dataUltimaAtualizacao DATETIME,
            dataConclusao DATETIME,
            total BIGDECIMAL,
            versao INTEGER,
            id_cliente INTEGER,
            id_statusPedido INTEGER,
            id_endereco iNTEGER,
            id_notaFiscal INTEGER,
            id_pagamento INTEGER,
            CONSTRAINT fk_idCliente
            FOREIGN KEY (id_cliente) REFERENCES clientes(id),
            CONSTRAINT fk_idStatusPedido
            FOREIGN KEY (id_statusPedido) REFERENCES statusPedido(id),
            CONSTRAINT fk_idEndereco
            FOREIGN KEY (id_endereco) REFERENCES enderecos(id),
            CONSTRAINT fk_idNotaFiscal
            FOREIGN KEY (id_notaFiscal) REFERENCES notaFiscal(id),
            CONSTRAINT fk_idPagamento
            FOREIGN KEY (id_pagamento) REFERENCES pagamento(id)
                   )
        ''') 
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS itensPedido(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            precoProduto BIGDECIMAL,
            quantidade INTEGER,
            versao INTEGER,
            id_produto INTEGER,
            id_pedido INTEGER,
            CONSTRAINT fk_idProduto
            FOREIGN KEY (id_produto) REFERENCES produtos(id),
            CONSTRAINT fk_idPedido
            FOREIGN KEY (id_pedido) REFERENCES pedidos(id))
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

def save_statusPedido(status):
    ROOT_PATH = Path(__file__).parent
    conn = sqlite3.connect(ROOT_PATH / "loja.db")
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO statusPedido (status) VALUES(?)', (status,))
        #cursor.execute("UPDATE statusPedido SET nome = ? WHERE id=?", (nome, id))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

def save_statusPagamento(status):
    ROOT_PATH = Path(__file__).parent
    conn = sqlite3.connect(ROOT_PATH / "loja.db")
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO statusPagamento (status) VALUES(?)', (status,))
        #cursor.execute("UPDATE statusPedido SET nome = ? WHERE id=?", (nome, id))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


# **************** TELA USUÁRIO INICIAL ***************************

from Cliente import Cliente
from Endereco import Endereco
from Produto import Produto
from Pedido import Pedido

#criar_tabelas()

# save_sexo("M")
# save_sexo("F")
#save_categoria(12, "Calcinha", 8)
# save_categoria(10, "Camiseta")
# save_categoria(5, "Cueca")
# save_categoria(4, "Moleton")

# save_statusPedido("Aguardando")
# save_statusPedido("Cancelado")
# save_statusPedido("Pago")

# save_statusPagamento("Processando")
# save_statusPagamento("Cancelado")
# save_statusPagamento("Recebido")


# cliente1 = Cliente ( nome = 'Vitoria', primeiroNome = 'Pedro', cpf = '01234566789', contatos = 'Mãe', dataNascimento = "2010-10-12", versao = 5, id_sexo = 1)
# cliente1.save()
# cliente2 = Cliente( "Amanda", "Maria", "0123456202316", "Marisa", "1990-11-05", 1, 2)
# cliente2.save()

# endereco1 = Endereco(2, "37950-000", "Rua Pedro José", "230", "apto 2", "Verona", "Paraiso", "MG")
# endereco1.save()
# endereco2 = Endereco(2, "37925-000", "Rua Oliveira Rezende", "22", "loja", "Verona", "Paraiso", "MG")
# endereco2.save()

# pedido1 = Pedido(id_cliente=1, id_endereco=1, id_notaFiscal=0, id_pagamento=0,id_statusPedido=2, dataCriacao="2024-01-10", dataUltimaAtualizacao="2024-02-30", dataConclusao="2024-05-15", total=350.20, versao=1)
#pedido1.save()
#print ("error")

#cliente1.update(19)
#cliente1.delete(3)

#endereco1.update(1)
#endereco1.delete(1)

# pedido1.update(2)
# pedido1.delete(3)

# produto1 = Produto(dataCriacao="2024-05-25", dataUltimaAtualizacao="2024-06-30", nome="Saia", descricao="Saia rosa bordada", preco=23.20, foto=2, ativo=False, tags="saia, rosa, bordada", versao=5, id_categoria=3)
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

# #Listar todos os produtos:
# print ("Produtos:")
# produtos = Produto.get_all()
# for produto in produtos:
#     print(f"{produto.dataCriacao}, {produto.dataUltimaAtualizacao}, {produto.nome}, {produto.descricao}, {produto.preco}, {produto.foto}, {produto.ativo}, {produto.tags}, {produto.versao}, {produto.id_categoria}")

# print ("Único Produto:")
# produto = Produto.get_by_id(2)
# print(f"\n{produto.dataCriacao}, {produto.dataUltimaAtualizacao}, {produto.nome}, {produto.descricao}, {produto.preco}, {produto.foto}, {produto.ativo}, {produto.tags}, {produto.versao}, {produto.id_categoria}")

# #Listar todos os produtos:
# print ("Pedidos:")
# pedidos = Pedido.get_all()
# for pedido in pedidos:
#     print(f"{pedido.id_cliente}, {pedido.id_endereco}, {pedido.id_notaFiscal}, {pedido.id_pagamento}, {pedido.id_statusPedido}, {pedido.dataCriacao}, {pedido.dataUltimaAtualizacao}, {pedido.dataConclusao}, {pedido.total}, {pedido.versao}")

# print ("Único Pedido:")
# pedido = Pedido.get_by_id(2)
# print(f"\n{pedido.id_cliente}, {pedido.id_endereco}, {pedido.id_notaFiscal}, {pedido.id_pagamento}, {pedido.id_statusPedido}, {pedido.dataCriacao}, {pedido.dataUltimaAtualizacao}, {pedido.dataConclusao}, {pedido.total}, {pedido.versao}")

def incluir_cliente():
    print("Digite os dados do cliente: \n")
    nome = input("Nome: ")
    primeiroNome = input ("Primeiro Nome: ")
    cpf = input("CPF: ")
    contatos = input("Contatos: ")
    dataNascimento = input("Data de Nascimento: ")
    versao = input ("versao: ")
    id_sexo = input("Sexo ([1] para masculino, [2] para feminino): ")

    cliente1 = Cliente (0, nome, primeiroNome, cpf, contatos, dataNascimento, versao, id_sexo)
    if cliente1.save():
        print ("Cliente salvo com sucesso")

def consultar_cliente():
    # Listar todos os clientes
    print('Clientes:')
    #for cliente in clientes: - funciona assim também
    for cliente in Cliente.get_all():
        #print(f'Nome: {cliente.nome}, Data Nascimento: {cliente.dataNascimento}')
        print(f"{cliente.id}, {cliente.nome}, {cliente.primeiroNome}, {cliente.cpf}, {cliente.contatos}, {cliente.dataNascimento}, {cliente.versao}, {cliente.id_sexo}")

    # cliente = Cliente.get_by_id(1)
    # print (f'\nNome: {cliente.nome}, Data de Nascimento:{cliente.dataNascimento}')

def alterar_cliente():
    id = int(input("Digite o id do cliente: "))
    cliente = Cliente.get_by_id(id)
    print(f"Id:{cliente.id}, Nome:{cliente.nome}, Primeiro Nome: {cliente.primeiroNome}, CPF: {cliente.cpf}, Contatos: {cliente.contatos}, Data de Nacimento: {cliente.dataNascimento}, Versão: {cliente.versao}, Id sexo: {cliente.id_sexo}\n")

    novo_nome = input(f"Novo nome (atual: {cliente.nome}): ")
    novo_primeiroNome = input(f"Novo primeiro nome (atual: {cliente.primeiroNome}): ")
    novo_cpf = input(f"Novo CPF (atual: {cliente.cpf}): ")
    novo_contatos = input(f"Novos contatos (atual: {cliente.contatos}): ")
    nova_dataNascimento = input(f"Nova data de Nascimento (atual: {cliente.dataNascimento}): ")
    nova_versao = input(f"Nova versao (atual: {cliente.versao}): ")
    novo_idSexo = input(f"Novo id_sexo (atual: {cliente.id_sexo}): ")
    
    cliente1 = Cliente(cliente.id, novo_nome, novo_primeiroNome,novo_cpf, novo_contatos, nova_dataNascimento, nova_versao, novo_idSexo)

    cliente1.update(cliente.id)

def excluir_cliente():
    id = int(input("Digite o id do cliente: "))
    cliente = Cliente.get_by_id(id)
    print(f"{cliente.id}, {cliente.nome}, {cliente.primeiroNome}, {cliente.cpf}, {cliente.contatos}, {cliente.dataNascimento}, {cliente.versao}, {cliente.id_sexo}\n")
    cliente = Cliente.delete(id)

def cadastro_clientes():
    while True:
        print('''
          [1] Incluir Clientes
          [2] Consultar Clientes
          [3] Alterar Clientes
          [4] Excluir Clientes
          [0] Sair do Cadastro de Clientes
          ''')
        opcao = input("Digite o que deseja fazer: ")
        if opcao == "1":
            print("Entrando no módulo de Inclusão de clientes")
            incluir_cliente()
        elif opcao == "2":
            print("Entrando no módulo de Consulta de Clientes")
            consultar_cliente()
        elif opcao == "3":
            print("Entrando no módulo de Alteração de Clientes")
            alterar_cliente()
        elif opcao == "4":
            print("Entrando no módulo de Exclusão de Clientes")
            excluir_cliente()
        elif opcao == "0":
            print("Saindo do módulo de Cadastro de Clientes!")
            break
    

while True:
    print('''
          [1] Cadastro de Clientes
          [2] Cadastro de Produtos
          [3] Cadastro de Pedidos
          [0] Sair do Sistema
          ''')
    opcao = input("Digite o que deseja fazer: ")
    if opcao == "1":
        print("Entrando no módulo de Cadastro de clientes")
        cadastro_clientes()
    elif opcao == "2":
        print("Entrando no módulo de Cadastro de Produtos")
    elif opcao == "3":
        print("Entrando no módulo de Cadastro de Pedidos")
    elif opcao == "0":
        print("Saindo do sistema!")
        break
    

