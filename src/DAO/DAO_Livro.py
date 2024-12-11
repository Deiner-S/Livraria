from DAO.ABC import DAO

class DAO_Livro(DAO): 
    
    def create(self, livro):
        try: 
            cursor = self._conexao.cursor()

            comando = """INSERT INTO Livro VALUES (:isbn, :titulo, :autor, :assunto, :idioma, :editora, :estoque, :preco);"""                       
            
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

            self._conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao tentar cadastrar dados: {e}")
            return False
    #   
    #
    #
    #     
    def read(self, isbn):
        try: 
            cursor = self._conexao.cursor()

            comando = '''SELECT * FROM Livro WHERE isbn=:isbn;'''

            cursor.execute(comando, {"isbn": isbn})
            
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao ler dados: {e}")

    def read_all(self):
        try:
           cursor = self._conexao.cursor()
           comando ="""SELECT * FROM Livro"""
           cursor.execute(comando,{})
           return cursor.fetchall()
        except Exception as e:
           print(f'Erro ao tentar ler dados: {e}')
           return False
    #   
    #
    #
    #    
    def update(self, livro):
        try:
            cursor = self._conexao.cursor()
            comando = '''UPDATE Livro 
                         SET 
                            titulo= :titulo,
                            autor= :autor,
                            assunto= :assunto,
                            idioma= :idioma,
                            editora= :editora,
                            estoque= :estoque,
                            preco= :preco,
                            isbn= :isbn
                         WHERE 
                            isbn= :isbn;'''
            
            cursor.execute(comando, {
                'titulo': livro.get_titulo(),
                'autor': livro.get_autor(),
                'assunto': livro.get_assunto(),
                'idioma': livro.get_idioma(),
                'editora': livro.get_editora(),
                'estoque': livro.get_estoque(),
                'preco': livro.get_preco(),
                'isbn': livro.get_isbn()
            })
            self._conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar dados: {e}")
            return False
        
    #    
    #   
    #
    #     
    def delete(self, isbn):
        try:
            cursor = self._conexao.cursor()

            comando = '''DELETE FROM Livro WHERE isbn=:isbn;'''

            cursor.execute(comando, {"isbn": isbn})

            self._conexao.commit() 
            return True
        except Exception as e:
            print(f"Erro ao deletar dados: {e}")
            return False

        

       

