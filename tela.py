from tkinter import *
from tkinter import ttk
from tkinter.filedialog import  askopenfilename, asksaveasfilename
import geradorJava, geradorPython, geradorR
from PIL import ImageTk, Image
from tkinter import messagebox
import shutil
import gabaritos
import codigo
import classes
import modelos


class PaginaPrincipal:

    def __init__(self, root):
        root.title("Ambiente de Simulação Distribuída Automático - ASDA")
        

        self.mainframe = ttk.Frame(root, padding="5")
        self.mainframe.grid(column=0, row=0, columnspan=2, sticky=(N, W, E, S), padx=10, pady=5)
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=9)

        myimg = ImageTk.PhotoImage(Image.open("images/asda.png"))
        testeImg = ttk.Label(self.mainframe, image=myimg)
        testeImg.image = myimg

        testeImg.grid(column=0, row=0, sticky=W)

        ttk.Label(self.mainframe, wraplength=370, font=("Arial", 14), padding=(5, 10, 1, 30), justify='center', text="O Ambiente de Simulação Distribuída Automático - ASDA "  
        + " foi criado com intuito de tornar a simulação de sistemas acessivel a vários publicos "
        + " de diversos níveis de conhecimento. Para iniciar sua simulação, selecione o modelo do sistema"
        + " no campo abaixo e click no botão da linguagem que deseja gerar seu código!").grid(column=0, row=1, sticky=E, padx=1)

       # self.quadro1 = ttk.Frame(root, padding=(5, 20,))
       # self.quadro1.grid(column=0, row=2, sticky=(N, W, E, S), padx=20, pady=0)
       # self.quadro1['borderwidth'] = 1
       # self.quadro1['relief'] = 'groove'

        self.modelo = ''
        self.modelo_entrada = Entry(self.mainframe, width=40, font=("Arial", 12), state="disabled")
        self.modelo_entrada.grid(column=0, row=2, sticky=(W, E))
        self.modelo_entrada.config(highlightbackground='#88C542', highlightthickness = 3)

        Button(self.mainframe, text="Selecionar", font=("Arial", 13, 'bold'), command=self.buscar, highlightbackground='#30499B', highlightthickness = 3).grid(column=0, row=3, sticky=(W, E))

        self.quadro2 = ttk.Frame(root, padding=(30,5))
        self.quadro2.grid(column=2, row=0, rowspan=4, sticky=(W), padx=0, pady=10)
        #self.quadro2['borderwidth'] = 1
        #self.quadro2['relief'] = 'groove'
       
        Button(self.quadro2, text="Python", width=9, height = 4, font=("Arial", 16, 'bold'), command=self.gerarPython, highlightbackground='#88C542', highlightthickness = 4).grid(column=0, row=0, sticky=(N, W, E, S), padx=1, pady=10) 
        Button(self.quadro2, text="Java", width=9, height = 4, font=("Arial", 16, 'bold'), command=self.gerarJava, highlightbackground='#30499B', highlightthickness = 4).grid(column=0, row=2, sticky=(N, W, E, S), padx=1, pady=10)
        Button(self.quadro2, text="R", width=9, height = 4, font=("Arial", 16, 'bold'), command=self.gerarR, highlightbackground='#88C542', highlightthickness = 4).grid(column=0, row=4, sticky=(N, W, E, S), padx=1, pady=10)        

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=10, pady=5)

        #for child in self.quadro1.winfo_children(): 
        #    child.grid_configure(padx=5, pady=6)    

    def buscar(self):
        self.modelo = askopenfilename(title="Escolha um arquivo", filetypes=(('.dot files', '*.gv'), ('.dot files', '*.dot')))
        # self.modelo.
        self.modelo_entrada['state'] = 'normal'
        self.modelo_entrada.insert(0, self.modelo)
        self.modelo_entrada['state'] = 'disabled'

    def gerarPython(self):

        if self.modelo == '':
            messagebox.showwarning ( message="Selecione um Modelo para continuar!", icon='warning', title='Aviso')

        else:
            py = geradorPython.GeradorPython(self.modelo)
            py.principal()
            name = py.nome()
            self.show(name) 

            
    
    def gerarJava(self):

        if self.modelo == '':
            messagebox.showwarning ( message="Selecione um Modelo para continuar!", icon='warning', title='Aviso')
        else:
            java = geradorJava.GeradorJava(self.modelo)
            java.principal()
            name = java.nome()
            self.show1(name)
    
    def gerarR(self):

        if self.modelo == '':
             messagebox.showwarning ( message="Selecione um Modelo para continuar!", icon='warning', title='Aviso')
        else:
            r = geradorR.GeradorR(self.modelo)
            r.principal()
            name = r.nome()
            self.show(name) 
        
    
    def show(self, name):
        self.info = Tk()
        # self.info.geometry("100x100")
        self.info.title('Visualizar Código')
        frame1= ttk.Frame(self.info, padding="5")
        frame1.grid(column=0, row=0, sticky=(N, W, E, S))
        self.info.columnconfigure(0, weight=1)
        self.info.rowconfigure(0, weight=1)
        ttk.Label(frame1, justify='center', font=("Arial", 13), text="Código gerado com sucesso!").grid(column=0, row=0, padx=5, pady=5)  
       # frame2 = ttk.Frame(self.info, padding="5")
       # frame2.grid(column=0, row=1, sticky=(N, W, E, S))
        #ttk.Button(frame2, text="Ler", command=self.read).grid(column=0, row=1, padx=5, pady=5)
        # ttk.Button(frame2, text="Editar", command=self.update).grid(column=1, row=1, padx=5, pady=5)
        Button(frame1, text="Salvar Código", command=lambda:self.save(name), highlightbackground='#88C542', highlightthickness = 2).grid(column=0, row=1, padx=5, pady=5)

    def show1(self, name):
        self.info = Tk()
        # self.info.geometry("100x100")
        self.info.title('Visualizar Código')
        frame1= ttk.Frame(self.info, padding="5")
        frame1.grid(column=0, row=0, sticky=(N, W, E, S))
        self.info.columnconfigure(0, weight=1)
        self.info.rowconfigure(0, weight=1)
        ttk.Label(frame1, justify='center', font=("Arial", 13), text="Código gerado com sucesso!").grid(column=0, row=0, padx=5, pady=5)  
       # frame2 = ttk.Frame(self.info, padding="5")
       # frame2.grid(column=0, row=1, sticky=(N, W, E, S))
        #ttk.Button(frame2, text="Ler", command=self.read).grid(column=0, row=1, padx=5, pady=5)
        # ttk.Button(frame2, text="Editar", command=self.update).grid(column=1, row=1, padx=5, pady=5)
        Button(frame1, text="Salvar Código", command=lambda:self.zipFile(name), highlightbackground='#88C542', highlightthickness = 2).grid(column=0, row=1, padx=5, pady=5)
          
       
    def save(self, name):
        files = [('R Files', '*.R'), 
             ('Python Files', '*.py'),
             ('Java Files', '*.java')]
        c = open('codigo/'+ name, 'r')
        codigo = c.readlines()
        codigoSalvo = asksaveasfilename(initialfile = name, title='Salvar arquivo', filetypes = files, defaultextension = files)
        arquivo = open(codigoSalvo, "w+")
        arquivo.writelines(codigo)
        c.close()
        arquivo.close()

        self.info.destroy()
        messagebox.showinfo( message="Código salvo com sucesso!", icon='info', title='Aviso')

    def zipFile(self, name):
        arquivo = asksaveasfilename(initialfile = name, title='Salvar arquivo')
        print(arquivo)
        shutil.make_archive(arquivo, 'zip', 'codigo/'+ name)
        self.info.destroy()
        messagebox.showinfo( message="Código salvo com sucesso!", icon='info', title='Aviso')
        
    def quit(self):
       self.info.destroy() 


    
root = Tk()
PaginaPrincipal(root)
root.geometry("620x500")
root.minsize(620, 490)
root.maxsize(620, 490)
root.mainloop()
