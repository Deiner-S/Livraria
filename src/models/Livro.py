class Livro():
    def __init__(self,isbn,titulo,autor,assunto,editora,idioma,estoque,preco):
        self._id = None
        self._isbn = isbn
        self._titulo = titulo 
        self._autor = autor
        self._assunto = assunto
        self._editora = editora
        self._idioma = idioma
        self._estoque = estoque
        self._preco = preco
    
    def get_id(self):
        return self._id
    def set_id(self, new):
        self._id = new
    
    def get_isbn(self):
        return self._isbn
    def set_isbn(self, new):
        self._isbn = new
        
    def get_titulo(self):
        return self._titulo
    def set_titulo(self, new):
        self._titulo = new

    def get_autor(self):
        return self._autor
    def set_autor(self, new):
        self._autor = new

    def get_assunto(self):
        return self._assunto
    def set_assunto(self, new):
        self._assunto = new

    def get_editora(self):
        return self._editora
    def set_editora(self, new):
        self._editora = new

    def get_idioma(self):
        return self._idioma
    def set_idioma(self, new):
        self._idioma = new

    def get_preco(self):
        return self._preco
    def set_preco(self, new):
        self._preco = new

    def get_estoque(self):
       return self._estoque
    def set_estoque(self,new):
       self._estoque= new
    
    def values():
        return "(:isbn,:titulo,:autor,:assunto,:idioma,:editora,:estoque,:preco)"