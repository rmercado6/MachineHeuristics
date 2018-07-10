import csv
import time
import random as rand
from threading import Condition, Thread, Event
import plotly as py
import plotly.graph_objs as go
from InputData import data_input


beneficios = []
maquinas = []
productos = []
traces = []

datainput = data_input()
data = datainput[0]
condicionesLst = datainput[1]
productosLst = datainput[2]
maquinasLst = datainput[3]


# # -----LECTURA DE INFORACION DE ARCHIVO CSV-----
# try:
#     with open('maquinas.csv', 'r') as archivo:
#         lineas = csv.reader(archivo, delimiter=' ', quotechar='|')
#         for row in lineas:
#             rawstr = ', '.join(row)
#             raw = rawstr.split(",")
#             data.append(raw)
#     # data.pop(0)
# except IOError:
#     print("Error al cargar el archivo maquinas.csv")
# # --acomodo de información--
# for i in range(len(data)):
#     if i <= len(data):
#         if data[i][0] == 'cond':
#             condicionesLst.append(data[i])
#         elif data[i][0] == 'producto':
#             productosLst.append(data[i])
#         elif data[i][0] == 'maquina':
#             maquinasLst.append(data[i])
# # -----FIN DE LECTURA DE ARCHIVO-----


# -----DEFINICION DE CLASES-----
class tipoProducto:

    def __init__(self, Nombre, Maquinas, Beneficio):
        self.nombre = Nombre
        self.maquinas = Maquinas
        self.beneficio = Beneficio
        self.tiempoTotal = 0
        self.color = [
            rand.randint(20, 230),
            rand.randint(20, 230),
            rand.randint(20, 230)
        ]

        for NombreMaquina in self.maquinas:
            for Maquina in maquinas:
                if Maquina.nombre == NombreMaquina:
                    for proceso in Maquina.procesos:
                        self.tiempoTotal += proceso.tiempo

        try:
            self.bt = Beneficio / self.tiempoTotal
        except ZeroDivisionError:
            self.bt = 0

    def toString(self):
        string = "\nProducto: " + self.nombre + "\n Maquinas: "
        for maquina in self.maquinas:
            string += maquina + " "
        string += "\n Beneficio: " + str(self.beneficio) + "\n Tiempo total: " + str(self.tiempoTotal) + \
                  "\n Beneficio/Tiempo: " + str(self.bt)

        return(string)


class maquina:

    def __init__(self, nombre, procesos):
        self.nombre = nombre
        self.procesos = procesos

    def toString(self):
        string = "\nMáquina: " + self.nombre
        for proceso in self.procesos:
            string += proceso.toString()
        return(string)


class proceso:

    def __init__(self, nombre, dependencia, maquina):
        self.nombre = nombre
        self.maquina = maquina
        self.dependencia = dependencia
        self.tiempo = rand.randint(2, 5)

    def toString(self):
        return("\n Proceso " + str(self.nombre) +
               "\n   Maquina: " + str(self.maquina) +
               "\n   Dependencia: " + str(self.dependencia) +
               "\n   tiempo: " + str(self.tiempo))


class producto:

    def __init__(self, indice, tipo, color):
        self.indice = indice
        self.tipo = tipo
        self.progreso = 0
        self.color = color

    def toString(self):
        return("Producto: " + str(self.tipo) + "-" + str(self.indice) )


class condicion:

    def __init__(self, nombre):
        self.nombre = nombre
        self.condicion = Condition()


class evento:

    def __init__(self, nombre):
        self.nombre = nombre
        self.evento = Event()


# ----FIN DE DEFINICION DE CLASES-----

TiempoTotal = 10 #rand.randint(30, 40)
print('Tiempo total disponible: ' + str(TiempoTotal))

# -----GENERACION DE OBJETOS CON LA INFORMACIÓN CARGADA DEL ARCHIVO-----
procesosTotal = []
for Maquina in maquinasLst:
    procesosLst = []
    procesos = []

    for i in range(len(Maquina)):
        if i > 1 and Maquina[i] != '':
            procesosLst.append([Maquina[i],Maquina[1]])
            procesosTotal.append([Maquina[i],Maquina[1]])
    for prod in range(len(procesosLst)):
        Dependencias = []
        for cond in condicionesLst:
            if procesosLst[prod] == [cond[3],cond[4]]:
                Dependencias.append([cond[1],cond[2]])
        procesos.append(proceso(procesosLst[prod], Dependencias, Maquina[1]))
    maquinas.append(maquina(Maquina[1], procesos))

for Producto in productosLst:
    MaquinasLst = []
    for i in range(len(Producto)):
        if i > 1 and Producto[i] != '':
            MaquinasLst.append(Producto[i])
    productos.append(tipoProducto(Producto[1], MaquinasLst, rand.randint(1, 100)))

for Producto in productos:
    print(Producto.toString())

for maquina in maquinas:
    print(maquina.toString())
# -----FIN DE LA GENEARCION DE OBJETOS CARGADOS DESDE ARCHIVO CSV-----


condiciones = []
eventos = []
for proceso in procesosTotal:
    condiciones.append(condicion(proceso))
    eventos.append(evento(proceso))

for evento in eventos:
    evento.evento.set()

condicionesMaquina = []
for maquina in maquinas:
    condicionesMaquina.append(condicion(maquina.nombre))

condicionesProducto = []
for Producto in productos:
    condicionesProducto.append(condicion(Producto.nombre))

ProductosBeneficio = sorted(productos, key=lambda producto: producto.bt, reverse=True)

almacen = []
indice = 0
fabricacion =[]
fabCond = []
for i in range(len(productos)):
    fabricacion.append([])
    fabCond.append(Condition())

productos = []

def HiloProducto(pro):

    y = []
    xinit = []
    xfin = []
    xelapsed = []
    x = []
    indice = 0
    while (time.time() - tiempo_de_inicio) < TiempoTotal:
        HilosManufactura = []
        HilosManufactura.append(Thread(name=(pro.nombre + str(indice)), target=HiloManufactura, args=[pro, indice]))
        y.append(pro.nombre + str(indice))
        xinit.append(time.time())
        xelapsed.append(xinit[-1] - tiempo_de_inicio)
        HilosManufactura[-1].start()
        HilosManufactura[-1].join()
        xfin.append(time.time())
        x.append(xfin[-1] - xinit[-1])
        indice += 1
    color = 'rgba(' + \
            str(pro.color[0]) + ', ' + \
            str(pro.color[1]) + ', ' + \
            str(pro.color[2]) + ', 0.8)'
    elapsed_trace = go.Bar(
        y=y,
        x=xelapsed,
        orientation='h',
        marker=dict(
            color='rgba(1, 1, 1, 0.04)',
            line=dict(
                color='rgba(1, 1, 1, 0.0)',
                width=3)
        ),
        showlegend=False
    )
    trace = go.Bar(
        y=y,
        x=x,
        name=pro.nombre + " execution time",
        orientation='h',
        marker=dict(
            color=color,
            line=dict(
                color='rgba(1, 1, 1, 0.0)',
                width=3)
        )
    )
    traces.append(elapsed_trace)
    traces.append(trace)

def HiloManufactura(pro, indice):

    y = []
    xinit = []
    xfin = []
    xelapsed = []
    x = []
    if ((time.time() - tiempo_de_inicio) < TiempoTotal):
        HilosMaquina = []
        for maq in pro.maquinas:
            for maquina in maquinas:
                if maquina.nombre == maq:
                    HilosMaquina.append(Thread(name=(pro.nombre + maq), target=HiloMaquina, args=[maquina,pro.color, indice, pro.nombre]))
                    y.append(pro.nombre + str(indice) + ' - ' + maq )
                    xinit.append(time.time())
                    xelapsed.append(xinit[-1] - tiempo_de_inicio)
                    HilosMaquina[-1].start()
                    HilosMaquina[-1].join()
                    xfin.append(time.time())
                    x.append(xfin[-1] - xinit[-1])

        color = 'rgba(' + \
                str(pro.color[0]) + ', ' + \
                str(pro.color[1]) + ', ' + \
                str(pro.color[2]) + ', 0.6)'
        elapsed_trace = go.Bar(
            y=y,
            x=xelapsed,
            orientation='h',
            marker=dict(
                color='rgba(1, 1, 1, 0.04)',
                line=dict(
                    color='rgba(1, 1, 1, 0.0)',
                    width=3)
            ),
            showlegend=False
        )
        trace = go.Bar(
            y=y,
            x=x,
            name= "machine execution time",
            orientation='h',
            marker=dict(
                color=color,
                line=dict(
                    color='rgba(1, 1, 1, 0.0)',
                    width=3)
            )
        )
        traces.append(elapsed_trace)
        traces.append(trace)
        if (time.time() - tiempo_de_inicio) < TiempoTotal:
            productos.append(pro)


def HiloMaquina(maq, color, indice, producto):
    y = []
    xinit = []
    xfin = []
    xelapsed = []
    x = []
    if ((time.time() - tiempo_de_inicio) < TiempoTotal):
        HilosProceso = []

        for pro in maq.procesos:
            for proceso in procesosTotal:
                if proceso == pro.nombre:
                    HilosProceso.append(Thread(name=(str(proceso)), target=HiloProceso, args=[pro]))
                    y.append(producto + str(indice) + ' - ' + maq.nombre + str(pro.nombre))
                    # y.append(str(pro.nombre) + str(indice) + ' - ' + maq.nombre )
                    xinit.append(time.time())
                    xelapsed.append(xinit[-1] - tiempo_de_inicio)
                    HilosProceso[-1].start()
                    HilosProceso[-1].join()
                    xfin.append(time.time())
                    x.append(xfin[-1] - xinit[-1])
        colorg = 'rgba(' + \
                str(color[0]) + ', ' + \
                str(color[1]) + ', ' + \
                str(color[2]) + ', 0.4)'
        elapsed_trace = go.Bar(
            y=y,
            x=xelapsed,
            orientation='h',
            marker=dict(
                color='rgba(1, 1, 1, 0.04)',
                line=dict(
                    color='rgba(1, 1, 1, 0.0)',
                    width=3)
            ),
            showlegend=False
        )
        trace = go.Bar(
            y=y,
            x=x,
            name="process execution time",
            orientation='h',
            marker=dict(
                color=colorg,
                line=dict(
                    color='rgba(1, 1, 1, 0.0)',
                    width=3)
            )
        )
        traces.append(elapsed_trace)
        traces.append(trace)



def HiloProceso(pro):

    if ((time.time() - tiempo_de_inicio) < TiempoTotal):
        if pro.dependencia == []:
            if ((time.time() - tiempo_de_inicio) + pro.tiempo) < TiempoTotal:
                time.sleep(pro.tiempo)
                almacen.append(pro.nombre)
        else:
            d = len(pro.dependencia)
            while d > 0:
                if (time.time() - tiempo_de_inicio) < TiempoTotal:
                    for dep in pro.dependencia:
                        if dep in almacen:
                            for i in range(len(almacen)):
                                if almacen[i] == dep:
                                    try:
                                        almacen.pop(i)
                                        time.sleep(pro.tiempo)
                                        almacen.append(pro.nombre)
                                        d -= 1
                                        if d == 0 or (time.time() - tiempo_de_inicio) > TiempoTotal:
                                            break
                                    except IndexError:
                                        # print('no alcanzo recurso')
                                        d = d
                else:
                    break





Hilos = []
tiempo_de_inicio = time.time()
for Producto in ProductosBeneficio:

    if len(Hilos) > len(productosLst):
        try:
            for Hilo in Hilos:
                Hilo.hilo.join()
        except:
            Hilos.append(producto(indice, Producto.nombre, Producto.color))
            Hilos[-1].hilo = (Thread(name=(str(Producto.nombre)), target=HiloProducto, args=[Producto]))
            Hilos[-1].xinit = time.time()
            Hilos[-1].xelapsed = Hilos[-1].xinit - tiempo_de_inicio
            Hilos[-1].hilo.start()
    else:
        Hilos.append(producto(indice, Producto.nombre, Producto.color))
        Hilos[-1].hilo = (Thread(name=(str(Producto.nombre)), target=HiloProducto, args=[Producto]))
        Hilos[-1].xinit = time.time()
        Hilos[-1].xelapsed = Hilos[-1].xinit - tiempo_de_inicio
        Hilos[-1].hilo.start()

for Hilo in Hilos:
    Hilo.hilo.join()
    Hilo.xfin = time.time()
    Hilo.x = Hilo.xfin - Hilo.xinit
    color = 'rgba(' + \
            str(Hilo.color[0]) + ', ' + \
            str(Hilo.color[1]) + ', ' + \
            str(Hilo.color[2]) + ', 1.0)'
    elapsed_trace = go.Bar(
        y=[Hilo.tipo],
        x=[Hilo.xelapsed],
        orientation='h',
        marker=dict(
            color='rgba(1, 1, 1, 0.04)',
            line=dict(
                color='rgba(1, 1, 1, 0.0)',
                width=3)
        ),
        showlegend=False
    )
    trace = go.Bar(
        y=[Hilo.tipo],
        x=[Hilo.x],
        name=Hilo.tipo + " execution time",
        orientation='h',
        marker=dict(
            color=color,
            line=dict(
                color='rgba(1, 1, 1, 0.0)',
                width=3)
        )

    )
    traces.append(elapsed_trace)
    traces.append(trace)

prod = []
beneficio = 0
for i in range(len(ProductosBeneficio)):
    prod.append(0)
    for producto in productos:
        if producto.nombre == ProductosBeneficio[i].nombre:
            prod[i] += 1
    beneficio += ProductosBeneficio[i].beneficio * prod[i]
    print(ProductosBeneficio[i].nombre + ": " + str(prod[i]) + " || Beneficio: " +
                                                    str(ProductosBeneficio[i].beneficio * prod[i]))
print("Beneficio total: " + str(beneficio))



layout = go.Layout(
    barmode='stack',
    title='Diagrama de Tiempos de Producción'
)

fig = go.Figure(data=traces, layout=layout)
py.offline.plot(fig, filename='maquinasGantt.html')

