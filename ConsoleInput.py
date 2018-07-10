
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def inputInteger(inputmessage, condition):
    while True:
        var = input(inputmessage)
        if var.isdigit():
            var = int(var)
            if var > condition:
                return var
            else:
                print('ERROR: ENTRADA FUERA DE RANGO; EL NUMERO TIEN EQUE SER MAYOR QUE ' + str(condition))
                return False
        else:
            print('ERROR: TIPO DE DATO INVALIDO; INGRESE UN NÚMERO ENTERO')


def inputString(inputmessage):
    var = input(inputmessage)
    return var


def ingreso_en_consola():
    print("CONSOLE DATA INPUT")
    maquinas = []

    nmachines = inputInteger('ingrese la cantidad de maquinas\n', 1)

    for i in range(nmachines):
        maquina = ['maquina']
        while True:
            used = 0
            nommaq = inputString('ingrese el nombre de la maquina\n')
            for maq in maquinas:
                if nommaq in maq:
                    print('Error: ese nombre ya existe, utilice otro')
                    used = 1
            if used == 0:
                maquina.append(nommaq)
                break
        nprocesos = inputInteger('Ingrese la cantidad de procesos de la maquina ' + maquina[1] + '\n', 0)
        for i in range(nprocesos):
            while True:
                nombreproc = inputString('ingrese el nombre del proceso\n')
                if not nombreproc in maquina:
                    maquina.append(nombreproc)
                    break
                else:
                    print('ERROR: Ese nombre ya existe utilice uno distinto')
        maquinas.append(maquina)
    print(maquinas)

ingreso_en_consola()
    #
    # while True:
    #     mi = input('Introduzca el número de maquinas\n')
    #     if (mi.isdigit()):
    #         mi = int(mi)
    #         if (mi > 1):
    #             break
    #         else:
    #             print(
    #                 'ERROR: ENTRADA FUERA DE RANGO\nLA CANTIDAD DE MAQUINAS TIENE QUE SER MAYOR QUE 1\n')
    #     else:
    #         print('ERROR: TIPO DE DATO INVALIDO\nLA CANTIDAD DE MAQUINAS TIENE QUE SER MAYOR QUE 1\n')
    #
    # while True:
    #     for i in range(mi):
    #         while True:
    #             mi = input('Introduzca el número de procesos de la maquina\n')
    #             if (mi.isdigit()):
    #                 mi = int(mi)
    #                 if (mi > 1):
    #                     break
    #                 else:
    #                     print(
    #                         'ERROR: ENTRADA FUERA DE RANGO\nLA CANTIDAD DE MAQUINAS TIENE QUE SER MAYOR QUE 1\n')
    #             else:
    #                 print('ERROR: TIPO DE DATO INVALIDO\nLA CANTIDAD DE MAQUINAS TIENE QUE SER MAYOR QUE 1\n')
    #
    # while True:
    #     while True:
    #         rx = input('Input the x dimension of r vector\n')
    #         if (isfloat(rx)):
    #             rx = float(rx)
    #             if (rx >= 0 and rx <= 1):
    #                 break
    #             else:
    #                 print(
    #                     'ERROR: INPUT OUT OF RANGE\nTHE r VECTOR\'S X-DIMENSION HAS TO BE A VALUE BETWEEN 0 AND 1\n')
    #         else:
    #             print('ERROR: INVALID DATA TYPE\nTHE r VECTOR\'S X-DIMENSION HAS TO BE A VALUE BETWEEN 0 AND 1\n')
    #
    #     while True:
    #         ry = input('Input the y dimension of r vector\n')
    #         if (isfloat(ry)):
    #             ry = float(ry)
    #             if (ry >= 0 and ry <= 1):
    #                 break
    #             else:
    #                 print(
    #                     'ERROR: INPUT OUT OF RANGE\nTHE r VECTOR\'S Y-DIMENSION HAS TO BE A VALUE BETWEEN 0 AND 1\n')
    #         else:
    #             print('ERROR: INVALID DATA TYPE\nTHE r VECTOR\'S Y-DIMENSION HAS TO BE A VALUE BETWEEN 0 AND 1\n')
    #     r = Vector(rx, ry)
    #     if r.magnitude <= 1:
    #         break
    #     else:
    #         print("ERROR: MAGNITUDE ERROR\nTHE X AND Y DIMENSIONS OF THE VECTOR r SHOULD BE IN A WAY THAT THE MAGNITUDE OF THE VERCTOR RESULTS TO A VALUE BETWEEN 0 AND 1")
    #
    # while True:
    #     maxspace = input('Input the size of the search space\n')
    #     if (isfloat(maxspace)):
    #         maxspace = float(maxspace)
    #         if (maxspace > 0):
    #             break
    #         else:
    #             print(
    #                 'ERROR: INPUT OUT OF RANGE\nTHE SEARCH SPACE HAS TO BE GREATER THAN 0\n')
    #     else:
    #         print('ERROR: INVALID DATA TYPE\nTHE SEARCH SPACE HAS TO BE GREATER THAN 0\n')
    #
    # while True:
    #     PreyQuantity = input('Input the amount of preys\n')
    #     if (PreyQuantity.isdigit()):
    #         PreyQuantity = int(PreyQuantity)
    #         if (PreyQuantity > 1):
    #             break
    #         else:
    #             print(
    #                 'ERROR: INPUT OUT OF RANGE\nTHE AMOUNT OF PREYS HAS TO BE AN INTEGER GREATER THAN 0\n')
    #     else:
    #         print('ERROR: INVALID DATA TYPE\nTHE AMOUNT OF PREYS HAS TO BE AN INTEGER GREATER THAN 0\n')
    #
    # for each in range(PreyQuantity):
    #     prey = Prey(0,0,0)
    #
    #     while True:
    #         prey.value = input('Input the prey\'s value\n')
    #         if (isfloat(prey.value)):
    #             prey.value = float(prey.value)
    #             if (prey.value >= 0):
    #                 break
    #             else:
    #                 print(
    #                     'ERROR: INPUT OUT OF RANGE\nTHE VALUE OF PREYS HAS TO BE A FLOAT GREATER THAN 0 \n')
    #         else:
    #             print('ERROR: INVALID DATA TYPE\nTHE VALUE OF PREYS HAS TO BE A FLOAT GREATER THAN 0 \n')
    #     while True:
    #         prey.x = input('Input the prey\'s x coordinate ')
    #         if (isfloat(prey.x)):
    #             prey.x = float(prey.x)
    #             if (prey.x >= 0 and prey.x <= maxspace):
    #                 break
    #             else:
    #                 print(
    #                     'ERROR: INPUT OUT OF RANGE\nTHE X COORDINATE OF PREYS HAS TO BE A FLOAT BETWEEN 0 AND ' + str(maxspace) + '\n')
    #         else:
    #             print('ERROR: INVALID DATA TYPE\nTHE X COORDINATE OF PREYS HAS TO BE A FLOAT BETWEEN 0 AND ' + str(maxspace) + '\n')
    #     while True:
    #         prey.y = input('Input the prey\'s y coordinate ')
    #         if (isfloat(prey.y)):
    #             prey.y = float(prey.y)
    #             if (prey.y >= 0 and prey.y <= maxspace):
    #                 break
    #             else:
    #                 print(
    #                     'ERROR: INPUT OUT OF RANGE\nTHE Y COORDINATE OF PREYS HAS TO BE A FLOAT BETWEEN 0 AND ' + str(maxspace) + '\n')
    #         else:
    #             print('ERROR: INVALID DATA TYPE\nTHE Y COORDINATE OF PREYS HAS TO BE A FLOAT BETWEEN 0 AND ' + str(maxspace) + '\n')
    #
    #     Preys.append(prey)
    #
    # while True:
    #     WhaleQuantity = input('Input the amount of whales\n')
    #     if (WhaleQuantity.isdigit()):
    #         WhaleQuantity = int(WhaleQuantity)
    #         if (WhaleQuantity > 1):
    #             break
    #         else:
    #             print(
    #                 'ERROR: INPUT OUT OF RANGE\nTHE AMOUNT OF WHALES HAS TO BE AN INTEGER GREATER THAN 1\n')
    #     else:
    #         print('ERROR: INVALID DATA TYPE\nTHE AMOUNT OF WHALES HAS TO BE AN INTEGER GREATER THAN 1\n')
    #
    # for each in range(WhaleQuantity):
    #     whale = Whale(0, 0, Prey(0, 0, 0))
    #
    #     while True:
    #         whale.x = input('Input the whale\'s x coordinate ')
    #         if (isfloat(whale.x)):
    #             whale.x = float(whale.x)
    #             if (whale.x >= 0 and whale.x <= maxspace):
    #                 break
    #             else:
    #                 print(
    #                     'ERROR: INPUT OUT OF RANGE\nTHE X COORDINATE OF WHALES HAS TO BE A FLOAT BETWEEN 0 AND ' + str(maxspace) + '\n')
    #         else:
    #             print('ERROR: INVALID DATA TYPE\nTHE X COORDINATE OF WHALES HAS TO BE A FLOAT BETWEEN 0 AND ' + str(maxspace) + '\n')
    #     while True:
    #         whale.y = input('Input the whale\'s y coordinate ')
    #         if (isfloat(whale.y)):
    #             whale.y = float(whale.y)
    #             if (whale.y >= 0 and whale.x <= maxspace):
    #                 break
    #             else:
    #                 print(
    #                     'ERROR: INPUT OUT OF RANGE\nTHE Y COORDINATE OF WHALES HAS TO BE A FLOAT BETWEEN 0 AND ' + str(maxspace) + '\n')
    #         else:
    #             print('ERROR: INVALID DATA TYPE\nTHE Y COORDINATE OF WHALES HAS TO BE A FLOAT BETWEEN 0 AND ' + str(maxspace) + '\n')
    #
    #     while True:
    #         preysv = []
    #         preysx = []
    #         preysy =[]
    #         for prey in Preys:
    #             preysv.append(prey.value)
    #             preysx.append(prey.x)
    #             preysy.append(prey.y)
    #
    #         d = {"Value": preysv, "x": preysx, "y": preysy}
    #         df = pd.DataFrame(data=d)
    #         print("\nPREY")
    #         print(df)
    #         whalePrey = input('Input the whale\'s prey index\n')
    #         if (whalePrey.isdigit()):
    #             whalePrey = int(whalePrey)
    #             if (whalePrey >= 0 and whalePrey < len(Preys)):
    #                 whale.prey = Preys[whalePrey]
    #                 break
    #             else:
    #                 print(
    #                     'ERROR: INPUT OUT OF RANGE\nTHE PREY INDEX HAS TO BE AN INTEGER GREATER THAN OR EQUAL TO 0 AND LESS THAN ' +str(len(Preys)) + '\n')
    #         else:
    #             print('ERROR: INVALID DATA TYPE\nTHE PREY INDEX HAS TO BE AN INTEGER GREATER THAN OR EQUAL TO 0 AND LESS THAN ' +str(len(Preys)) + '\n')
    #
    #     Whales.append(whale)

    # # Printing data by pandas data frame
    # whalesx = []
    # whalesy = []
    # whalespx = []
    # whalespy = []
    # whalespv = []
    # for whale in Whales:
    #     whalesx.append(whale.x)
    #     whalesy.append(whale.y)
    #     whalespx.append(whale.prey.x)
    #     whalespy.append(whale.prey.y)
    #     whalespv.append(whale.prey.value)
    #
    # d = {"Whale x": whalesx, "Whale y": whalesy, "Prey value": whalespv, "Prey x": whalespx, "Prey y": whalespv}
    # df = pd.DataFrame(data=d)
    # print("WHALES")
    # print(df)
    #
    # preysx = []
    # preysy = []
    # preysc = []
    # preysv = []
    # for prey in Preys:
    #     preysx.append(prey.x)
    #     preysy.append(prey.y)
    #     preysc.append([prey.x, prey.y])
    #     preysv.append(prey.value)
    #
    # d = {"Value": preysv, "x": preysx, "y": preysy}
    # df = pd.DataFrame(data=d)
    # print("\nPREY")
    # print(df)


    #     WhaleQuantity = input('Input the amount of whales\n')
    #     if (WhaleQuantity.isdigit()):
    #         WhaleQuantity = int(WhaleQuantity)
    #         if (WhaleQuantity > 1):
    #             break
    #         else:
    #             print(
    #                 'ERROR: INPUT OUT OF RANGE\nTHE AMOUNT OF WHALES HAS TO BE AN INTEGER GREATER THAN 0\n')
    #     else:
    #         print('ERROR: INVALID DATA TYPE\nTHE AMOUNT OF WHALES HAS TO BE AN INTEGER GREATER THAN 0\n')
    #
    #
    # print('Ingrese los objeto y sus caracteristicas con el siguiente formato:\n' + formato + '\n')
    #
    # for n in range(CantidadO):
    #     while True:
    #         Datos=input(Error)
    #         Error=''
    #         Datos=Datos.split('-')
    #         if(len(Datos)!= longitud):
    #             Error="ERROR #1: FORMATO DE ENTRADA INCORRECTO\nUTILICE EL FORMATO INDICADO ANTERIORMENTE:" \
    #                   "\n" + formato + "\n"
    #         for NombreR in Objetos:
    #             if(NombreR.name==Datos[0]):
    #                 Error="ERROR #2: NOMBRE DE OBJETO REPETIDO\nEL NOMBRE DE LOS OBJETOS NO SE PUEDE REPTIR\n"
    #         try:
    #             if(Datos[1].isdigit() == False or int(Datos[1]) < 1):
    #                 Error="ERROR #3: TIPO DE ENTRADA INVALIDA\nEL PESO TIENE QUE SER UN NUMERO ENTERO MAYOR QUE 0\n"
    #
    #             if tipo == 1:
    #                 if (Datos[2].isdigit() == False or int(Datos[2]) < 0):
    #                     Error = "ERROR #3: TIPO DE ENTRADA INVALIDA\nLA GANANCIA TIENE QUE SER UN NUMERO ENTERO MAYOR QUE 0\n"
    #             elif tipo == 2:
    #                 if(Datos[2].isdigit() == False or int(Datos[2]) < 0):
    #                     Error="ERROR #3: TIPO DE ENTRADA INVALIDA\nLA GANANCIA TIENE QUE SER UN NUMERO ENTERO MAYOR O IGUAL QUE 0\n"
    #                 if (Datos[3].isdigit() == False or int(Datos[3]) < 1):
    #                     Error = "ERROR #3: TIPO DE ENTRADA INVALIDA\nLA GANANCIA TIENE QUE SER UN NUMERO ENTERO MAYOR QUE 0\n"
    #
    #             if(Error==''):
    #                 break
    #         except IndexError:
    #             Error = "ERROR #4: FORMATO DE ENTRADA ERRONEO\n INGRESE LA INFORMACIÓN DEL OBJETO CON EL FORMATO " \
    #                     "\"" + formato + "\" (INCLUYENDO LOS GUIONES)\n NO ES POSIBLE OMITIR NINGUN DATO DEL OBJETO\n"
    #     if tipo == 1:
    #         Objetos.append(Item(Datos[0], int(Datos[1]), 0, int(Datos[2])))
    #     if tipo == 2:
    #         Objetos.append(Item(Datos[0], int(Datos[1]), int(Datos[2]), int(Datos[3])))
    #
    # while True:
    #     Capacidad = input('Ingrese la capacidad en peso de la mochila\n')
    #     if tipo == 2:
    #         CapVol = input('Ingrese la capacidad en volumen de la mochila\n')
    #     else:
    #         CapVol = '0'
    #     if tipo == 3:
    #         PenalizacionW = input('Ingrese la penalización en peso por unidad\n')
    #         PenalizacionV = input('Ingrese la penalización en volumen por unidad\n')
    #     else:
    #         PenalizacionV = '0'
    #         PenalizacionW = '0'
    #
    #     if (Capacidad.isdigit() and CapVol.isdigit() and PenalizacionW.isdigit() and PenalizacionV.isdigit()):
    #         Capacidad = int(Capacidad)
    #         CapVol = int(CapVol)
    #         if (Capacidad > 0 and CapVol >= 0):
    #             break
    #         else:
    #             print('ERROR #4: ENTRADA FUERA DE RANGO\nLA CAPACIAD Y LA PENALIZACION TIENEN QUE SER UN NUMERO ENTERO '
    #                   'MAYOR A CERO\n')
    #     else:
    #         print('ERROR #3: TIPO DE ENTRADA INVALIDA\nLA CANTIDAD DE OBJETOS TIENE QUE SER UN NUMERO ENTERO\n')
    #
    # for Objeto in Objetos:
    #     Objeto.maxUnit = Capacidad / Objeto.weight
    #     if CapVol != 0:
    #         Objeto.maxUnitVol = CapVol / Objeto.volume
    #     else:
    #         Objeto.maxUnitVol = 0
    #
    # Capacidad = [Capacidad, CapVol, [PenalizacionW, PenalizacionV]]

    # print([mi, r, maxspace, Whales, Preys])
    # return([mi, r, maxspace, Whales, Preys])
