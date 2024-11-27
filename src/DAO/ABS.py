from abc import ABC, abstractmethod
import sqlite3 as conexao


class DAO(ABC):    
    primaryKey = ""
    tabela = ""    
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
    @abstractmethod
    def create(self,cursor,obj):
        pass
    #   
    #
    #
    #  
    def read(self,cursor,cod):
        try:
            comando = f"""SELECT * FROM {self.tabela} WHERE {self.primaryKey} = '{cod}' """
            cursor.execute(comando)
            return cursor.fetchall()        
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
    #   
    #
    #
    #     
    def update(self,cursor,chave,coluna,update):
        try:
            comando = f"""UPDATE {self.tabela} SET {coluna}= ? WHERE {self.primaryKey}={chave};"""           
            cursor.execute(comando, (update,))            
            print("Dados atualizados com sucesso!")
            return True            
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
        
    #   
    #
    #
    # 
    def delete(self,cursor,cpf):
        #self.conexao.execute("PRAGMA foreign_keys = on")
        try:
            comando = f'''DELETE FROM {self.tabela} WHERE {self.primaryKey}= {cpf};'''
            cursor.execute(comando)            
            print("Cadastro removido")
            return True
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False