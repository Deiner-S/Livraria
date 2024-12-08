import sys
import time
sys.path.append("src")
from models.Atendente import Atendente
from DAO.DAO_Atendente import DAO_Atendente

from models.Cliente import Cliente
from DAO.DAO_Cliente import DAO_Cliente

from models.Livro import Livro
from DAO.DAO_Livro import DAO_Livro

def teste_livro():
    dao_livro = DAO_Livro()

    livro = Livro("978-3-16-148410-0","A Arte da Guerra", "Sun Tzu", "Estratégia / Filosofia", "Português", "Editora Nova Era", 50, 29.90)
    retorno1 = dao_livro.create(livro)
    print(retorno1)
    time.sleep(5)
    retorno2 = dao_livro.read(livro.get_isbn())
    print(retorno2)
    livro2 = Livro("978-3-16-148410-0", "O Grande Mistério", "João Silva", "Mistério / Ficção", "Português", "Editora Exemplo", 120, 39.90)
    retorno3 = dao_livro.update(livro2)
    print(retorno3)
    time.sleep(5)
    retorno4 = dao_livro.delete(livro2.get_isbn())
    print(retorno4)
    dao_livro.close()
    
    
def teste_cliente():
    dao_cliente = DAO_Cliente()
    cliente1 = Cliente("João Silva", "123.456.789-00", "Pessoa Física")

    retorno1 = dao_cliente.create(cliente1) 
    print(retorno1)
    time.sleep(5)
    retorno2 = dao_cliente.read(cliente1.get_cpf_cnpj())
    print(retorno2)

    cliente2 = Cliente("Deiner Rodrigues de Souza", "123.456.789-00", "Pessoa Física")

    retorno3 = dao_cliente.update(cliente2)
    print(retorno3)
    time.sleep(5)
    retorno4 = dao_cliente.delete(cliente2.get_cpf_cnpj())    
    print(retorno4)
    
    
    dao_cliente.close()
def teste_atendente():
    dao_atendente = DAO_Atendente()
    atendente1 = Atendente("João Silva", "joao.silva@email.com")

    retorno1 = dao_atendente.create(atendente1)         
    print(retorno1)
    time.sleep(5)
    retorno2 = dao_atendente.read(atendente1.get_email())    
    print(retorno2)

    atendente2 = Atendente("Deiner Rodrigues", "joao.silva@email.com")

    retorno3 = dao_atendente.update(atendente2)
    print(retorno3)
    time.sleep(5)
    retorno4 = dao_atendente.delete(atendente2.get_email())
    print(retorno4)
    
    
    dao_atendente.close()

def main():
    teste_atendente()   
        

if __name__ == ("__main__"):
    main()