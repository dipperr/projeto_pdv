import tkinter as tk
from tkinter import ttk
from tkinter import Menu


class JanelaCadastrarProduto(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.__set_configs()

    def __set_configs(self):
        self.geometry('600x400')
        self.title('Cadastro de Produtos')
        self.mainloop()


class JanelaCadastrarCliente(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.__set_configs()

    def __set_configs(self):
        self.geometry('600x400')
        self.title('Cadastro de Cliente')
        self.mainloop()

    
class JanelaCadastrarVendedor(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.__set_configs()

    def __set_configs(self):
        self.geometry('600x400')
        self.title('Cadastro de Vendedor')
        self.mainloop()   


class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__set_configs()
        self.__set_labels()
        self.__set_entrys()
        self.__set_frame()
        self.__set_treview()
        self.__set_menubar()

    
    def __set_configs(self):
        self.geometry('800x600')
        self.title('PDV')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    def __set_labels(self):
        self.lcodigo = ttk.Label(self, text='Código', font=('Helvetica', 15))
        self.lcodigo.place(relx=0.02, rely=0.02)

    def __set_entrys(self):
        self.ecodigo = ttk.Entry(self)
        self.ecodigo.place(relx=0.02, rely=0.06, relwidth=0.2)

    def __set_frame(self):
        self.frame = ttk.Frame(self)
        self.frame.place(relx=0, rely=0.13, relwidth=1, relheight=0.87)

    def __set_treview(self):
        ids = ('cod', 'nome', 'preco', 'qtd')
        self.tree = ttk.Treeview(self.frame, columns=ids, show='headings')
        self.tree.heading('cod', text='Código')
        self.tree.heading('nome', text='Nome')
        self.tree.heading('preco', text='Preço')
        self.tree.heading('qtd', text='Quantidade')
        self.tree.pack(fill='both', expand=True)

    def __set_menubar(self):
        self.menubar = Menu(self)
        self.config(menu=self.menubar)
        itens_menu = Menu(self.menubar, tearoff=False)
        itens_menu.add_command(label='Cadastrar Produto', command=lambda: eval('JanelaCadastrarProduto')(self))
        itens_menu.add_command(label='Cadastrar Cliente', command=lambda: eval('JanelaCadastrarCliente')(self))
        itens_menu.add_command(label='Cadastrar Vendedor', command=lambda: eval('JanelaCadastrarVendedor')(self))
        itens_menu.add_command(label='Sair', command=self.destroy)
        self.menubar.add_cascade(label='Opções', menu=itens_menu)



if __name__ == '__main__':
    app = JanelaPrincipal()
    app.mainloop()