import sys
import time
sys.path.append("src")

import util.Util as u

from models.Login import Login
from DAO.DAO_Login import DAO_Login

from models.Nota_fiscal import Nota_fiscal
from DAO.DAO_Nota_fiscal import DAO_Nota_fiscal

from models.Compra_cliente import Compra_cliente
from DAO.DAO_Compra_cliente import DAO_Compra_cliente

from models.Endereco import Endereco
from DAO.DAO_Endereco import DAO_Endereco

from models.Carrinho import Carrinho
from DAO.DAO_Carrinho import DAO_Carrinho

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
    
def teste_endereco():
    dao_endereco = DAO_Endereco()
    endereco = Endereco(101, "12345-678", "Rua Exemplo", 123, "Bairro Central", "Apto 202", "Cidade Exemplo", "SP")
    retorno1 = dao_endereco.create(endereco)
    endereco.set_id(retorno1)
    print(retorno1)
    time.sleep(5)

    retorno2 =dao_endereco.read(endereco.get_id())
    print(retorno2)
    endereco1 = Endereco(101, "98765-432", "Avenida das Rosas", 456, "Jardim Primavera", "Bloco 3", "Metropolis", "RJ")
    endereco1.set_id(retorno1)
    retorno3 =dao_endereco.update(endereco1)
    print(retorno3)
    time.sleep(5)    
    retorno4 = dao_endereco.delete(endereco.get_id())
    print(retorno4)
    
    dao_endereco.close()
        
def teste_carrinho():
    dao_carrinho = DAO_Carrinho()
    carrinho1 = Carrinho(1, 101, 202, 1)
    
    retorno1 = dao_carrinho.create(carrinho1)
    print(retorno1)
    time.sleep(5)
    
    retorno2 = dao_carrinho.read(carrinho1.get_id())
    print(retorno2)
    
    carrinho2 = Carrinho(1, 101, 202, 2)
    retorno3 = dao_carrinho.update(carrinho2)
    print(retorno3)
    time.sleep(5)
    retorno4 = dao_carrinho.delete(carrinho2)
    print(retorno4)
    
    dao_carrinho.close()

def teste_compra_cliente():
    dao_compra_cliente = DAO_Compra_cliente()
    id_compra = u.id_alfanumerico()
    compra_cliente = Compra_cliente(id_compra,123, 456, 789, '2024-12-09', 'compra', 10.0, 150.75)
    
    retorno1 = dao_compra_cliente.create(compra_cliente)
    print(retorno1)
    
    retorno2 = dao_compra_cliente.read(compra_cliente.get_id())
    print(retorno2)
    
    compra_cliente.set_desconto(20.00)
    compra_cliente.set_operacao("comodt")
    
    retorno3 = dao_compra_cliente.update(compra_cliente)
    print(retorno3)
    
    retorno4 = dao_compra_cliente.delete(compra_cliente.get_id())
    print(retorno4)
    dao_compra_cliente.close()
    
def teste_nota_fiscal():
    dao_nota_fiscal = DAO_Nota_fiscal()
    
    nota_fiscal = Nota_fiscal('Liberado', 1234)
    retorno1 = dao_nota_fiscal.create(nota_fiscal)
    nota_fiscal.set_id(retorno1)
    print(retorno1)
    retorno2 = dao_nota_fiscal.read(nota_fiscal.get_id())
    print(retorno2)
    nota_fiscal.set_cfop("5102")
    retorno3 = dao_nota_fiscal.update(nota_fiscal)
    print(retorno3)
    retorno4 = dao_nota_fiscal.delete(nota_fiscal.get_id())
    print(retorno4)
    
    dao_nota_fiscal.close()

def teste_login():
    dao_login = DAO_Login()
    login = Login(1, True, '2024-01-01', '2024-12-10 09:00:00', 'atendente01', 'senha123')

    retorno1 = dao_login.create(login)
    login.set_id(retorno1)
    print(retorno1)
    retorno2 = dao_login.read(login.get_id())
    print(retorno2)
    login.set_ativo(False)
    login.set_ultimo_login("14/11/2024")
    retorno3 = dao_login.update(login)
    print(retorno3)
    retorno4 = dao_login.delete(login.get_id())
    print(retorno4)

    dao_login.close()
def main():
    teste_atendente()
    teste_carrinho()
    teste_cliente()
    teste_compra_cliente()
    teste_endereco()
    teste_livro()
    teste_login()
    teste_nota_fiscal()    
if __name__ == ("__main__"):
    main()