import tkinter
from tkinter import messagebox
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
g = 9.8

#el def menu debe e tener la pagina de inicio
#raiz / menu
raiz=tkinter.Tk()
raiz.title("Calculadora de Dinamica (Fisica)") #titulo a la ventana
raiz.iconbitmap("iconoATM.ico")
raiz.geometry("500x200")
raiz.resizable(0,0) #ancho,alto, 0,0 = no se puede cambiar tamaño= Fañse,False
raiz.config(background="#033E72")
#etiqueta bienvenido 1
texto1 = tkinter.Label(raiz, text = "Bienvenido :D", fg="#FFFFFF")
texto1.pack()
texto1.config(bg="#033E72")

def cfloat(numero):
    try:
        result=float(numero)
    except:
        messagebox.showerror("ERROR","INTRODUCE BIEN LOS DATOS")
    return result

#def matematicos/fisicos
#ALONDRA
def calcular_trabajo():
    ECF = float(energia_cinetica_final.get())
    ECI = float(energia_cinetica_inicial.get())

    if ECF >= 0 and ECI >= 0:
        resultado.set(cfloat(ECF)-cfloat(ECI))
        mostrarResultado()

def calcular_energia_potencial_gravitacional():
    Massa1=float(masa1.get())
    alltura=float(altura.get())

    if Massa1 >=0 and alltura >=0:
        resultado.set(cfloat(Massa1)*cfloat(alltura)*g)
        mostrarResultado()

def calcular_fuerza_gravitatoria():
    G = 6.67430e-11  
    Massa1=float(masa1.get())
    Massa2=float(masa2.get())
    distanciaa=float(distancia.get())

    if Massa1 >=0 and Massa2 >=0 and distanciaa>=0:
        resultado.set(((cfloat(Massa1)*cfloat(Massa2))*G)/distanciaa**2)
        mostrarResultado()


def calculo_energia_mecanica():
    EC=float(energia_cinetica_inicial.get())
    EP=float(energia_potencial.get())

    if EC >=0 and EP >=0:
        resultado.set(cfloat(EC)+cfloat(EP))
        mostrarResultado()
   

#KAREN
def tiro_parabólico():
  # Convertir el ángulo de grados a radianes
  AG=float(angulo_grados.get())
  VI = float(velocidad_inicial.get())
  tiempoo =float(tiempo.get())
  anguloo=math.cos(AG)
  # Usar la fórmula Δx = v0 * cos(a) * t para calcular el desplazamiento del objeto
  if tiempoo >=0:
    resultado.set(cfloat(VI)*cfloat(anguloo)*cfloat(tiempoo))
    # Devolver el desplazamiento como resultado
    mostrarResultado()

# Definir una función para calcular el movimiento rectilíneo uniforme variado
def movimiento_variado():
    VelI=float(velocidad_inicial.get())
    Ace=float(aceleracionn.get())
    tiem=float(tiempo.get())
    velf=VelI+(Ace*tiem)

    resultado.set(cfloat(velf))
    mostrarResultado()
  

def movimiento_uniforme():
    velI = float(velocidad_inicial.get())
    tiem = float(tiempo.get())

    if tiem >= 0:
        resultado.set(cfloat(velI)*cfloat(tiem))
        mostrarResultado()

def caída_libre():
  # Usar la fórmula Vo * t + 1/2 * g * t^2 para calcular la distancia recorrida por el objeto
    VelI=float(velocidad_inicial.get())
    tiem=float(tiempo.get())

    if tiem >0:
        distancia = VelI * tiem + 0.5 * g * (tiem ** 2)
        resultado.set(cfloat(distancia))
        mostrarResultado()

#DULCE
def Ecinetica():
    masa=float(masa1.get())
    velo=float(velocidad_inicial.get())

    if masa > 0:
        ener=((masa*(velo*velo))/2)
        resultado.set(cfloat(ener))
        mostrarResultado()

def trabajo():
    fuer=float(furza.get())
    desp=float(desplazamiento.get())

    if fuer >= 0 and desp >=0:
        trab= fuer*desp
        resultado.set(cfloat(trab))
        mostrarResultado()


def ffuerza():
    masa = float(masa1.get())
    ace = float(aceleracionn.get())

    if masa > 0:
        fue=masa*ace
        resultado.set(cfloat(fue))
        mostrarResultado()


def aceleracion():
    velf=float(velocidad_final.get())
    veli=float(velocidad_inicial.get())
    tie=float(tiempo.get())

    if tie >=0:
        ace=(velf-veli)/tie
        resultado.set(cfloat(ace))
        mostrarResultado()


def mostrarResultado():
    messagebox.showinfo("RESULTADO",f"El resultado de la operacion es: {resultado.get()}")

energia_cinetica_inicial=tkinter.StringVar()
energia_cinetica_final=tkinter.StringVar()
resultado = tkinter.StringVar()
angulo_grados=tkinter.StringVar()
velocidad_inicial=tkinter.StringVar()
velocidad_final=tkinter.StringVar()
masa1=tkinter.StringVar()
masa2=tkinter.StringVar()
altura=tkinter.StringVar()
distancia=tkinter.StringVar()
energia_potencial=tkinter.StringVar()
tiempo=tkinter.StringVar()
aceleracionn=tkinter.StringVar()
furza=tkinter.StringVar()
desplazamiento=tkinter.StringVar()

#graficadora del tiro parabolico
def graficadora():
    AG = float(angulo_grados.get())
    VI = float(velocidad_inicial.get())

    angulo_radianes = math.radians(AG)

    v0x = VI * math.cos(angulo_radianes)
    v0y = VI * math.sin(angulo_radianes)
    t_max = 2 * v0y / g
    t_intervalo = 0.01
    t = 0  # tiempo inicial
    tiempos = [t]
    posiciones_x = [0]
    posiciones_y = [0]

    while t <= t_max:
        t += t_intervalo
        tiempos.append(t)
        x = v0x * t
        y = v0y * t - 0.5 * g * t ** 2
        posiciones_x.append(x)
        posiciones_y.append(y)

    # Crear una nueva ventana Toplevel
    ventana_grafico = tkinter.Toplevel(raiz)
    ventana_grafico.title("Tiro parabolico")

    # Crear un marco en la nueva ventana
    frame_grafico = ttk.Frame(ventana_grafico)
    frame_grafico.pack()

    # Crear una figura de Matplotlib
    figura = Figure()
    ax = figura.add_subplot(111)
    ax.plot(posiciones_x, posiciones_y)

    # Establecer etiquetas de ejes
    ax.set_xlabel('Posición en el eje X')
    ax.set_ylabel('Posición en el eje Y')

    # Crear un widget de lienzo para mostrar la figura
    canvas = FigureCanvasTkAgg(figura, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack()




def inicioCalc():
    ventanaCal=tkinter.Toplevel()
    ventanaCal.title("Calculadora de funciones")
    ventanaCal.config(bg = "#033E72")
    ventanaCal.geometry("800x700")
    #etiqueta de las fucniones
    etiqueta = tkinter.Label(ventanaCal, text="Esta es la seccion de funciones",fg="#FFFFFF")
    etiqueta.pack()
    etiqueta.config(bg="#033E72")

    #coso meter valoroes 
    EngCinL=tkinter.Label(ventanaCal, text="Energia cinetica inicial (o la unica que tengas):",fg="black",font=("Arial", 10,"bold"))
    EngCinL.pack()
    EngCinL.place(x=50, y=30)
    EngCinE=tkinter.Entry(ventanaCal,textvariable=energia_cinetica_inicial)
    EngCinE.pack()
    EngCinE.place(x=50, y=50)

    EngCinFL=tkinter.Label(ventanaCal, text="Energia cinetica final:",fg="black",font=("Arial", 10,"bold"))
    EngCinFL.pack()
    EngCinFL.place(x=50, y=70)
    EngCinFE=tkinter.Entry(ventanaCal,textvariable=energia_cinetica_final,justify="left")
    EngCinFE.pack()
    EngCinFE.place(x=50, y=90)

    EngPotL=tkinter.Label(ventanaCal, text="Energia potencial:",fg="black",font=("Arial", 10,"bold"))
    EngPotL.pack()
    EngPotL.place(x=50, y=110)
    EngPotE=tkinter.Entry(ventanaCal,textvariable=energia_potencial,justify="left")
    EngPotE.pack()
    EngPotE.place(x=50, y=130)

    Masa1L=tkinter.Label(ventanaCal, text="Masa 1 (kg):",fg="black",font=("Arial", 10,"bold"))
    Masa1L.pack()
    Masa1L.place(x=50, y=150)
    Masa1E=tkinter.Entry(ventanaCal,textvariable=masa1,justify="left")
    Masa1E.pack()
    Masa1E.place(x=50, y=170)

    Masa2L=tkinter.Label(ventanaCal, text="Masa 2 (kg):",fg="black",font=("Arial", 10,"bold"))
    Masa2L.pack()
    Masa2L.place(x=50, y=190)
    Masa2E=tkinter.Entry(ventanaCal,textvariable=masa2,justify="left")
    Masa2E.pack()
    Masa2E.place(x=50, y=210)

    AltL=tkinter.Label(ventanaCal, text="Altura (m):",fg="black",font=("Arial", 10,"bold"))
    AltL.pack()
    AltL.place(x=50, y=230)
    AltE=tkinter.Entry(ventanaCal,textvariable=altura,justify="left")
    AltE.pack()
    AltE.place(x=50, y=250)

    DisL=tkinter.Label(ventanaCal, text="distancia (m):",fg="black",font=("Arial", 10,"bold"))
    DisL.pack()
    DisL.place(x=50, y=270)
    DisE=tkinter.Entry(ventanaCal,textvariable=distancia,justify="left")
    DisE.place()
    DisE.place(x=50,y=290)

    VIL=tkinter.Label(ventanaCal, text="Velocidad inicial(m/s):",fg="black",font=("Arial", 10,"bold"))
    VIL.pack()
    VIL.place(x=50,y=310)
    VIE=tkinter.Entry(ventanaCal,textvariable=velocidad_inicial,justify="left")
    VIE.pack()
    VIE.place(x=50, y=330)

    VFL=tkinter.Label(ventanaCal, text="Velocidad final(m/s):",fg="black",font=("Arial", 10,"bold"))
    VFL.pack()
    VFL.place(x=50,y=350)
    VFE=tkinter.Entry(ventanaCal,textvariable=velocidad_final,justify="left")
    VFE.pack()
    VFE.place(x=50, y=370)
    
    AngL=tkinter.Label(ventanaCal, text="Angulo (en grados):",fg="black",font=("Arial", 10,"bold"))
    AngL.pack()
    AngL.place(x=50,y=390)
    AngE=tkinter.Entry(ventanaCal,textvariable=angulo_grados,justify="left")
    AngE.pack()
    AngE.place(x=50,y=410)

    TieL=tkinter.Label(ventanaCal, text="Tiempo:",fg="black",font=("Arial", 10,"bold"))
    TieL.pack()
    TieL.place(x=50, y=430)
    TieE=tkinter.Entry(ventanaCal,textvariable=tiempo,justify="left")
    TieE.pack()
    TieE.place(x=50,y=450)

    AcelL=tkinter.Label(ventanaCal, text="Aceleracion(m/s^2):",fg="black",font=("Arial", 10,"bold"))
    AcelL.pack()
    AcelL.place(x=50, y=470)
    AcelE=tkinter.Entry(ventanaCal,textvariable=aceleracionn,justify="left")
    AcelE.pack()
    AcelE.place(x=50,y=490)

    BotonFuerL=tkinter.Label(ventanaCal, text="Fuerza:",fg="black",font=("Arial", 10,"bold"))
    BotonFuerL.pack()
    BotonFuerL.place(x=50, y=510)
    BotonFuerE=tkinter.Entry(ventanaCal,textvariable=furza,justify="left")
    BotonFuerE.pack()
    BotonFuerE.place(x=50,y=530)

    BotonDesL=tkinter.Label(ventanaCal, text="Desplazamiento:",fg="black",font=("Arial", 10,"bold"))
    BotonDesL.pack()
    BotonDesL.place(x=50, y=550)
    BotonDesE=tkinter.Entry(ventanaCal,textvariable=desplazamiento,justify="left")
    BotonDesE.pack()
    BotonDesE.place(x=50,y=570)


    #botones de ventana calculadora
    BotonTrabajo= tkinter.Button(ventanaCal, text = "Trabajo (Energia Cinetica)", command = calcular_trabajo)
    BotonTrabajo.pack()
    BotonTrabajo.place()

    BotonEPGravitatoria= tkinter.Button(ventanaCal, text = "Energia Potencial Gravitatoria", command = calcular_energia_potencial_gravitacional)
    BotonEPGravitatoria.pack()
    BotonEPGravitatoria.place()

    BotonEGravitatoria= tkinter.Button(ventanaCal, text = "Fuerza Gravitatoria", command = calcular_fuerza_gravitatoria)
    BotonEGravitatoria.pack()
    BotonEGravitatoria.place()

    BotonEMecanica= tkinter.Button(ventanaCal, text = "Energia Mecanica", command = calculo_energia_mecanica)
    BotonEMecanica.pack()
    BotonEMecanica.place()

    BotonTP= tkinter.Button(ventanaCal, text = "Tiro Parabolico(desplazamiento)", command = tiro_parabólico)
    BotonTP.pack()
    BotonTP.place()

    BotonMRUV= tkinter.Button(ventanaCal, text = "Movimiento rectilíneo uniforme variado(Vf)", command = movimiento_variado)
    BotonMRUV.pack()
    BotonMRUV.place()

    BotonMRU= tkinter.Button(ventanaCal, text = "MRU (distancia)", command = movimiento_uniforme)
    BotonMRU.pack()
    BotonMRU.place()
    
    BotonCL= tkinter.Button(ventanaCal, text = "Caida libre (distancia)", command = caída_libre)
    BotonCL.pack()
    BotonCL.place()

    BotonEC= tkinter.Button(ventanaCal, text = "Energia cinetica", command = Ecinetica)
    BotonEC.pack()
    BotonEC.place()

    TBoron= tkinter.Button(ventanaCal, text = "Trabajo (con fuerza y desplazamiento)", command = trabajo)
    TBoron.pack()
    TBoron.place()

    BotonF= tkinter.Button(ventanaCal, text = "Fuerza", command = ffuerza)
    BotonF.pack()
    BotonF.place()

    BotonF= tkinter.Button(ventanaCal, text = "Aceleracion", command = aceleracion)
    BotonF.pack()
    BotonF.place()

    return energia_cinetica_inicial, energia_cinetica_final


def VentanaGraficadora():
    ventanaGraf=tkinter.Toplevel()
    ventanaGraf.title("Calculadora de funciones")
    ventanaGraf.config(bg = "#033E72")
    ventanaGraf.geometry("500x400")
    #etiqueta de las fucniones
    etiqueta = tkinter.Label(ventanaGraf, text="Esta es la seccion de grafica de tiro parabolico",fg="#FFFFFF")
    etiqueta.pack()
    etiqueta.config(bg="#033E72")


    tkinter.Label(ventanaGraf, text="Angulo:",fg="black",font=("Arial", 10,"bold")).pack()
    tkinter.Entry(ventanaGraf,textvariable=angulo_grados,justify="center").pack()

    tkinter.Label(ventanaGraf, text="Velocidad inicial:",fg="black",font=("Arial", 10,"bold")).pack()
    tkinter.Entry(ventanaGraf,textvariable=velocidad_inicial,justify="center").pack()


    BotonGraficadora= tkinter.Button(ventanaGraf, text = "Graficar", command = graficadora)
    BotonGraficadora.pack()
    BotonGraficadora.place()

def ventanaQuizz():
    class QuizApp(tkinter.Toplevel):
        def __init__(self):
            super().__init__()

            self.preguntas = [
            {"pregunta": "¿En que unidad se mide la energia mecanica?",
             "opciones": ["Kilogramos", "Newton", "Joules", "Litros"],
             "respuesta": "Joules"},
            {"pregunta": "¿Cuál es la fórmula de fuerza?",
             "opciones": ["f*d", "f*g", "m*a", "s*1"],
             "respuesta": "m*a"},
            {"pregunta": "Una moto tiene una masa de 100kg y una aceleracion de 3 m/s^2 ¿Cuál es su fuerza?",
             "opciones": ["285N", "150N", "300N", "213N"],
             "respuesta": "300N"},
            {"pregunta": "¿Cual es la energia que esta almacenada en un objeto debido a su posición.?",
             "opciones": ["Potencial", "Cinetica", "Mecanica", "Calorica"],
             "respuesta": "Potencial"},
            {"pregunta": "Es la capacidad física para realizar un trabajo o un movimiento",
             "opciones": ["Masa", "Fuerza", "Aceleración", "Ganas"],
             "respuesta": "Fuerza"}]
            
            self.puntos = 0
            self.pregunta_actual = 0

            self.label_pregunta = tkinter.Label(self, text="")
            self.label_pregunta.pack()

            self.botones_opciones = []
            for i in range(4):
                boton = tkinter.Button(self, text="", command=lambda i=i: self.verificar_respuesta(i))
                self.botones_opciones.append(boton)
                boton.pack()

            self.actualizar_pregunta()

        def actualizar_pregunta(self):
            if self.pregunta_actual < len(self.preguntas):
                pregunta = self.preguntas[self.pregunta_actual]["pregunta"]
                opciones = self.preguntas[self.pregunta_actual]["opciones"]
                self.respuesta_correcta = self.preguntas[self.pregunta_actual]["respuesta"]

                self.label_pregunta.config(text=pregunta)

                for i, opcion in enumerate(opciones):
                    self.botones_opciones[i].config(text=opcion)

        def verificar_respuesta(self, indice):
            respuesta_elegida = self.botones_opciones[indice]["text"]
            if respuesta_elegida == self.respuesta_correcta:
                self.puntos += 1

            self.pregunta_actual += 1
            self.actualizar_pregunta()

            if self.pregunta_actual == len(self.preguntas):
                messagebox.showinfo("Fin del quiz", f"Puntos obtenidos: {self.puntos}")

    if __name__ == "__main__":
        app = QuizApp()
        app.mainloop()



#boton para ir a la ventana calculadora-graficadora-quizzes
BotonCalculadora= tkinter.Button(raiz, text = "Calculadora", command = inicioCalc)
BotonCalculadora.pack()
BotonCalculadora.place()

BotonCalculadora= tkinter.Button(raiz, text = "Graficadora", command = VentanaGraficadora)
BotonCalculadora.pack()
BotonCalculadora.place()

BotonCalculadora= tkinter.Button(raiz, text = "Quizz", command = ventanaQuizz)
BotonCalculadora.pack()
BotonCalculadora.place()

# Contenedor para el gráfico
frame_grafico = tkinter.Frame(raiz)
frame_grafico.pack()

raiz.mainloop() # la interfaz que debe quedarse esperando a que el usuario haga algo
