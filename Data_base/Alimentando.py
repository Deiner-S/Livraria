import sys
sys.path.append('src')
from DAO.ABS import DAO
from models.Livro import Livro

"""with open("Data_base\Alimentandobanco\ISBN.txt","r",encoding="utf-8") as isbn:
    lista_isbn =  isbn.readlines()
with open("Data_base\Alimentandobanco\TITULO.txt","r",encoding="utf-8") as titulo:
    lista_titulo =  titulo.readlines()
with open("Data_base\Alimentandobanco\AUTOR.txt","r",encoding="utf-8") as autor:
    lista_autor =  autor.readlines()
with open("Data_base\Alimentandobanco\ASSUNTO.txt","r",encoding="utf-8") as assunto:
    lista_assunto =  assunto.readlines()
with open("Data_base\Alimentandobanco\EDITORA.txt","r",encoding="utf-8") as editora:
    lista_editora =  editora.readlines()
with open("Data_base\Alimentandobanco\CAPA.txt","r",encoding="utf-8") as capa:
    lista_capa =  capa.readlines()
tabela_livro = []    
for c1,c2,c3,c4,c5,c6 in zip(lista_isbn,lista_titulo,lista_autor,lista_assunto,lista_editora,lista_capa):
    
    
    tabela_livro.append((c1,c2,c3,c4,c5,"PORTUGUES",c6))"""
    
banco = DAO()
con = banco.connect()
cursor = con.cursor()
livro = Livro()

"""for i in tabela_livro:
    livro = Livro(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
    banco.create("Livro",cursor,livro)
    pass"""
cursor.close()
con.close()        
    