import sys
sys.path.append('src')
from DAO.ABS import DAO
from models.Livro import Livro

with open("Data_base\ISBN.txt","r",encoding="utf-8") as isbn:
    lista_isbn =  isbn.readlines()
with open("Data_base\TITULO.txt","r",encoding="utf-8") as titulo:
    lista_titulo =  titulo.readlines()
with open("Data_base\AUTOR.txt","r",encoding="utf-8") as autor:
    lista_autor =  autor.readlines()
with open("Data_base\ASSUNTO.txt","r",encoding="utf-8") as assunto:
    lista_assunto =  assunto.readlines()
with open("Data_base\EDITORA.txt","r",encoding="utf-8") as editora:
    lista_editora =  editora.readlines()
with open("Data_base\CAPA.txt","r",encoding="utf-8") as capa:
    lista_capa =  capa.readlines()
tabela_livro = []    
for c1,c2,c3,c4,c5,c6 in zip(lista_isbn,lista_titulo,lista_autor,lista_assunto,lista_editora,lista_capa):
    
    
    tabela_livro.append((c1.strip(),c2.strip(),c3.strip(),c4.strip(),c5.strip(),"PORTUGUES",c6.strip()))
    
banco = DAO()
con = banco.connect()
cursor = con.cursor()

for i in tabela_livro:
    livro = Livro(i[0],i[1],i[2],i[3],i[4],i[5],0,i[6])
    comando = """
    INSERT INTO Livro (isbn, titulo, autor, assunto, idioma, editora, estoque, preco)
    VALUES (:isbn, :titulo, :autor, :assunto, :idioma, :editora, :estoque, :preco);
"""
    cursor.execute(comando, {
        'isbn': livro.get_isbn(),
        'titulo': livro.get_titulo(),
        'autor': livro.get_autor(),
        'assunto': livro.get_assunto(),
        'idioma': livro.get_idioma(),
        'editora': livro.get_editora(),
        'estoque': livro.get_estoque(),
        'preco': livro.get_preco()
    })
    con.commit()

cursor.close()
con.close()        
    