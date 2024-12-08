import sys
sys.path.append('src')
from DAO.DAO_Livro import DAO_Livro
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
    
banco = DAO_Livro()


for i in tabela_livro:
    livro = Livro(i[0],i[1],i[2],i[3],i[4],i[5],0,i[6])
    banco.create(livro)

banco.close()
    


      
    