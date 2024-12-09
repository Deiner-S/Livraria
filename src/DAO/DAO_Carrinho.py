from DAO.ABC import DAO

class DAO_Carrinho(DAO):
    #   
    #
    #
    def create(self, carrinho):
        try:
            cursor =  self._conexao.cursor()
            comando = """INSERT INTO Carrinho VALUES (:id,:fk_cliente_id,:fk_livro_id,:exemplar,:status);"""
            cursor.execute(comando, vars(carrinho))
            self._conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")
            return False
    #   
    #
    # 
    def read(self, id):
        try:
            cursor = self._conexao.cursor()
            comando = """SELEC * FROM Crrinho WHERE id = :id"""
            cursor.execute(comando, {":id": id})
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao tentar ler dados: {e}")
            return False
    #   
    #
    #     
    def update(self, carrinho):
        try:
            cursor = self._conexao.cursor()
            comando = """UPDATE Carrinho SET exemplar = :exemplar WHERE id = :id AND fk_livro_id = :fk_livro_id"""
            cursor.execute(comando, {"exemplar": carrinho.get_exemplar(),"id": carrinho.get_id(), "fk_livro_id": carrinho.get_id_Livro()})
            self._conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao tentar atualizar dados: {e}")
            return False
    #   
    #
    # 
    def delete(self, carrinho):
        try:
            cursor = self._conexao.cursor()
            comando = """DELETE FROM Carrinho WHERE id = :id AND fk_livro_id = :fk_livro_id"""
            cursor.execute(comando,{"id": carrinho.get_id(), "fk_livro_id": carrinho.get_id_Livro()})
            self._conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao tentar deletar dados: {e}")
            return False