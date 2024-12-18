from models.User import User

@login_manager.user_loader
def load_user(user_id):
    for usuario in usuarios:
        if usuario['id'] == int(user_id):
            return User(id=usuario['id'], username=usuario['username'])
    return None