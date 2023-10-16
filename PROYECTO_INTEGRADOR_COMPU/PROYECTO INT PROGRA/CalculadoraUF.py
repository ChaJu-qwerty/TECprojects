import tkinter
#el def menu debe e tener la pagina de inicio
#def menu():

#raiz / menu
raiz=tkinter.Tk()
raiz.title("Calculadora de Dinamica (Fisica)") #titulo a la ventana
raiz.iconbitmap("iconoATM.ico")
raiz.geometry("500x600")
raiz.resizable(0,0) #ancho,alto, 0,0 = no se puede cambiar tamaño= Fañse,False
raiz.config(background="#033E72")
#etiqueta bienvenido 1
texto1 = tkinter.Label(raiz, text = "Bienvenido :D", fg="#FFFFFF")
texto1.pack()
texto1.config(bg="#033E72")


#Frame

#funcioes funcionalidad
def acabartodo ():
    raiz.destroy()

def inicioCalc():
    ventanaCal=tkinter.Toplevel()
    ventanaCal.title("Calculadora de funciones")
    ventanaCal.config(bg = "#033E72")
    ventanaCal.geometry("500x600")
    #etiqueta de las fucniones
    etiqueta = tkinter.Label(ventanaCal, text="Esta es la seccion de funciones",fg="#FFFFFF")
    etiqueta.pack()
    etiqueta.config(bg="#033E72")
    
    
    
#botones1
BotonCalculadora= tkinter.Button(raiz, text = "Calculadora", command = inicioCalc)
BotonCalculadora.pack()
BotonCalculadora.place()


raiz.mainloop() # la interfaz que debe quedarse esperando a que el usuario haga algo
