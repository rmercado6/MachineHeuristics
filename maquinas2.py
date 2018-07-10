import csv, time
import random as rand
from threading import Condition, Thread, Event, Semaphore

data = []
condicionesLst = []
productosLst = []
maquinasLst = []
beneficios = []
maquinas =[]
productos =[]


#-----LECTURA DE INFORACION DE ARCHIVO CSV-----
try:
    with open('maquinas.csv', 'r') as archivo:
        lineas = csv.reader(archivo, delimiter=' ', quotechar='|')
        for row in lineas:
            rawstr = ', '.join(row)
            raw = rawstr.split(",")
            data.append(raw)
    data.pop(0)
except:
    print()
# --acomodo de información--
for i in range(len(data)):
    if i <= len(data):
        if data[i][0] == 'cond':
            condicionesLst.append(data[i])
        elif data[i][0] == 'producto':
            productosLst.append(data[i])
        elif data[i][0] == 'maquina':
            maquinasLst.append(data[i])
# -----FIN DE LECTURA DE ARCHIVO-----




# print("---")
# for element in condicionesLst:
#     print(element)
# print("---")
# for element in productosLst:
#     print(element)
# print("---")
# for element in maquinasLst:
#     print(element)

# -----DEFINICION DE CLASES-----
class tipoProducto:

    def __init__(self, Nombre, Maquinas, Beneficio):
        self.nombre = Nombre
        self.maquinas = Maquinas
        self.beneficio = Beneficio
        self.tiempoTotal = 0

        for NombreMaquina in self.maquinas:
            for Maquina in maquinas :
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

    def __init__(self, indice, tipo):
        self.indice = indice
        self.tipo = tipo
        self.progreso = 0

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

TiempoTotal = rand.randint(15, 30)
# tiempo_de_inicio = time.time()

# -----GENERACION DE OBJETOS CON LA INFORMACIÓN CARGADA DEL ARCHIVO-----
procesosTotal = []
for Maquina in maquinasLst:
    procesosLst = []
    procesos = []

    for i in range(len(Maquina)):
        if i > 1 and Maquina[i] != '':
            procesosLst.append([Maquina[i],Maquina[1]])
            procesosTotal.append([Maquina[i],Maquina[1]])
    # print(str(procesosTotal))
    for prod in range(len(procesosLst)):
        Dependencias = []
        for cond in condicionesLst:
            if procesosLst[prod] == [cond[3],cond[4]]:
                Dependencias.append([cond[1],cond[2]])
        # if prod > 0:
        #     Dependencias.append(procesosLst[prod - 1])
        procesos.append(proceso(procesosLst[prod], Dependencias, Maquina[1]))
    maquinas.append(maquina(Maquina[1], procesos))

for Producto in productosLst:
    MaquinasLst = []
    for i in range(len(Producto)):
        if i > 1 and Producto[i] != '':
            MaquinasLst.append(Producto[i])
    productos.append(tipoProducto(Producto[1], MaquinasLst, rand.randint(1, 100)))
    # productos.append(tipoProducto(Producto[1], MaquinasLst, 1))

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


# def Proceso(nombre, dependencias, tiempo):
#     if dependencias == []:
#         for evento in eventos:
#             if evento.nombre == nombre:
#                 for condicion in condiciones:
#                     if condicion.nombre == nombre:
#                     #             # for evento in eventos:
#                     #             #     if evento.nonmbre == nombre:
#                     #                     # while not evento.evento.is_set():
#                     #                     #     evento.evento.wait()
#                     #                     #     if evento.evento.is_set():
#                     #                     #         break
#                     #                     # evento.evento.clear()
#                         time.sleep(tiempo)
#                         condicion.condicion.acquire()
#                         condicion.condicion.notify_all()
#                         print("se procesó " + nombre)
#                         condicion.condicion.release()
#                         evento.evento.set()
#                         break
#                 else:
#                     evento.evento.wait()
#     else:
#         hilos = []
#         for dependencia in dependencias:
#             hilos.append(Thread(target=esperaDependencia(dependencia)))
#             hilos[-1].setName(nombre + " - dep: " + dependencia)
#             for evento in eventos:
#                 if evento.nombre == dependencia:
#                     if evento.evento.is_set():
#                         evento.evento.clear()
#                         try:
#                             hilos[-1].start()
#                         except:
#                             print()
#             # hilos[-1].start()
#
#         for hilo in hilos:
#             hilo.join()
#
#         for evento in eventos:
#             if evento.nombre == nombre:
#                 # if evento.evento.is_set():
#                 #     evento.evento.clear()
#                 for condicion in condiciones:
#                     if condicion.nombre == nombre:
#                         time.sleep(tiempo)
#                         condicion.condicion.acquire()
#                         print("se procesó " + nombre)
#                         condicion.condicion.notify_all()
#                         condicion.condicion.release()
#                         evento.evento.set()
#                         break
#
#
# def esperaDependencia(nombre):
#     for condicion in condiciones:
#         if condicion.nombre == nombre:
#             # print(" - Se espera al proceso " + nombre)
#
#             # for proceso in procesosLst:
#             #     if proceso.nombre == nombre:
#             #         time.sleep(proceso.tiempo)
#             condicion.condicion.acquire()
#             while True:
#
#
#                 if condicion.condicion.wait():
#                     break
#                 else:
#                     print(" - Se espera al proceso " + nombre)
#                 condicion.condicion.release()
#                 for evento in eventos:
#                     if evento.nombre == nombre:
#                         evento.evento.set()
#
#             print(" - Se espero al proceso " + nombre)
#             condicion.condicion.release()
#             # break
#
#
# # def esperaMaquina(nombre):
# #     for condicion in condicionesMaquina:
# #         if condicion.nombre == nombre:
# #             condicion.condicion.acquire()
# #             condicion.condicion.notify()
# #             condicion.condicion.release()
#
#
# # def Proceso(proceso):
# #     if proceso.dependencia == []:
# #
# #     else:
#
# for maquina in maquinas:
#     for proceso in maquina.procesos:
#         proceso.hilo = Thread(target=Proceso, args=(proceso.nombre, proceso.dependencia, proceso.tiempo))
#         proceso.hilo.setName(proceso.nombre)
#         # proceso.hilo.start()


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
    # time.sleep(1)
    # print(" H I L O P R O D U C T O ")
    # time.sleep(1)
    # print("hilo" + pro.nombre)
    # return 0

    while (time.time() - tiempo_de_inicio) < TiempoTotal:
        indice = 0
        HilosManufactura = []
        # while True:
        HilosManufactura.append(Thread(name=(pro.nombre + str(indice)), target=HiloManufactura, args=[pro]))
        # time.sleep(2)
        HilosManufactura[-1].start()
        HilosManufactura[-1].join()
        # for maq in pro.maquinas:
        #     for maquina in maquinas:
        #         if maquina.nombre == maq:
        #             HiloManufactura.append(Thread(name=(pro.nombre + str(indice)), target=HiloManufactura(maquina)))
        #
        indice += 1

def HiloManufactura(pro):
    # time.sleep(1)
    # print(" H I L O M A N U F A C T U R A ")
    if ((time.time() - tiempo_de_inicio) < TiempoTotal):
        HilosMaquina = []
        for maq in pro.maquinas:
            for maquina in maquinas:
                if maquina.nombre == maq:
                    HilosMaquina.append(Thread(name=(pro.nombre + maq), target=HiloMaquina, args=[maquina]))
                    HilosMaquina[-1].start()
        for hilo in HilosMaquina:
            hilo.join()
        if (time.time() - tiempo_de_inicio) < TiempoTotal:
            productos.append(pro)

def HiloMaquina(maq):
    # print(" H I L O M A Q U I N A ")
    if ((time.time() - tiempo_de_inicio) < TiempoTotal):
        HilosProceso = []

        for pro in maq.procesos:
            for proceso in procesosTotal:
                if proceso == pro.nombre:
                    HilosProceso.append(Thread(name=(str(proceso)), target=HiloProceso, args=[pro]))
                    HilosProceso[-1].start()
                    HilosProceso[-1].join()




def HiloProceso(pro):
    # print(" H I L O P R O C E S O  ")
    if ((time.time() - tiempo_de_inicio) < TiempoTotal):
        if pro.dependencia == []:
            time.sleep(pro.tiempo)
            almacen.append(pro.nombre)
        else:
            d = len(pro.dependencia)
            while d > 0:
                for dep in pro.dependencia:
                    if dep in almacen:
                        for i in range(len(almacen)):
                            if almacen[i] == dep:
                                almacen.pop(i)
                                time.sleep(pro.tiempo)
                                almacen.append(pro.nombre)
                                d -= 1
                                if d == 0:
                                    break
                    # else:
                    #     d = 0








Hilos = []
tiempo_de_inicio = time.time()
# while (time.time() - tiempo_de_inicio) < TiempoTotal:
for Producto in ProductosBeneficio:
    # print(" m a i n ")
    if len(Hilos) > len(productosLst):
        try:
            for Hilo in Hilos:
                Hilo.hilo.join()
        except:
            Hilos.append(producto(indice, Producto.nombre))
            Hilos[-1].hilo = (Thread(name=(str(Producto.nombre)), target=HiloProducto, args=[Producto]))
            Hilos[-1].hilo.start()
    else:
        Hilos.append(producto(indice, Producto.nombre))
        Hilos[-1].hilo = (Thread(name=(str(Producto.nombre)), target=HiloProducto, args=[Producto]))
        Hilos[-1].hilo.start()

time.sleep(TiempoTotal)



# for Hilo in Hilos:
#     Hilo.hilo.join()






# for evento in eventos:
#     if evento.evento.wait():
#         print("evento " + evento.nombre)
#         evento.evento.clear()
#
# for evento in eventos:
#     print("EVENTOS OCUPADOS")
#     if not evento.evento.is_set():
#         print("evento ocupado " + evento.nombre)
#         evento.evento.set()

# --------
#
# def procesarProducto(producto, i):
#     for maquina in maquinas:
#         for maq in producto.maquinas:
#             if maquina.nombre == maq:
#                 for proc in maquina.procesos:
#                     if not proc.hilo.is_alive():
#                         proc.hilo.start()
#                     # else:
#                     #     proc.hilo.join()
#                         # fabCond[i].acquire()
#                         # fabCond[i].notify_all()
#                         # fabCond[i].release()
#
#     almacen.append(producto)
#     fabCond[i].acquire()
#     fabCond[i].notify_all()
#     fabCond[i].release()
#
#
# # time.sleep(1)
# tiempo_de_inicio = time.time()
# while (time.time() - tiempo_de_inicio) < TiempoTotal:
#     for prod in ProductosBeneficio:
#         for maq in prod.maquinas:
#             for maquina in maquinas:
#                 if maq == maquina.nombre:
#                     for proc in maquina.procesos:
#                         for proceso in procesosTotal:
#                             if proc.nombre == proceso:
#                                 for evento in eventos:
#                                     if evento.nombre == proceso:
#                                         if evento.evento.is_set():
#                                             evento.evento.clear()
#                                             try:
#                                                 proc.hilo.start()
#                                             except:
#                                                 proc.hilo.join()
#                                             break

                                        # else:
                                        #     evento.evento.set()

#     for i in range(len(productos)):
#         # if fabricacion[i] == None:
#         if len(fabricacion[i]) > 0 :
#             if fabricacion[i][-1].indice > 0:
#                 indice =+ 1
#                 fabricacion[i].append(producto(indice, productos[i].nombre))
#                 fabricacion[i][-1].hilo = Thread(target=procesarProducto, args=(productos[i], i))
#                 fabricacion[i][-1].hilo.setName(productos[i].nombre)
#                 fabricacion[i][-1].hilo.start()
#             else:
#                 fabricacion[i][-1].join()
#                 # fabricacion[i] = None
#             fabCond[i].acquire()
#             if fabCond[i].wait():
#                 fabCond[i].release()
#                 fabricacion[i][-1].join()
#                 # fabricacion[i] = None
#             else:
#                 fabCond[i].release()
#         else:
#             indice = + 1
#             fabricacion[i].append(producto(indice, productos[i].nombre))
#             fabricacion[i][-1].hilo = Thread(target=procesarProducto, args=(productos[i], i))
#             fabricacion[i][-1].hilo.setName(productos[i].nombre)
#             fabricacion[i][-1].hilo.start()
#
#
#


    # break
# threads = []
# for func in [Produccion, consumidor]:
#     threads.append(Thread(target=func, args=(almacen)))
#     threads[-1].start()  # Starts the thread.
# for thread in threads:
#     thread.join()
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

