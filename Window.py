from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import Lib as LogHandler


class Ventana(Frame):

    def __init__(self, interfaz = Tk(), window_zise = "750x550", titulo = "Window App", autor = "Abel Jimenez"):
        self.interfaz = interfaz
        self.interfaz.geometry(window_zise)
        self.interfaz.resizable(False, False) 
        self.interfaz.title(titulo)
        self.titulo = titulo
        self.criteria = StringVar()
        self.resultado = StringVar()
        self.datos = [["Archivo","Nuevo", "Abrir", "Guardar", "Salir"], ["Edit"], ["Herramienta", "Buscar"], ["Ayuda", "Acerca de"]]
        self.IndexList = []
        self.poblar_mb()
        self.autor = autor
        self.msg = "Este es un software desarrollado por Sn0wFreeze!"




    def ayuda(self):
        messagebox.showinfo(self.titulo,"\nAutor: "+self.autor +" \n\n"+self.msg)


    def browseFile(self):
        try:
            file_path = filedialog.askopenfilename()
            self.resultado.set(LogHandler.Open_File(file_path))
        except:
            messagebox.showerror(self.titulo,"Ha ocurrido un error mientras se realiza la lectura del archivo en: " +(file_path))
        self.poblar_w()



    def browseDir(self):
        try:
            
            file_name = filedialog.askdirectory()
            file_name += "/LogParser"

            if  self.ReadedText:

                LogHandler.Write_File(file_name, self.ReadedText.get("1.0",END))
            
            else:

                messagebox.showinfo(self.titulo,"Aun no tienes contenido en realizado!\nDebes crear contenido escrito en la caja de texto.")
                self.poblar_w()

        except:

            messagebox.showerror(self.titulo,"Ha ocurrido un error mientras se realiza la escritura del archivo.")




    def search(self, keyword, tag):

        if keyword and tag:

            self.ReadedText.tag_delete(tag)
            idx = '1.0'

            while True:

                try:

                    idx = self.ReadedText.search(r''+keyword, idx, nocase=1, stopindex=END, regexp = True) 
                
                except:

                    messagebox.showerror(self.titulo, "Error Grave en el search Engine. Valor del Index: " + idx)

                if not idx:
                    break

                LastIdx = '%s+%dc'%(idx, len(keyword))

                self.IndexList.append(LastIdx)
                
                self.ReadedText.tag_add(tag, idx, LastIdx)
                
                idx = LastIdx



    def buscar(self):

        try:
            
            self.index = 0
            self.search(keyword=self.criteria.get(), tag="success")
            self.ReadedText.tag_config('success', background='yellow', foreground='red')

            Button(self.interfaz, text = "↓↑", command=self.ocurrencias).place(x=280, y=25)
            Button(self.interfaz, text = "clear", command=self.clear).place(x=310, y=25)
            self.ReadedText.see(self.IndexList[0])

        except TypeError:

            messagebox.showerror(self.titulo,"Ha ocurrido un error mientras se buscaba lo solicitado: Error interno.")

        except :

            messagebox.showerror(self.titulo,"Ha ocurrido un error mientras se buscaba lo solicitado: " + self.criteria.get() + ".")



    def ocurrencias(self):


        if self.IndexList:

            try:

                self.ReadedText.see(self.IndexList[self.index])

            except:

                messagebox.showerror(self.titulo,"Index Error, Index: " + str(self.index))

            if self.index != len(self.IndexList)-1 :

                self.index += 1

            else:

                self.index = 0



    def clear(self):
        self.index = 0
        self.IndexList.clear()
        self.ReadedText.delete("1.0",END)
        self.criteria.set("")




    def poblar_w(self):
        Label(self.interfaz, text = "Ingresa un criterio: ").place(x=10, y=10)
        self.LookedText = Entry(self.interfaz, textvariable = self.criteria, font=("arial", 14), fg="white", bg="black").place(x=10, y=25)
        Button(self.interfaz, text = "Buscar", command=self.buscar).place(x=220, y=25)
        Label(self.interfaz, text = "Resultado: ").place(x=10, y=95)
        self.ReadedText = Text(self.interfaz, wrap=WORD, font=("arial", 16), fg="white", bg="black")
        self.ScB=Scrollbar(self.ReadedText, orient='vertical')
        self.ScB.config(command=self.ReadedText.yview)
        self.ScB.pack(side=RIGHT, fill=BOTH)
        self.ReadedText.place(x=10, y=110, width=930, height=430)
        self.ReadedText.config(yscrollcommand = self.ScB.set)
        self.ReadedText.insert(INSERT, self.resultado.get())

        

    def poblar_mb(self):
        menubar = Menu(self.interfaz)
        file_menu = Menu(menubar)
        menubar.add_cascade(label=self.datos[0][0],menu=file_menu)
        file_menu.add_command(label=self.datos[0][1], command=self.poblar_w)
        file_menu.add_command(label=self.datos[0][2], command=self.browseFile)
        file_menu.add_command(label=self.datos[0][3], command=self.browseDir)
        file_menu.add_command(label=self.datos[0][4], command=self.interfaz.destroy)
        edit_menu = Menu(menubar)
        menubar.add_cascade(label=self.datos[1],menu=edit_menu)
        herr_menu = Menu(menubar)
        menubar.add_cascade(label=self.datos[2][0],menu=herr_menu)
        herr_menu.add_command(label=self.datos[2][1], command=self.browseFile)
        ayuda_menu = Menu(menubar)
        menubar.add_cascade(label=self.datos[3][0],menu=ayuda_menu)
        ayuda_menu.add_command(label=self.datos[3][1], command=self.ayuda)
        self.interfaz.configure(menu=menubar)
