# from ConsoleInput import ingreso_en_consola
from randomGeneration import generacion_aleatoria
from fileInput import carga_por_archivo

def data_input():
    while True:
        N = input(
            "DATA INPUT\n SELECT DESIRED DATA INPUT METHOD:\n "
            "1) CSV FILE LOAD \n 2) RANDOM GENERATION\n")
        if N.isdigit():
            N= int(N)
            if 0 < N < 3:
                break
            else:
                print('ERROR: SELECT THE NUMBER OF THE DESIRED OPTION. \n')
        else:
            print('ERROR: SELECT THE NUMBER OF THE DESIRED OPTION. \n')

    if N == 1:
        Input = carga_por_archivo()
        # Input = [] # ingreso_en_consola()
    elif N == 2:
        # Input = carga_por_archivo()
        Input = generacion_aleatoria()
    else:
        Input = generacion_aleatoria()

    return Input