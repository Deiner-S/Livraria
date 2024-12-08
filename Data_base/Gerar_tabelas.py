import sqlite3 as db

try:
    conexao = db.connect("Data_base\data.db")
    cursor = conexao.cursor()
    
    comand1 = """CREATE TABLE Endereco (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fk_cliente_id INT NOT NULL,                    
                    cep TEXT NOT NULL,
                    rua TEXT NOT NULL,
                    numero TEXT NOT NULL,
                    bairro TEXT NOT NULL,
                    complemento TEXT NOT NULL,
                    cidade TEXT NOT NULL,
                    estado TEXT NOT NULL,
                    FOREIGN KEY (fk_cliente_id) REFERENCES Cliente (id)
                );
                """
    comand2 = """CREATE TABLE Cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cnpj TEXT NULL,
                    ie TEXT NULL,
                    cpf TEXT NULL,
                    Cliente_TIPO TEXT NOT NULL
                    
                );
              """
    comand3 = """CREATE TABLE Livro (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    isbn TEXT NOT NULL,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    assunto TEXT NOT NULL,
                    idioma TEXT NOT NULL,
                    editora TEXT NOT NULL,
                    estoque INT NOT NULL,                    
                    preco REAL NOT NULL
              );
              """
    comand6 = """CREATE TABLE Atendente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL                    
                );
              """
    comand7 = """CREATE TABLE Nota_Fiscal (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cfop TEXT NOT NULL,
                    acesso TEXT NOT NULL                    
                );
              """
    
    comand8 = """CREATE TABLE Carrinho (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fk_cliente_id INT NOT NULL,
                    fk_livro_id INT NOT NULL,
                    exemplares INT NOT NULL,
                    status BLOB NOT NULL,                                        
                    FOREIGN KEY (fk_cliente_id) REFERENCES Cliente (id),
                    FOREIGN KEY (fk_livro_id) REFERENCES Livro (id)
                );
              """
    comand9 = """CREATE TABLE Compra_Cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fk_carrinho_id INT NOT NULL,
                    fk_nota_Fiscal_numero INT NOT NULL,
                    fk_atendente_id INT NOT NULL,
                    operacao TEXT NOT NULL,
                    data DATE NOT NULL,
                    desconto REAL NOT NULL,
                    total REAL NOT NULL,                    
                    FOREIGN KEY (fk_carrinho_id) REFERENCES Carrinho (id),
                    FOREIGN KEY (fk_nota_Fiscal_numero) REFERENCES Nota_Fiscal (id),
                    FOREIGN KEY (fk_atendente_id) REFERENCES Atendente (id)
                );
              """

    comand10 = """CREATE TABLE Login (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fk_atendente_id INT NOT NULL,
                    ativo BLOB NOT NULL,
                    data_criacao DATE NOT NULL,
                    ultimo_acesso DATE NOT NULL,
                    login TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    FOREIGN KEY (fk_atendente_id) REFERENCES Atendente (id)
                );"""        

    
    cursor.execute(comand1)
    cursor.execute(comand2)
    cursor.execute(comand3)    
    cursor.execute(comand6)
    cursor.execute(comand7)
    cursor.execute(comand8)
    cursor.execute(comand9)
    cursor.execute(comand10)

    
    conexao.commit()
    
    
    
    
    
    

except Exception as e:
    print(f"Erro inesperado: {e}")
    
    
    
finally:
    if conexao:
        cursor.close()
        conexao.close()