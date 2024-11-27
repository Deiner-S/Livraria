import sqlite3 as db

try:
    conexao = db.connect("Data_base\data.db")
    cursor = conexao.cursor()
    
    comand = """DROP TABLE Livro"""
                
    comand0 = """CREATE TABLE Livro( 
                    isbn INT NOT NULL,  
                    autor TEXT NOT NULL,  
                    titulo TEXT NOT NULL,  
                    assunto TEXT NOT NULL,  
                    editora TEXT NOT NULL,  
                    idioma TEXT NOT NULL,  
                    fk_idEstoque INT NOT NULL,  
                    preco REAL NOT NULL, 
                    PRIMARY KEY(isbn),
                    FOREIGN KEY(fk_idEstoque) REFERENCES Estoque (id)
                );""" 

    comand1 =   """CREATE TABLE Cliente( 
                    nome TEXT NOT NULL,  
                    id INT NOT NULL,                
                    PRIMARY KEY(id),                
                    );""" 

    comand2 =   """CREATE TABLE Atendente( 
                    id INT NOT NULL,  
                    nome TEXT NOT NULL,
                    PRIMARY KEY(id)
                    ); """

    comand3 =   """CREATE TABLE Endereco(
                    id INT NOT NULL,
                    cep INT NOT NULL,  
                    numero INT NOT NULL,  
                    rua TEXT NOT NULL,
                    complemento NULL,
                    fk_idCliente NOT NULL,               
                    PRIMARY KEY(id),
                    PRIMARY KEY(fk_idCliente),
                    FOREIGN KEY(fk_idCliente) REFERENCES Cliente (id)                
                    );""" 

    comand4 =   """CREATE TABLE NFe( 
                    numero INT NOT NULL,  
                    chave INT NOT NULL,  
                    cfop INT NOT NULL, 
                    PRIMARY KEY(numero)
                    );""" 

    comand5 =   """CREATE TABLE Estoque( 
                    exemplares INT NOT NULL,  
                    id INT NOT NULL,
                    PRIMARY KEY(id)
                    );""" 

    comand6 =   """CREATE TABLE Pedido( 
                    id INT NOT NULL,  
                    fk_idLivro INT NOT NULL,  
                    fk_idCliente INT NOT NULL,  
                    precoTotal REAL NOT NULL,  
                    PRIMARY KEY(id),
                    FOREIGN KEY(fk_idLivro) REFERENCES Livro (isbn),    
                    FOREIGN KEY(fk_idCliente) REFERENCES Cliente (id)
                    );""" 

    comand7 =   """CREATE TABLE Retirada( 
                    id INT NOT NULL,  
                    fk_idEstoque INT NOT NULL,  
                    PRIMARY KEY(id),
                    FOREIGN KEY(fk_idEstoque) REFERENCES Estoque (id)
                    );""" 

    comand8 =   """CREATE TABLE Venda( 
                    id INT NOT NULL,
                    data DATE NOT NULL,
                    consignacao BLOB NOT NULL,  
                    fk_idRetirada INT NOT NULL,  
                    fk_idAtendente INT NOT NULL,  
                    fk_idpedido INT NOT NULL,  
                    fk_idNFe INT NOT NULL,  
                    data DATE NOT NULL,  
                    PRIMARY KEY(id),
                    FOREIGN KEY(fk_idRetirada) REFERENCES Retirada (id),
                    FOREIGN KEY(fk_idAtendente) REFERENCES Atendente (id),
                    FOREIGN KEY(fk_idpedido) REFERENCES Pedido (id),
                    FOREIGN KEY(fk_idNFe) REFERENCES NFe (numero)
                
                    );""" 
                
    comand95 =  """CREATE TABLE Pessoa_fisica( 
                    cpf INT NOT NULL,  
                    fk_idCliente INT NOT NULL,  
                    PRIMARY KEY(fk_idCliente),
                    FOREIGN KEY(fk_idCliente) REFERENCES Cliente (id)
                    );""" 
                    
    comand9 =   """CREATE TABLE Pessoa_juridica( 
                    ie INT NOT NULL,  
                    cnpj INT NOT NULL,
                    fk_idCliente INT NOT NULL,  
                    PRIMARY KEY(fk_idCliente),
                    FOREIGN KEY(fk_idCliente) REFERENCES Cliente (id)
                    );""" 


            

    cursor.execute(comand0)
    cursor.execute(comand1)
    cursor.execute(comand2)
    cursor.execute(comand3)
    cursor.execute(comand4)
    cursor.execute(comand5)
    cursor.execute(comand6)
    cursor.execute(comand7)
    cursor.execute(comand8)
    cursor.execute(comand9)
    cursor.execute(comand95)
    
    conexao.commit()
    
    
    
    
    
    

except Exception as e:
    print(f"Erro inesperado: {e}")
    
    
    
finally:
    if conexao:
        cursor.close()
        conexao.close()