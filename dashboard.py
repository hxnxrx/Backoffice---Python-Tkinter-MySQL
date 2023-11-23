from tkinter import *
from PIL import ImageTk, Image
import os
import mysql.connector
from tkinter import ttk, messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING
import tkinter as tk

app=Tk()

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "hypeinblock"
)

class DashBoard(tk.Frame):
    def __init__(self,master=None):
        super().__init__()
        self.app=app
        self.current_frame = None
        self.tela()
        self.menu()
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Hypeinblock"
        )
        app.mainloop()

    def tela(self):
        self.app.title("DashBoard")
        self.app.geometry("1000x540")
        self.app.resizable(False,False)

        self.fundo=PhotoImage(file="resources\\imagens\\menu.png")
        self.lab_fundo = Label(self.app, image=self.fundo).pack()

    def menu(self):

        self.fornecedores=Button(self.app,text="Fornecedores",command=self.exibir_fornecedores).place(x=25,y=150,width=80,height=30)
        self.produtos=Button(self.app,text="Produtos",command=self.exibir_produtos).place(x=25,y=250,width=80,height=30)
        self.vendas=Button(self.app,text="Vendas",command=self.exibir_vendas).place(x=25,y=350,width=80,height=30)
        self.btt_sair=Button(self.app,text="Sair",command=self.sair).place(x=25,y=500,width=80,height=30)
        
        
    def Create_fornecedor(self):
        id_fornecedor = self.ident_fornecedor.get()
        nome = self.nomeent_fornecedor.get()
        email = self.emailent_fornecedor.get()
        fone = self.foneent_fornecedor.get()

        cursor = self.mydb.cursor()
        comando = f'INSERT INTO fornecedores (id, nome, email, telefone) VALUES ("{id_fornecedor}","{nome}","{email}","{fone}")'
        cursor.execute(comando)
        self.mydb.commit()
        messagebox.showinfo("Inserção","inserido com sucesso")
        
    
    def delete_fornecedor(self):
        id_fornecedor = int(self.ident_fornecedor.get())
        cursor = self.mydb.cursor()
        comando = f"DELETE FROM fornecedores WHERE id ={id_fornecedor}"
        cursor.execute(comando)
        self.mydb.commit()
        messagebox.showinfo("Exclusão","Fornecedor removido com sucesso")
        
    def search(self):
        id = int(self.ident_fornecedor.get())
        with mydb.cursor() as cursor:
            cursor.execute("SELECT * FROM fornecedores WHERE id = %s", (id,))
            results = cursor.fetchall()
        self.tv.delete(*self.tv.get_children())
        for row in results:
            self.tv.insert("", tk.END, values=row)
    
    def exibir_fornecedores(self):
        messagebox.showinfo("Fornecedores", "Exibindo fornecedores")
        self.frm_fornecedores=Frame(self.app,bg="#FFFFFF").place(x=0,y=0,height=110,width=1000)
        self.logo = Image.open("resources\\imagens\\LOGO.png")
        self.logo = self.logo.resize((90,90), Image.LANCZOS)
        self.tk_logo = ImageTk.PhotoImage(self.logo)
        logo_lb = Label(self.frm_fornecedores, image=self.tk_logo).place(x=900,y=5,height=90,width=90)
        #construção da tabela
        
        self.tv=ttk.Treeview(self.frm_fornecedores,columns=("ID","nome","email","telefone"),show="headings")
        self.tv.column("ID",minwidth=0,width=50,anchor=S)
        self.tv.column("nome",minwidth=0,width=250,anchor=S)
        self.tv.column("email",minwidth=0,width=250,anchor=S)
        self.tv.column("telefone",minwidth=0,width=100,anchor=S)
        self.tv.heading("ID",text="ID")
        self.tv.heading("nome",text="Nome")
        self.tv.heading("email",text="Email")
        self.tv.heading("telefone",text="Telefone")
        self.tv.place(x=140,y=120,width=830,height=390)
    
        #cria butoes CRUD      
        
        self.inserir=Button(self.frm_fornecedores,text="Inserir",command=self.Create_fornecedor,anchor=S)
        self.inserir.place(x=410,y= 30)
        self.deletar=Button(self.frm_fornecedores,text="Eliminar",command=self.delete_fornecedor)
        self.deletar.place(x=455,y=30)
        self.obter=Button(self.frm_fornecedores,text="Obter",command=self.search)
        self.obter.place(x=510,y=30)
        
        #Cria CAIXAS DE TEXTO PARA FUNCAO DA TABELA fornecedores

        self.lbid=Label(self.frm_fornecedores,text="ID:").place(x=5,y=10)
        self.ident_fornecedor=Entry(self.frm_fornecedores)
        self.ident_fornecedor.place(x=5,y=30)

        self.lbnome=Label(self.frm_fornecedores,text="Nome:").place(x=135,y=10)
        self.nomeent_fornecedor=Entry(self.frm_fornecedores)
        self.nomeent_fornecedor.place(x=135,y=30)
        
        self.lbemail=Label(self.frm_fornecedores,text="Email:").place(x=5,y=50)
        self.emailent_fornecedor=Entry(self.frm_fornecedores)
        self.emailent_fornecedor.place(x=5,y=70)
        
        self.lbfone=Label(self.frm_fornecedores,text="Telefone:").place(x=135,y=50)
        self.foneent_fornecedor=Entry(self.frm_fornecedores)
        self.foneent_fornecedor.place(x=135,y=70)


        
        # Consultar dados da tabela ligada ao banco de dados
        cursor = self.mydb.cursor()
        query = "SELECT * FROM fornecedores"
        cursor.execute(query)
        result = cursor.fetchall()

        # Inserir os dados na tabela
        for row in result:
            self.tv.insert("", "end", values=row)


    def Create_prod(self):
        id_produto= self.idprod_ent.get()
        nome_prod = self.nomeprod_ent.get()
        desc_prod = self.desc_ent.get()
        preco_prod = self.preco_ent.get()
        idfornecedor = self.idfornec_ent.get()
        img_prod =  self.imgprod_ent.get()

        cursor = self.mydb.cursor()
        comando = f'INSERT INTO produtos (id_produto, nome, descricao, preco, id, images) VALUES ("{id_produto}","{nome_prod}","{desc_prod}","{preco_prod}","{idfornecedor}","{img_prod}")'
        cursor.execute(comando)
        self.mydb.commit()
        messagebox.showinfo("Inserção","inserido com sucesso")

    def delete_produto(self):
        id_produto = int(self.idprod_ent.get())
        cursor = self.mydb.cursor()
        comando = f"DELETE FROM produtos WHERE id_produto={id_produto}"
        cursor.execute(comando)
        self.mydb.commit()
        messagebox.showinfo("Exclusão","Produto removido com sucesso")   

    def search_produtos(self):
        id = int(self.idprod_ent.get())
        with mydb.cursor() as cursor:
            cursor.execute("SELECT * FROM produtos WHERE id_produto = %s", (id,))
            results = cursor.fetchall()
        self.tv.delete(*self.tv.get_children())
        for row in results:
            self.tv.insert("", tk.END, values=row)
    

    def exibir_produtos(self):
        messagebox.showinfo("Produtos", "Exibindo produtos")        
        #construção da tabela

        self.frm_produtos=Frame(self.app,bg="#FFFFFF").place(x=0,y=0,height=110,width=1000)

        self.logo = Image.open("resources\\imagens\\LOGO.png")
        self.logo = self.logo.resize((90,90), Image.LANCZOS)
        self.tk_logo = ImageTk.PhotoImage(self.logo)
        logo_lb = Label(self.frm_produtos, image=self.tk_logo).place(x=900,y=5,height=90,width=90)

        self.tv=ttk.Treeview(self.frm_produtos,columns=("ID","nome","desc","preco","id_fornecedor","imag"),show="headings")
        self.tv.column("ID",minwidth=0,width=50,anchor=S)
        self.tv.column("nome",minwidth=0,width=100,anchor=S)
        self.tv.column("desc",minwidth=0,width=250,anchor=S)
        self.tv.column("preco",minwidth=0,width=50,anchor=S)
        self.tv.column("id_fornecedor",minwidth=0,width=100,anchor=S)
        self.tv.column("imag",minwidth=0,width=0,anchor=S)
        
        self.tv.heading("ID",text="ID")
        self.tv.heading("nome",text="Nome")
        self.tv.heading("desc",text="Descrição")
        self.tv.heading("preco",text="Preço")
        self.tv.heading("id_fornecedor",text="N_Fornecedor")
        self.tv.heading("imag",text="Imagem")
        self.tv.place(x=140,y=120,width=830,height=390)
        self.tv["displaycolumns"] = ("ID", "nome", "desc", "preco", "id_fornecedor")
        #cria butoes CRUD

        self.inserir=Button(self.frm_produtos,text="Inserir",command=self.Create_prod,anchor=S)
        self.inserir.place(x=410,y= 30)
        self.deletar=Button(self.frm_produtos,text="Eliminar",command=self.delete_produto)
        self.deletar.place(x=455,y=30)
        self.obter=Button(self.frm_produtos,text="Obter",command=self.search_produtos)
        self.obter.place(x=510,y=30)
        
        #Cria CAIXAS DE TEXTO PARA FUNCAO DA TABELA fornecedores
        
        self.lbid=Label(self.frm_produtos,text="ID:").place(x=5,y=10)
        self.idprod_ent=Entry(self.frm_produtos)
        self.idprod_ent.place(x=5,y=30)
        
        self.lbnome=Label(self.frm_produtos,text="Nome:").place(x=135,y=10)
        self.nomeprod_ent=Entry(self.frm_produtos)
        self.nomeprod_ent.place(x=135,y=30)
        
        self.lb_desc=Label(self.frm_produtos,text="Descrição:").place(x=5,y=50)
        self.desc_ent=Entry(self.frm_produtos)
        self.desc_ent.place(x=5,y=70)
        
        self.lbpreco_prod=Label(self.frm_produtos,text="Preço:").place(x=135,y=50)
        self.preco_ent=Entry(self.frm_produtos)
        self.preco_ent.place(x=135,y=70)
        
        self.id_fornec=Label(self.frm_produtos,text="ID Fornecedor:").place(x=265,y=10)
        self.idfornec_ent=Entry(self.frm_produtos)
        self.idfornec_ent.place(x=265,y=30)

        self.imgprod_lb=Label(self.frm_produtos,text="Imagem:").place(x=265,y=50)
        self.imgprod_ent=Entry(self.frm_produtos)
        self.imgprod_ent.place(x=265,y=70)
        
        
        # Consultar dados da tabela ligada ao banco de dados
        cursor = self.mydb.cursor()
        query = "SELECT * FROM produtos"
        cursor.execute(query)
        result = cursor.fetchall()

        # Inserir os dados na tabela
        for row in result:
            self.tv.insert("", "end", values=row)


    def exibir_vendas(self):
        
        
        messagebox.showinfo("Vendas", "Exibindo vendas")        
        #construção da tabela
        self.frm_vendas = Frame(self.app,background="#FFFFFF").place(x=0,y=0,height=110,width=1000)

        self.logo = Image.open("resources\\imagens\\LOGO.png")
        self.logo = self.logo.resize((90,90), Image.LANCZOS)
        self.tk_logo = ImageTk.PhotoImage(self.logo)
        logo_lb = Label(self.frm_vendas, image=self.tk_logo).place(x=900,y=5,height=90,width=90)

        self.tv=ttk.Treeview(self.frm_vendas,columns=("ID_venda","ID_vendedor","ID_cliente","data_v","valor_total"),show="headings")
        self.tv.column("ID_venda",minwidth=0,width=50,anchor=S)
        self.tv.column("ID_vendedor",minwidth=0,width=100,anchor=S)
        self.tv.column("ID_cliente",minwidth=0,width=250,anchor=S)
        self.tv.column("data_v",minwidth=0,width=50,anchor=S)
        self.tv.column("valor_total",minwidth=0,width=100,anchor=S)

        self.tv.heading("ID_venda",text="ID")
        self.tv.heading("ID_vendedor",text="ID_Vendedor")
        self.tv.heading("ID_cliente",text="ID Cliente")
        self.tv.heading("data_v",text="Data venda")
        self.tv.heading("valor_total",text="Valor Total")
        self.tv.place(x=140,y=120,width=830,height=390)
    #cria butoes CRUD

        self.inserir=Button(self.frm_vendas,text="Inserir",command=self.create_venda,anchor=S)
        self.inserir.place(x=410,y= 30) 
        self.deletar=Button(self.frm_vendas,text="Eliminar",command=self.delete_venda)
        self.deletar.place(x=455,y=30)
        self.obter=Button(self.frm_vendas,text="Obter",command=self.search_vendas)
        self.obter.place(x=510,y=30)


        #Cria CAIXAS DE TEXTO PARA FUNCAO DA TABELA VENDAS


        self.lbid = Label(self.frm_vendas,text="ID_Venda:").place(x=5,y=10)
        self.idvenda_ent = Entry(self.frm_vendas)
        self.idvenda_ent.place(x=5,y=30)

        self.lbdatavenda = Label(self.frm_vendas,text="Data_venda:").place(x=135,y=10)
        self.datavenda_ent = Entry(self.frm_vendas)
        self.datavenda_ent.place(x=135,y=30)

        self.lbidcliente = Label(self.frm_vendas,text="ID Cliente:").place(x=5,y=50)
        self.idcliente_ent = Entry(self.frm_vendas)
        self.idcliente_ent.place(x=5,y=70)
        
        self.lbpreco = Label(self.frm_vendas,text="Preço:").place(x=135,y=50)
        self.preco_ent = Entry(self.frm_vendas)
        self.preco_ent.place(x=135,y=70)
        
        self.lbidcaixa = Label(self.frm_vendas,text="ID Caixa:").place(x=265,y=10)
        self.idcaixa_ent = Entry(self.frm_vendas)
        self.idcaixa_ent.place(x=265,y=30)

        # Consultar dados da tabela ligada ao banco de dados
        cursor = self.mydb.cursor()
        query = "SELECT * FROM vendas"
        cursor.execute(query)
        result = cursor.fetchall()

        # Inserir os dados na tabela
        for row in result:
            self.tv.insert("", "end", values=row)

    def create_venda(self):
        id_venda = self.idvenda_ent.get()
        id_caixa = self.idcaixa_ent.get()
        id_cliente = self.idcliente_ent.get()
        data_venda = self.datavenda_ent.get()
        valor_total = self.preco_ent.get()

        cursor = self.mydb.cursor()
        comando = f'INSERT INTO vendas (id_venda, id_caixa, id_cliente, data_venda, valor_total) VALUES ("{id_venda}","{id_caixa}","{id_cliente}","{data_venda}","{valor_total}")'
        cursor.execute(comando)
        self.mydb.commit()
        messagebox.showinfo("Inserção","vendas inserida com sucesso")

    def delete_venda(self):
        id_venda = int(self.idvenda_ent.get())
        cursor = self.mydb.cursor()
        comando = f"DELETE FROM vendas WHERE id_venda={id_venda}"
        cursor.execute(comando)
        self.mydb.commit()
        messagebox.showinfo("Exclusão","Venda removida com sucesso")   

    def search_vendas(self):
        id = int(self.idvenda_ent.get())
        with mydb.cursor() as cursor:
            cursor.execute("SELECT * FROM vendas WHERE id_venda = %s", (id,))
            results = cursor.fetchall()
        self.tv.delete(*self.tv.get_children())
        for row in results:
            self.tv.insert("", tk.END, values=row)
    
    def sair(self):
        resp = askokcancel(
            title="confirme saida",
            message="Tem certeza que deseja sair")
        if resp:
            self.app.destroy()



DashBoard()
