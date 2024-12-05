from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #processando os dados do formulário
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"Login efetuado com usuário {username}") 

    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)