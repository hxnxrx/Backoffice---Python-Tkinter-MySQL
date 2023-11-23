from tkinter import *
import mysql.connector
from tkinter import messagebox


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Hypeinblock"
)

root = Tk()

class Registration():
    def __init__(self):
        self.root=root
        self.tela()
        root.mainloop()
        
        
    def tela(self):
        self.root.title("Registro HYB")
        self.root.resizable(False,False)
        self.root.geometry("490x545")
        # Imagem de fundo
        self.fundo2 = PhotoImage(file="resources\\imagens\\2.png")
        self.lab_fundo2 = Label(self.root, image=self.fundo2)
        self.lab_fundo2.pack()

        # Labels e Entry para nome, email e password
        self.nome_ent = Entry(self.root)
        self.nome_ent.place(x=53, y=177, width=340,height=23)

        self.email_ent = Entry(self.root)
        self.email_ent.place(x=53, y=246, width=340,height=23)
        
        self.password_ent = Entry(self.root, show="*")
        self.password_ent.place(x=53, y=318, width=340,height=23)

        self.password_confirm_ent = Entry(self.root, show="*")
        self.password_confirm_ent.place(x=53, y=392, width=340,height=23)
        
        # Botões
        self.btt_confirm = Button(self.root, text="Confirmar", command=self.entrar)
        self.btt_confirm.place(x=338, y=434, width=60, height=30)

        self.btt_voltar = Button(self.root, text="Voltar", command=self.voltar_log)
        self.btt_voltar.place(x=338, y=490, width=60, height=30)

    def entrar(self):
        nome = self.nome_ent.get()
        email = self.email_ent.get()
        password = self.password_ent.get()
        password_confirm = self.password_confirm_ent.get()
        
        if nome and email and password and password_confirm:
            if password == password_confirm:
                try:
                    mycursor = mydb.cursor()
                    sql = "INSERT INTO caixa (nome, email, password) VALUES (%s, %s, %s)"
                    valores = (nome, email, password)
                    mycursor.execute(sql, valores)
                    mydb.commit()
                    messagebox.showinfo("Sucesso", "Registro inserido com sucesso.")
                except mysql.connector.Error as err:
                    messagebox.showerror("Erro", f"Erro ao inserir registro: {err}")
            else:
                messagebox.showerror("Erro", "As senhas digitadas não coincidem.")
                return
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")

    def voltar_log(self):
        root.destroy()
        self.main_mod = "main"
        self.mod = __import__(self.main_mod)
        print(self.mod)

Registration()
