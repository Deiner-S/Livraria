import sqlite3 as conexao
from abc import ABC, abstractmethod

class DAO(ABC):
    def __init__(self):
        self._conexao = conexao.connect("Data_base\data.db")            
    #   
    #
    #
    # 
    @abstractmethod
    def create(self, ett):
        pass
    #   
    #
    #
    # 
    @abstractmethod 
    def read(self, id):
        pass
    #   
    #
    #
    @abstractmethod     
    def update(self, ett):
        pass
        
    #   
    #
    #
    @abstractmethod 
    def delete(self, id):
        pass
    
    def close(self):
        self._conexao.close()
        