import csv

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


data = []
condicionesLst = []
productosLst = []
maquinasLst = []


def carga_por_archivo():
    # -----LECTURA DE INFORACION DE ARCHIVO CSV-----
    try:
        with open('maquinas.csv', 'r') as archivo:
            lineas = csv.reader(archivo, delimiter=' ', quotechar='|')
            for row in lineas:
                rawstr = ', '.join(row)
                raw = rawstr.split(",")
                data.append(raw)
        # data.pop(0)
    except IOError:
        print("Error al cargar el archivo maquinas.csv")
    # --acomodo de información--
    for i in range(len(data)):
        if i <= len(data):
            if data[i][0] == 'cond':
                condicionesLst.append(data[i])
            elif data[i][0] == 'producto':
                productosLst.append(data[i])
            elif data[i][0] == 'maquina':
                maquinasLst.append(data[i])
    if len(productosLst) <= 1 or len(maquinasLst) <= 1:
        raise ValueError('Invalid data input on file maquinas.csv')
    else:
        print(data)
        print(condicionesLst)
        print(productosLst)
        print(maquinasLst)
        return([data, condicionesLst, productosLst, maquinasLst])
