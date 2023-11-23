from tkinter import *
import os
import mysql.connector 
from tkinter import ttk, messagebox
import re

db = mysql.connector.connect(
    host="localhost",
    user= "root",
    password="",
    database="hypeinblock"
)

app = Tk()

class Aplication():
    def __init__(self):
        self.app=app
        self.tela()
        app.mainloop()

    def tela(self):
        self.app.title("cadastro de clientes")
        self.app.resizable(False,False)
        self.app.geometry("490x545")

        self.fundo = PhotoImage(file="resources\\imagens\\1.png")
        self.lab_fundo=Label(self.app,image=self.fundo)
        self.lab_fundo.pack()

        self.email_ent = Entry(self.app,font=("10"))
        self.email_ent.place(x=43.6,y=183,width=397.4,height=48.9)
        self.pass_ent = Entry(self.app,font=("10"),show="*")
        self.pass_ent.place(x=43.6,y=303,width=397.4,height=48.9)

        self.btt_entrar = Button(self.app,command=self.verificar_login,font=('Ivy',10),text="ENTRAR").place(x=195,y=400,width=100,height=40)
        self.btt_cadastrar = Button(app,command=self.importa_register,font=('Ivy', 10),text="FAZER CADASTRO").place(x=160,y=460,width=170,height=40)

    def verificar_login(self):
        email = self.email_ent.get()
        password = self.pass_ent.get()

        if not self.validar_email(email):
            messagebox.showerror("Erro", "Email inválido.")
            return

        if len(password) < 6:
            messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres.")
            return

        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM caixa WHERE email = %s AND password = %s", (email, password))
        resultado = mycursor.fetchone()

        if resultado is None:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")
        else:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso.")
            app.destroy()
            self.dash_mod = "dashboard"
            self.mod = __import__(self.dash_mod)
            print(self.mod)


    def validar_email(self,email):
        # Define a regex para validar o formato do email
        regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
        # Verifica se o email está no formato correto
        if re.match(regex_email, email):
            return True
        else:
            return False

    def importa_register(self):
        app.destroy()
        self.dash_mod = "register"
        self.mod = __import__(self.dash_mod)
        print(self.mod)

Aplication()
