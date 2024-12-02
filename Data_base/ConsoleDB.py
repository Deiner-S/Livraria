import sqlite3 as db

try:
    conexao = db.connect("Data_base\data.db")
    cursor = conexao.cursor()
    
    comand1 = """CREATE TABLE Endereco (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    numero INT NOT NULL,
                    rua TEXT NOT NULL,
                    cep INT NOT NULL,
                    fk_Cliente_id INT NOT NULL,                    
                    FOREIGN KEY (fk_Cliente_id) REFERENCES Cliente (id)
                );
                """
    comand2 = """CREATE TABLE Cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    ie INT NOT NULL,
                    cnpj INT,
                    cpf INT,
                    Cliente_TIPO BLOB NOT NULL
                    
                );
              """
    comand3 = """CREATE TABLE Livro (
                    autor TEXT NOT NULL,
                    titulo TEXT NOT NULL,
                    idioma TEXT NOT NULL,
                    editora TEXT NOT NULL,
                    assunto TEXT NOT NULL,
                    isbn INT NOT NULL,
                    fk_Estoque_id INT NOT NULL,
                    peso REAL NOT NULL,
                    preco REAL NOT NULL,
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    FOREIGN KEY (fk_Estoque_id) REFERENCES Estoque (id)
                );
              """
    comand4 = """CREATE TABLE Estoque (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    exemplares INT NOT NULL
                
                );
              """
    
    comand5 = """CREATE TABLE Carrinho (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    exemplares INT NOT NULL
                    
                );
              """
    comand6 = """CREATE TABLE Atendente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL
                    
                );
              """
    comand7 = """CREATE TABLE Nota_Fiscal (
                    acesso INT NOT NULL,
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cfop INT NOT NULL
                    
                );
              """
    comand8 = """CREATE TABLE Adiciona_Carrinho (
                    fk_Cliente_id INT NOT NULL,
                    fk_Livro_id INT NOT NULL,
                    fk_Carrinho_id INT NOT NULL,                    
                    PRIMARY KEY(fk_Carrinho_id, fk_Livro_id),
                    FOREIGN KEY (fk_Cliente_id) REFERENCES Cliente (id),
                    FOREIGN KEY (fk_Livro_id) REFERENCES Livro (isbn),
                    FOREIGN KEY (fk_Carrinho_id) REFERENCES Carrinho (id)
                );
              """
    comand9 = """CREATE TABLE Compra_Cliente (
                    fk_Cliente_id INT NOT NULL,
                    fk_Carrinho_id INT NOT NULL,
                    fk_Nota_Fiscal_numero INT NOT NULL,
                    fk_Atendente_id INT NOT NULL,
                    data DATE NOT NULL,
                    operacao TEXT NOT NULL,
                    desconto REAL NOT NULL,
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    total REAL NOT NULL,
                    total_com_desconto REAL NOT NULL,
                    
                    FOREIGN KEY (fk_Cliente_id) REFERENCES Cliente (id),
                    FOREIGN KEY (fk_Carrinho_id) REFERENCES Carrinho (id),
                    FOREIGN KEY (fk_Nota_Fiscal_numero) REFERENCES Nota_Fiscal (numero),
                    FOREIGN KEY (fk_Atendente_id) REFERENCES Atendente (id)
                );
              """

    comand10 = """CREATE TABLE Login (
                    id INT NOT NULL,
                    login TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    fk_Atendente_id INT NOT NULL,
                    PRIMARY KEY (id, fk_Atendente_id)
                    FOREIGN KEY (fk_Atendente_id) REFERENCES Atendente (id)
                );"""        

    
    """cursor.execute(comand1)
    cursor.execute(comand2)
    cursor.execute(comand3)
    cursor.execute(comand4)
    cursor.execute(comand5)
    cursor.execute(comand6)
    cursor.execute(comand7)
    cursor.execute(comand8)
    """

    cursor.execute(comand10)
    conexao.commit()
    
    
    
    
    
    

except Exception as e:
    print(f"Erro inesperado: {e}")
    
    
    
finally:
    if conexao:
        cursor.close()
        conexao.close()