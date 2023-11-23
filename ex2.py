

import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Conexão com o banco de dados
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hypeinblock"
)

# Função de verificação de login
def verificar_login():
    email = entrada_usuario.get()
    password = entrada_senha.get()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM caixa WHERE email = %s AND password = %s", (email, password))
    resultado = mycursor.fetchone()

    if resultado is None:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")
    else:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso.")

# Criação da janela
root = tk.Tk()

# Criação dos campos de entrada para usuário e senha
label_usuario = tk.Label(root, text="Usuário")
label_usuario.pack()
entrada_usuario = tk.Entry(root)
entrada_usuario.pack()

label_senha = tk.Label(root, text="Senha")
label_senha.pack()
entrada_senha = tk.Entry(root, show="*")
entrada_senha.pack()

# Botão para efetuar o login
botao_login = tk.Button(root, text="Login", command=verificar_login)
botao_login.pack()

root.mainloop()
