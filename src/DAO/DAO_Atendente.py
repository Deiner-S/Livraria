from DAO.ABC import DAO


class DAO_Atendente(DAO):
    #   
    #
    # 
    def create(self, atendente):
        try:
            cursor = self._conexao.cursor()
            comando = """INSERT INTO Atendente VALUES(:nome,:email)"""
            cursor.execute(comando,{"nome":atendente.get_nome(),"email":atendente.get_email()})
            self._conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao tentar inserir dados: {e}")
            return False
    #   
    #
    #  
    def read(self, email):
        try:
            cursor = self._conexao.cursor()
            comando = """SELECT * FROM Atendente WHERE email=:email"""
            cursor.execute(comando, {"email":email})
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao tentar ler os dados: {e}")
            return False
    
    #   
    #
    #     
    def update(self, atendente):
        try:
            cursor = self._conexao.cursor()
            comando = """UPDATE Atendente SET nome = :nome WHERE email = :email"""
            cursor.execute(comando, {"nome": atendente.get_nome(), "email": atendente.get_email()})
            self._conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao tentar atualizar dados: {e}")
            return False        
    #   
    #
    # 
    def delete(self, email):
        try:
            cursor = self._conexao.cursor()
            comando = """DELETE FROM Atendente WHERE email = :email"""
            cursor.execute(comando, {"email":email})
            self._conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao tentar deletar dados: {e}")
            return False