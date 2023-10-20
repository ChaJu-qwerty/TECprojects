import tkinter
from tkinter import messagebox
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
g = 9.8

#el def menu debe e tener la pagina de inicio
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

def cfloat(numero):
    try:
        result=float(numero)
    except:
        messagebox.showerror("ERROR","INTRODUCE BIEN LOS DATOS")
    return result

#def matematicos/fisicos
#ALONDRA
def calcular_trabajo():
    ECF = int(energia_cinetica_final.get())
    ECI = int(energia_cinetica_inicial.get())

    if ECF >= 0 and ECI >= 0:
        resultado.set(cfloat(ECF)-cfloat(ECI))
        mostrarResultado()

def calcular_energia_potencial_gravitacional(masa, altura, gravedad=9.81):
    return masa * gravedad * altura

def calcular_fuerza_gravitatoria(masa1, masa2, distancia):
    G = 6.67430e-11  
    fuerza_gravitatoria = (G * masa1 * masa2) / distancia**2
    return fuerza_gravitatoria

def calculo_energia_mecanica(energia_cinetica, energia_potencial):
    return energia_cinetica + energia_potencial

#KAREN
def tiro_parabólico(velocidad_inicial, angulo, tiempo):
  # Convertir el ángulo de grados a radianes
  angulo = math.radians(angulo)
  # Usar la fórmula Δx = v0 * cos(a) * t para calcular el desplazamiento del objeto
  desplazamiento = velocidad_inicial * math.cos(angulo) * tiempo
  # Devolver el desplazamiento como resultado
  return desplazamiento

# Definir una función para calcular el movimiento rectilíneo uniforme variado
def movimiento_variado(velocidad_inicial, aceleración, tiempo):
  # Usar la fórmula v = v0 + a * t para calcular la velocidad final
  velocidad_final = velocidad_inicial + aceleración * tiempo
  # Devolver la velocidad final como resultado
  return velocidad_final

def movimiento_uniforme(velocidad, tiempo):
  # Usar la fórmula d = v * t para calcular la distancia recorrida
  distancia = velocidad * tiempo
  # Devolver la distancia como resultado
  return distancia

def caída_libre(Vo, t):
  # Usar la fórmula Vo * t + 1/2 * g * t^2 para calcular la distancia recorrida por el objeto
  distancia = Vo * t + 0.5 * g * t ** 2
  # Devolver la distancia como resultado
  return distancia

#DULCE
def Ecinetica(masa, velocidad):
    return ((masa*(velocidad*velocidad))/2)

def trabajo(fuerza, desplazamiento):
    return fuerza*desplazamiento

def ffuerza(masa, aceleracion):
    return masa*aceleracion

def aceleracion(Vf, Vi, t):
    return ((Vf-Vi)/t)

def mostrarResultado():
    messagebox.showinfo("RESULTADO",f"El resultado de la operacion es: {resultado.get()}")

energia_cinetica_inicial=tkinter.StringVar()
energia_cinetica_final=tkinter.StringVar()
resultado = tkinter.StringVar()
angulo_grados=tkinter.StringVar()
velocidad_inicial=tkinter.StringVar()


def graficadora():
    AG=int(angulo_grados.get())
    VI = int(velocidad_inicial.get())

    angulo_radianes = math.radians(AG)

    v0x = VI * math.cos(angulo_radianes)
    v0y = VI * math.sin(angulo_radianes)
    t_max = 2 * v0y / g
    t_intervalo = 0.01
    t = 0 #tiempo inicial
    tiempos = [t]
    posiciones_x = [0]
    posiciones_y = [0]

    # Calculamos las posiciones en cada instante de tiempo
    while t <= t_max:
        t += t_intervalo
        tiempos.append(t)
        x = v0x * t
        y = v0y * t - 0.5 * g * t**2
        posiciones_x.append(x)
        posiciones_y.append(y)
    
    # Crear una figura de Matplotlib
    figura = Figure()
    ax = figura.add_subplot(111)
    ax.plot(posiciones_x, posiciones_y)

    # Limpiar el contenedor del gráfico
    for widget in frame_grafico.winfo_children():
        widget.destroy()

    # Crear un widget de lienzo para mostrar la figura
    canvas = FigureCanvasTkAgg(figura, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack()




def inicioCalc():
    ventanaCal=tkinter.Toplevel()
    ventanaCal.title("Calculadora de funciones")
    ventanaCal.config(bg = "#033E72")
    ventanaCal.geometry("500x600")
    #etiqueta de las fucniones
    etiqueta = tkinter.Label(ventanaCal, text="Esta es la seccion de funciones",fg="#FFFFFF")
    etiqueta.pack()
    etiqueta.config(bg="#033E72")

    #coso meter valroes 
    tkinter.Label(ventanaCal, text="Energia cinetica inicial:",fg="black",font=("Arial", 10,"bold")).pack()
    tkinter.Entry(ventanaCal,textvariable=energia_cinetica_inicial,justify="center").pack()

    tkinter.Label(ventanaCal, text="Energia cinetica final:",fg="black",font=("Arial", 10,"bold")).pack()
    tkinter.Entry(ventanaCal,textvariable=energia_cinetica_final,justify="center").pack()

    #botones de ventana calculadora
    BotonTrabajo= tkinter.Button(ventanaCal, text = "Trabajo", command = calcular_trabajo)
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

    return energia_cinetica_inicial, energia_cinetica_final


def Ventanagraficadora():
    ventanaGraf=tkinter.Toplevel()
    ventanaGraf.title("Calculadora de funciones")
    ventanaGraf.config(bg = "#033E72")
    ventanaGraf.geometry("500x600")
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

    


#boton para ir a la ventana calculadora-graficadora-quizzes
BotonCalculadora= tkinter.Button(raiz, text = "Calculadora", command = inicioCalc)
BotonCalculadora.pack()
BotonCalculadora.place()

BotonCalculadora= tkinter.Button(raiz, text = "Graficadora", command = Ventanagraficadora)
BotonCalculadora.pack()
BotonCalculadora.place()

# Contenedor para el gráfico
frame_grafico = tkinter.Frame(raiz)
frame_grafico.pack()

raiz.mainloop() # la interfaz que debe quedarse esperando a que el usuario haga algo
