from flask_login import UserMixin
from DAO.DAO_Login import DAO_Login

class User(UserMixin):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    @staticmethod
    def get_user(username):
        dao_login = DAO_Login()
        login = dao_login.readIfTrue(username)
        dao_login.close()        
        
        return User(login[0][0], login[0][1])
        
    
    @staticmethod
    def authenticate(username, password):

        dao_login = DAO_Login()
        login = dao_login.readIfTrue(username)
        dao_login.close()

        if login[0][6] == password:
            return True
        else:
            return False
         
     