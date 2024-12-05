class Atendente():    
    def __init__(self,nome,email):
        self._id = None
        self._nome = nome
        self._email = email

    def get_login(self):
        return self._login
    def set_login(self, new):
        self._login = new

    def get_id(self):
        return self._id
    def set_id(self, new):
        self._id = new

    def get_nome(self):
        return self._nome
    def set_nome(self, new):
        self._nome = new

    def get_email(self):
        return self._email
    def set_email(self, new):
        self._email = new
    
    def values():
        return "(:nome,:email)"
    

    

