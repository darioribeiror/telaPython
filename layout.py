from tkinter import *

from matplotlib.pyplot import grid

root = Tk()

class Application():

    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()

    # Redimensionamento e configs da tela
    def tela(self):
        self.root.title("Canhotos Manual") ## Título da tela 
        self.root.configure(background='#C0C0C0') ## Cor de fundo
        self.root.geometry("700x500") ## Tamanho que a tela será exibida inicialmente
        self.root.resizable("true", "true") ## Permite redimensionar a tela (true/false)
        self.root.maxsize(width=900, height=700) ## Tamanho máximo que a tela poderá ser redimensionada  
        self.root.minsize(width=400, height=300) ## Tamanho mínimo que a tela poderá ser redimensionada 

    # Frames dentro da tela 
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg="#DCDCDC", highlightbackground='#A9A9A9', highlightthickness=2) ## Bordas frame 1
        self.frame_1.place(relx= 0.01, rely= 0.02, relwidth= 0.98, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd = 4, bg="#DCDCDC", highlightbackground='#A9A9A9', highlightthickness=2) ## Bordas frame 2
        self.frame_2.place(relx= 0.01, rely= 0.5, relwidth= 0.98, relheight= 0.46)

    ## Criando botões
    def widgets_frame1(self):
        ## Botão limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar")
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ## Botão buscar
        self.bt_limpar = Button(self.frame_1, text="Buscar")
        self.bt_limpar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ## Botão novo
        self.bt_limpar = Button(self.frame_1, text="Novo")
        self.bt_limpar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15) 
        ## Botão alterar
        self.bt_limpar = Button(self.frame_1, text="Alterar")
        self.bt_limpar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15) 
        ## Botão apagar
        self.bt_limpar = Button(self.frame_1, text="Apagar")
        self.bt_limpar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15) 

        ## Criação de label e entrada do código 
        self.lb_codigo = Label(self.frame_1,text="Código")
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ## Crianção da label e entrada de nome 
        self.lb_nome = Label(self.frame_1,text="Nome")
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        ## Crianção da label e entrada de telefone 
        self.lb_telefone = Label(self.frame_1,text="Telefone")
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        ## Crianção da label e entrada de cidade 
        self.lb_cidade = Label(self.frame_1,text="Cidade")
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
Application()

