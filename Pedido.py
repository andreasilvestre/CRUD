import sqlite3
from pathlib import Path

class Pedido:
    def __init__(self, id_cliente, id_endereco, id_notaFiscal, id_pagamento,id_statusPedido, dataCriacao, dataUltimaAtualizacao, dataConclusao, total, versao):
        #self.id = id
        self.id_cliente = id_cliente
        self.id_endereco = id_endereco
        self.id_notaFiscal = id_notaFiscal
        self.id_pagamento= id_pagamento
        self.id_statusPedido = id_statusPedido
        self.dataCriacao = dataCriacao
        self.dataUltimaAtualizacao = dataUltimaAtualizacao
        self.dataConclusao = dataConclusao
        self.total = total
        self.versao = versao

        
    # def __init__(self):
    #     pass

    def save(self):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO pedidos (id_cliente, id_endereco, id_notaFiscal, id_pagamento, id_statusPedido, dataCriacao, dataUltimaAtualizacao, dataConclusao, total, versao) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (self.id_cliente, self.id_endereco, self.id_notaFiscal, self.id_pagamento,self.id_statusPedido, self.dataCriacao, self.dataUltimaAtualizacao, self.dataConclusao, self.total, self.versao))
            self.id = cursor.lastrowid
            conn.commit()
            conn.close()
        except Exception as e:
            print("Erro ao salvar o pedido: " + e)
    
    def update(self, id):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute('UPDATE pedidos SET id_endereco = ?, id_statusPedido = ?, dataCriacao = ?, dataUltimaAtualizacao =?, dataConclusao = ?, total = ?, versao = ? WHERE id = ?', (self.id_endereco,self.id_statusPedido, self.dataCriacao, self.dataUltimaAtualizacao, self.dataConclusao, self.total, self.versao, id))
        print("erro ***********************")
        conn.commit()
        conn.close()

    def delete(self, id):        
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        conn.execute("DELETE FROM pedidos WHERE id = ?", (id,))
        #conn.execute("DELETE FROM clientes")
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedidos")
        pedidos = cursor.fetchall()
        conn.close()
        return [Pedido (id_cliente=row[0], id_endereco=row[1], id_notaFiscal=row[2], id_pagamento=row[3], id_statusPedido=row[4], dataCriacao=row[5], dataUltimaAtualizacao=row[6], dataConclusao=row[7], total=row[8], versao=row[9]) for row in pedidos]
    
    @staticmethod
    def get_by_id(id):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedidos WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close
        if row:
            return Pedido (id_cliente=row[0], id_endereco=row[1], id_notaFiscal=row[2], id_pagamento=row[3], id_statusPedido=row[4], dataCriacao=row[5], dataUltimaAtualizacao=row[6], dataConclusao=row[7], total=row[8], versao=row[9])
        return None