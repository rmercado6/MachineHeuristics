import random

data = []
condicionesLst = []
productosLst = []
maquinasLst = []

nameMachine = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y',
    'Z'
]

nameProcess = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y',
    'z'
]

# nameProcess = {
#     'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'F': 'f', 'G': 'g',
#     'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm',
#     'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's',
#     'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y',
#     'Z': 'z'
# }

def generacion_aleatoria():
    nprod = random.randint(2, 4)
    nmachine = random.randint(2, 5)
    procesos = []
    for i in range(nmachine):
        maquina = ['maquina']
        maquina.append(nameMachine[i])
        nproc = random.randint(1, 3)
        for j in range(nproc):
            maquina.append(nameProcess[i] + str(j))
            procesos.append(nameProcess[i] + str(j))
        maquinasLst.append(maquina)

    for i in range(nprod):
        producto = ['producto']
        producto.append(nameMachine[-(i+1)])
        nmachine = random.randint(2, 4)
        for j in range(nmachine):
            machine = random.randint(0, len(maquinasLst) - 1)
            if not nameMachine[machine] in producto:
                producto.append(nameMachine[machine])
        productosLst.append(producto)

    for proceso in procesos:
        prob = random.random()
        if prob < 0.2:
            while True:
                dependency = procesos[random.randint(0, len(procesos) - 1)]
                if dependency[0] != proceso[0]:
                    condition = ['cond', dependency]
                    for i in range(len(nameProcess)):
                        if dependency[0] == nameProcess[i]:
                            condition.append(nameMachine[i])
                    condition.append(proceso)
                    for i in range(len(nameProcess)):
                        if proceso[0] == nameProcess[i]:
                            condition.append(nameMachine[i])
                    condicionesLst.append(condition)
                    break

    return [data, condicionesLst, productosLst, maquinasLst]


# generacion_aleatoria()

    #
    # #Global Variables
    # Preys =[]
    # Whales = []
    #
    # mi = random.randint(100, 1000)
    #
    #
    # #vector r, it's magnitude is in between [0, 1]
    # r = Vector(0, 0)
    # r.magnitude = random.random()
    # rand = random.random()
    # while rand > r.magnitude:
    #     rand = random.random()
    # r.x = rand
    # r.calc_y()
    #
    #
    #
    # # max values
    # maxspace = random.randint(2, 10)
    # maxvalue = random.randint(5, 50)
    #
    # # prey and whale generation
    # npreys = random.randint(10, 25)
    # nwhales = random.randint(5, 10)
    # for i in range(npreys):
    #     prey = Prey(random.random() * maxspace, random.random() * maxspace, random.random() * maxvalue)
    #     Preys.append(prey)
    #
    # for j in range(nwhales):
    #     whale = Whale(random.random() * maxspace, random.random() * maxspace, Preys[random.randint(0, npreys) - 1])
    #     Whales.append(whale)
    #
    # # print([mi, r, maxspace, Whales, Preys])
    # return ([mi, r, maxspace, Whales, Preys])
