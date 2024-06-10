import sqlite3
from pathlib import Path

class Produto:
    def __init__(self, dataCriacao, dataUltimaAtualizacao, nome, descricao, preco, foto, ativo, tags, versao, id_categoria ):
        self.dataCriacao = dataCriacao
        self.dataUltimaAtualizacao = dataUltimaAtualizacao
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.foto = foto
        self.ativo = ativo
        self.tags = tags
        self.versao = versao
        self.id_categoria = id_categoria

    def save(self):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor() 
        cursor.execute("INSERT INTO produtos (dataCriacao, dataUltimaAtualizacao, nome, descricao, preco, foto, ativo, tags, versao, id_categoria) VALUES(?,?,?,?,?,?,?,?,?,?)", (self.dataCriacao, self.dataUltimaAtualizacao, self.nome, self.descricao, self.preco, self.foto, self.ativo, self.tags, self.versao, self.id_categoria))
        conn.commit()
        conn.close()

    def update(self, id):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute('UPDATE produtos SET dataCriacao=?, dataUltimaAtualizacao=?, nome=?, descricao=?, preco=?, foto=?, ativo=?, tags=?, versao=?, id_categoria=? WHERE id = ?', (self.dataCriacao, self.dataUltimaAtualizacao, self.nome, self.descricao, self.preco, self.foto, self.ativo, self.tags, self.versao, self.id_categoria, id))
        conn.commit()
        conn.close()
    
    def delete(self, id):        
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        conn.execute("DELETE FROM produtos WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        conn.close()
        return [Produto (dataCriacao=row[0], dataUltimaAtualizacao=row[1], nome=row[2], descricao=row[3], preco=row[4], foto=row[5],ativo=row[6], tags=row[7], versao=row[8],id_categoria=row[9]  ) for row in produtos]
    
    @staticmethod
    def get_by_id(id):
        ROOT_PATH = Path(__file__).parent
        conn = sqlite3.connect(ROOT_PATH / "loja.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close
        if row:
            return Produto (dataCriacao=row[0], dataUltimaAtualizacao=row[1], nome=row[2], descricao=row[3], preco=row[4], foto=row[5],ativo=row[6], tags=row[7], versao=row[8],id_categoria=row[9]) 
        return None