from DAO.ABC import DAO

class DAO_Cliente(DAO):
    #   
    #
    #
    # 
    
    def create(self, cliente):
        try:
            cursor = self._conexao.cursor()
            comando = """INSERT INTO Cliente (nome,cpf_cnpj,cliente_tipo) 
                        VALUES (:nome,:cpf_cnpj,:cliente_tipo); """
            cursor.execute(comando, {
                "nome": cliente.get_nome(),
                "cpf_cnpj":cliente.get_cpf_cnpj(),
                "cliente_tipo":cliente.get_cliente_tipo()           
            })
            self._conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao tentar cadastrar dados: {e}")
            return False

    #   
    #
    #
    # 
     
    def read(self, cpf_cnpj):
        try:
            cursor = self._conexao.cursor()
            comando = """SELECT * FROM Cliente WHERE cpf_cnpj = :cpf_cnpj;"""
            cursor.execute(comando, {"cpf_cnpj": cpf_cnpj})

            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao tentar ler dados: {e}")
            return False
        
    #   
    #
    #
         
    def update(self, cliente):
        try:
            cursor = self._conexao.cursor()
            comando = '''UPDATE Cliente 
                         SET 
                            nome = :nome
                         WHERE 
                            cpf_cnpj= :cpf_cnpj;'''
            
            cursor.execute(comando, {'nome': cliente.get_nome(),"cpf_cnpj": cliente.get_cpf_cnpj()})
            self._conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar dados: {e}")
            return False
        pass
        
    #   
    #
    #
     
    def delete(self, cpf_cnpj):
        try:
            cursor = self._conexao.cursor()
            comando = """DELETE FROM Cliente WHERE  cpf_cnpj=:cpf_cnpj;"""
            cursor.execute(comando, {"cpf_cnpj":cpf_cnpj})
            self._conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao tentar deletar dados: {e}")
            return False        