from tkinter import *
from tkinter import ttk
import sqlite3
from matplotlib.pyplot import grid

root = Tk()

## Funções front-end
class Funcs(): 
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor(); print("Conectado ao banco de dados")
    
    def desconecta_bd(self):
        self.conn.close(); print("Desconectado do banco de dados")
    
    def montatabelas(self):
        self.conecta_bd(); 
        ## Cria tabela 
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS CLIENTES(
                    COD INTEGER PRIMARY KEY,
                    NOME_CLIENTE CHAR(40) NOT NULL,
                    TELEFONE INTERGER(20),
                    CIDADE CHAR(40)
                );
            """)

        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()

    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()
        
        self.cursor.execute("""INSERT INTO CLIENTES (NOME_CLIENTE, TELEFONE, CIDADE) VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT COD, NOME_CLIENTE, TELEFONE, CIDADE FROM CLIENTES ORDER BY NOME_CLIENTE ASC; """)
        
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()

    def onDoubleClick(self, event):

        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            Col1, Col2, Col3, Col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, Col1)
            self.nome_entry.insert(END, Col2)
            self.telefone_entry.insert(END, Col3)
            self.cidade_entry.insert(END, Col4)
    
    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM CLIENTES WHERE COD = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()
        
    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE CLIENTES SET NOME_CLIENTE = ?, TELEFONE = ?, CIDADE = ? WHERE COD = ?""", (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

class Application(Funcs):

    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montatabelas()
        self.select_lista()
        self.Menus()
        root.mainloop()

    ## Funções back-end
    # Redimensionamento e configs da tela
    def tela(self):
        self.root.title('Criando Tela') ## Título da tela 
        self.root.configure(background='#C0C0C0') ## Cor de fundo
        self.root.geometry('700x500') ## Tamanho que a tela será exibida inicialmente
        self.root.resizable('true', 'true') ## Permite redimensionar a tela (true/false)
        self.root.maxsize(width=900, height=700) ## Tamanho máximo que a tela poderá ser redimensionada  
        self.root.minsize(width=400, height=300) ## Tamanho mínimo que a tela poderá ser redimensionada 

    # Frames dentro da tela 
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg='#DCDCDC', highlightbackground='#A9A9A9', highlightthickness=2) ## Bordas frame 1
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd = 4, bg='#DCDCDC', highlightbackground='#A9A9A9', highlightthickness=2) ## Bordas frame 2
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)

    ## Criando botões
    def widgets_frame1(self):
        ## Botão limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#696969', fg='white', font=('caribe', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ## Botão buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#696969', fg='white', font=('caribe', 8, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ## Botão novo
        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#696969', fg='white', font=('caribe', 8, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15) 
        ## Botão alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#696969', fg='white', font=('caribe', 8, 'bold'), command=self.altera_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15) 
        ## Botão apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#696969', fg='white', font=('caribe', 8, 'bold'), command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15) 

        ## Criação de label e entrada do código 
        self.lb_codigo = Label(self.frame_1,text='Código', bg='#DCDCDC', fg='#696969')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ## Crianção da label e entrada de nome 
        self.lb_nome = Label(self.frame_1,text='Nome', bg='#DCDCDC', fg='#696969')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        ## Crianção da label e entrada de telefone 
        self.lb_telefone = Label(self.frame_1,text='Telefone', bg='#DCDCDC', fg='#696969')
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        ## Crianção da label e entrada de cidade 
        self.lb_cidade = Label(self.frame_1,text='Cidade', bg='#DCDCDC', fg='#696969')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
    
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=("Col1", "Col2", "COl3", "Col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.onDoubleClick) ## Chama a função de double click

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label = "Opções", menu= filemenu)
        menubar.add_cascade(label = "sobre", menu= filemenu2)

        filemenu.add_command(label="Sair", command= Quit)
        filemenu2.add_command(label= "Limpa Cliente", command= self.limpa_tela)




Application()

