from _typeshed import Self
from tkinter import *
from tkinter import ttk

class Principal():
    principal = Tk()

    #Titulo de la barra titulo de la ventana.
    principal.title("SOFTWARE PARA EL DISEÑO DE TRANSMISIONES MECANICAS POR CADENAS DE RODILLOS")

    #intruccion para solicitar al sistema la resolucion de la pantalla tanto en alto como en ancho.
    w, h = principal.winfo_screenwidth(), principal.winfo_screenheight()

    #pasa al atrubuto geometri la resolucion de la pantalla solicitada al sistema en ancho y alto.
    principal.geometry("%dx%d+0+0" % (w, h))

    principalFrame = Frame(principal)
    principalFrame.pack(fill=BOTH, expand=1)



    principal.mainloop()