from DAO.ABC import DAO

class DAO_Nota_fiscal(DAO):
    
    
    
    def create(self, nota_fiscal):
        try:
           cursor = self._conexao.cursor()
           comando ="""INSERT INTO Nota_fiscal (acesso,cfop) VALUES (:acesso,:cfop)"""
           cursor.execute(comando,{"acesso":nota_fiscal.get_acesso(),"cfop":nota_fiscal.get_cfop()})
           self._conexao.commit()
           return cursor.lastrowid
        except Exception as e:
           print(f'Erro ao tentar inserir dados: {e}')
           return False
    #   
    #
    #
    # 
     
    def read(self, id):
        try:
           cursor = self._conexao.cursor()
           comando ="""SELECT * FROM Nota_fiscal WHERE id = :id"""
           cursor.execute(comando,{"id":id})
           self._conexao.commit()
           return cursor.fetchall()
        except Exception as e:
           print(f'Erro ao tentar ler dados: {e}')
           return False
    #   
    #
    #
         
    def update(self, nota_fiscal):
        try:
           cursor = self._conexao.cursor()
           comando ="""UPDATE Nota_fiscal SET cfop = :cfop WHERE id = :id"""
           cursor.execute(comando,{"cfop":nota_fiscal.get_cfop(),"id":nota_fiscal.get_id()})
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
           comando ="""DELETE FROM Nota_fiscal WHERE id = :id"""
           cursor.execute(comando,{"id":id})
           self._conexao.commit()
           return True
        except Exception as e:
           print(f'Erro ao tentar deletar dados: {e}')
           return False