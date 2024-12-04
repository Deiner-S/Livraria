import sqlite3 as conexao

class DAO():    
        
    #
    #
    #
    #
    def connect(self):
       con = conexao.connect("Data_base\data.db", detect_types=conexao.PARSE_DECLTYPES) 
       return con                 
    #   
    #
    #
    # 
    
    def create(self,tabela,cursor,obj):
        try:
            comando = f"""INSERT INTO {tabela} VALUES {obj.values()};"""        
            cursor.execute(comando, vars(obj))
        except Exception as e:
            print(f"Erro banco de dados: {e}")
    #   
    #
    #
    #  
    def read(self,tabela,key,cursor,cod):
        try:
            comando = f"""SELECT * FROM {tabela} WHERE {key} = '{cod}' """
            cursor.execute(comando)
            return cursor.fetchall()        
        except Exception as e:
            print(f"Erro banco de dados: {e}")
            return False
    #   
    #
    #
    #     
    def update(self,tabela,key,cursor,chave,coluna,update):
        try:
            comando = f"""UPDATE {tabela} SET {coluna}= ? WHERE {key}={chave};"""           
            cursor.execute(comando, (update,))            
            print("Dados atualizados com sucesso!")
            return True            
        except Exception as e:
            print(f"Erro banco de dados: {e}")
            return False
        
    #   
    #
    #
    # 
    def delete(self,tabela,key,cursor,cpf):
        #self.conexao.execute("PRAGMA foreign_keys = on")
        try:
            comando = f'''DELETE FROM {tabela} WHERE {key}= {cpf};'''
            cursor.execute(comando)            
            print("Cadastro removido")
            return True
        except Exception as e:
            print(f"Erro banco de dados: {e}")
            return False