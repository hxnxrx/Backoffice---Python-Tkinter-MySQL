from tkinter import *
from tkinter import ttk
import mysql.connector 

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "hypeinblock"
)
cursor = con.cursor()


def Create():
     id_produto = "1"
     nome_produto = "sneackers""chocolate"
     descr="barra-chocolate"
     preco = 15
     comando = f'INSERT INTO produtos (id_produto,nome,descricao,preco) VALUES ({id_produto},"{nome_produto}","{descr}",{preco})'
     cursor.execute(comando)
     con.commit() # edita o banco de dados

def Read():
    comando = f'SELECT * FROM produtos'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler o banco de dados
    print(resultado)

Read()