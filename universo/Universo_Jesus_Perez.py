import matplotlib.pyplot as plt
import math
import random


def cal(k):
    strf = []
    strj = ""
    strs = []
    combination = []
    ones = []
    ones64 = []
    oneslogten = []
    alphabet = ['0', '1']
    if (k >= 0):
        combination.append('v')
        strf.append('e')
        strj += strf[0]
    if (k >= 1):
        combination.append(alphabet)
        strf.append('0')
        strf.append('1')
        strj += strf[1]
        strj += strf[2]
    for i in range(2, k + 1):
        nstr = []
        laststr = combination[i - 1]
        for l in range(0, len(laststr)):
            for j in range(0, len(alphabet)):
                nstr.append(laststr[l] + alphabet[j])
                strf.append(laststr[l] + alphabet[j])
                strj += (laststr[l] + alphabet[j])
        combination.append(nstr)

    for z in range(0, len(strf)):
        ones.append(strf[z].count('1'))

    for i in range(0, len(strj), 64):
        strs.append(strj[i:i + 64])

    for j in range(0, len(strs)):
        ones64.append(strs[j].count('1'))
        oneslogten.append(math.log10(ones64[j]))

    file = open("out.txt", "w")
    file.write(str(strf))
    file.close

    file = open("out2.txt", "w")
    file.write(str(strs))
    file.close

    fig, ax = plt.subplots()
    ax.plot(range(1, len(strf) + 1), ones)

    fig, ax2 = plt.subplots()
    ax2.plot(range(1, len(strs) + 1), ones64)

    fig, ax3 = plt.subplots()
    ax3.plot(range(1, len(strs) + 1), oneslogten)
    plt.show()


r = "s"
while (r == "s"):
    d = input("Eliga una opción, 1.-Usuario ingresa ContenidoCad 2.-ContenidoCad calculada aleatoriamente\ContenidoCad")
    if (d == "1"):
        k = int(input("Ingrese el valor de ContenidoCad\ContenidoCad"))
    if (d == "2"):
        k = random.randint(0, 20)

    cal(k)
    r = input("Desea calcular otra ContenidoCad? s/ContenidoCad\ContenidoCad")
