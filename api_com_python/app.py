from flask import Flask
from flask import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'seu_usuario'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sua_senha'
app.config['MYSQL_DATABASE_DB'] = 'seu_banco_de_dados'
app.config['MYSQL_DATABASE_HOST'] = 'seu_host'

mysql = MySQL(app)

@app.route('/jogoos')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
