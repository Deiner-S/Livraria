from DAO.ABC import DAO

class DAO_endereco(DAO):

    
    def create(self, endereco):
        try:
            cursor = self._conexao.cursor()
            comando = """INSERT INTO Endereco (fk_cliente_id,cep,rua,numero,bairro,complemento,cidade,estado) 
                         VALUES (:fk_cliente_id,:cep,:rua,:numero,:bairro,:complemento,:cidade,:estado)"""
            cursor.execute(comando, {
                "fk_cliente_id" : endereco.get_id_cliente(),
                "cep" : endereco.get_cep(),
                "rua" : endereco.get_rua(),
                "numero" : endereco.get_numero(),
                "bairro" : endereco.get_bairro(),
                "complemento" : endereco.get_complemento(),
                "cidade" : endereco.get_cidade(),
                "estado" : endereco.get_estado()
            })
            self._conexao.commit
            return True
        except Exception as e:
            print(f"Erro ao tentar inserir dados: {e}")
            return False
    #   
    #
    #
    # 
     
    def read(self, id):
        try:
           cursor = self._conexao.cursor()
           comando = """SELECT * FROM Endereco WHERE id = :id"""
           cursor.execute(comando, {"id":id})
           return cursor.fetchall()
        except Exception as e:
           print(f'Erro ao tentar ler dados: {e}')
           return False
    #   
    #
    #
         
    def update(self, endereco):
        try:
           cursor = self._conexao.cursor()
           comando = """UPDATE Endereco 
                        SET cep = :cep, 
                            rua = :rua, 
                            numero = :numero, 
                            bairro = :bairro, 
                            complemento = :complemento, 
                            cidade = :cidade, 
                            estado = :estado
                        WHERE id = :id"""
           cursor.execute(comando,{})
           self._conexao.commit()
           return True
        except Exception as e:
           print(f'Erro ao tentar: {e}')
           return False
        
    #   
    #
    #
     
    def delete(self, id):
        pass