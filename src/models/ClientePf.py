from Cliente import Cliente

class ClientePF(Cliente):
    def __init__(self,nome, cpf):
        super().__init__(nome)        
        self._cpf = cpf

    def get_cpf(self):
        return self._cpf
    def set_cpf(self, new):
        self._cpf = new
    
    def values():
        return "(:nome,:cpf,:tipo)"
        
        