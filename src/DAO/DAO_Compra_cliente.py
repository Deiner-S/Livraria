from DAO.ABC import DAO

class DAO_Compra_cliente(DAO):
    
    def create(self, compra_cliente):
        try:
           cursor = self._conexao.cursor()
           comando = """INSERT INTO Compra_cliente VALUES(:id,:fk_carrinho_id,:fk_nota_Fiscal_id,:fk_atendente_id,:operacao,:data,:desconto,:total)"""
           cursor.execute(comando,{
                    "id" : compra_cliente.get_id(),
                    "fk_carrinho_id" : compra_cliente.get_id_carrinho(),
                    "fk_nota_Fiscal_id" : compra_cliente.get_id_notaFiscal(),
                    "fk_atendente_id" : compra_cliente.get_id_atendente(),
                    "operacao" : compra_cliente.get_operacao(),
                    "data" : compra_cliente.get_data(),
                    "desconto" : compra_cliente.get_desconto(),
                    "total" : compra_cliente.get_total(),
           })
           self._conexao.commit()
           return True
        except Exception as e:
           print(f'Erro ao tentar inserir dados: {e}')
           return False
    #   
    #
    #  
    def read(self, id):
        try:
           cursor = self._conexao.cursor()
           comando ="""SELECT * FROM Compra_cliente WHERE id = :id"""
           cursor.execute(comando,{"id":id})
           
           return cursor.fetchall()
        except Exception as e:
           print(f'Erro ao tentar ler dados: {e}')
           return False
    #   
    #
    #     
    def update(self, compra_cliente):
        try:
           cursor = self._conexao.cursor()
           comando = """UPDATE Compra_cliente 
                         SET operacao = :operacao,
                             desconto = :desconto
                         WHERE id = :id"""
                         
           cursor.execute(comando,{
                                    "operacao": compra_cliente.get_operacao(),
                                    "desconto": compra_cliente.get_desconto(),
                                    "id": compra_cliente.get_id()})
           self._conexao.commit()
           return True
        except Exception as e:
           print(f'Erro ao tentar atualizar dados: {e}')
           return False
        
    #   
    #
    # 
    def delete(self, id):
        try:
           cursor = self._conexao.cursor()
           comando ="""DELETE FROM Compra_cliente WHERE id=:id"""
           cursor.execute(comando,{"id":id})
           self._conexao.commit()
           return True
        except Exception as e:
           print(f'Erro ao tentar ao tentar deletar dados: {e}')
           return False