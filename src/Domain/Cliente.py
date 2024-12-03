class Cliente():
    def __init__(self,id,nome):
        self._id = id
        self._nome = nome

    def get_id(self):
        return self._id
    def set_id(self, new):
        self._id = new
    
    def get_nome(self):
        return self._nome
    def set_nome(self, new):
        self._nome = new    