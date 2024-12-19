from DAO.ABC import DAO

class DAO_Login(DAO):
    
    def create(self, login):
      try:
         cursor = self._conexao.cursor()
         comando ="""INSERT INTO Login (fk_atendente_id,ativo,data_criacao,ultimo_login,login,senha) 
                     VALUES (:fk_atendente_id,:ativo,:data_criacao,:ultimo_login,:login,:senha)"""
         cursor.execute(comando,{"fk_atendente_id" :login.get_id_atendente(),
                                 "ativo" :login.get_ativo(),
                                 "data_criacao" :login.get_data_criacao(),
                                 "ultimo_login" :login.get_ultimo_login(),
                                 "login" :login.get_login(),
                                 "senha" :login.get_senha()})
         self._conexao.commit()
         return cursor.lastrowid
      except Exception as e:
         print(f'Erro ao tentar inserir dados: {e}')
         return False
    #   
    #
    #
    #
    def readIfTrue(self,email):
      try:
         cursor = self._conexao.cursor()
         comando ="""SELECT * FROM Login WHERE email = :email AND ativo = :ativo"""
         cursor.execute(comando,{"id":email,"ativo":True})
         self._conexao.commit()
         return cursor.fetchall()
      except Exception as e:
         print(f'Erro ao tentar ler dados: {e}')
         return False  
    #
    # 
    #
    #  
    def read(self, email):
      try:
         cursor = self._conexao.cursor()
         comando ="""SELECT * FROM Login WHERE email = :email"""
         cursor.execute(comando,{"id":email})
         self._conexao.commit()
         return cursor.fetchall()
      except Exception as e:
         print(f'Erro ao tentar ler dados: {e}')
         return False
    #   
    #
    #
         
    def update(self, login):
      try:
         cursor = self._conexao.cursor()
         comando ="""UPDATE Login SET ultimo_login = :ultimo_login, ativo = :ativo WHERE id = :id"""
         cursor.execute(comando,{
            "ultimo_login":login.get_ultimo_login(),
            "ativo":login.get_ativo(),
            "id":login.get_id()})
         self._conexao.commit()
         return True
      except Exception as e:
         print(f'Erro ao tentar: {e}')
         return False
        
    #   
    #
    #     
    def delete(self, id):
      try:
         cursor = self._conexao.cursor()
         comando ="""DELETE FROM Login WHERE id = :id"""
         cursor.execute(comando,{"id":id})
         self._conexao.commit()
         return True
      except Exception as e:
         print(f'Erro ao tentar deletar dados: {e}')
         return False