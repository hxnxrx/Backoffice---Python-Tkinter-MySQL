import tkinter as tk
import mysql.connector
from tkinter import ttk

# Cria conexão com o banco de dados MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hypeinblock"
)

# Cria janela tkinter
root = tk.Tk()
root.title("Pesquisa por ID")

# Cria treeview
tree = ttk.Treeview(root)
tree.pack()

# Cria função de pesquisa
def search():
    id = int(id_entry.get())
    with mydb.cursor() as cursor:
        cursor.execute("SELECT * FROM fornecedores WHERE id_fornecedor = %s", (id,))
        results = cursor.fetchall()
    tree.delete(*tree.get_children())
    for row in results:
        tree.insert("", tk.END, values=row)

# Cria entrada e botão de pesquisa
id_label = tk.Label(root, text="ID:")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()
search_button = tk.Button(root, text="Pesquisar", command=search)
search_button.pack()

# Inicia janela tkinter
root.mainloop()

# Fecha conexão com o banco de dados
mydb.close()
