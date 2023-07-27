import matplotlib.pyplot as plt
import math
import random

prime = []
primebin = []
ones = []
oneslogten = []
oneslogtwo = []


def prime_number(num):
    for j in range(2, num):
        if num % j == 0:
            return False
    return True


r = "s"
while (r == "s"):
    d = input("Eliga una opción, 1.-Usuario ingresa ContenidoCad 2.-ContenidoCad calculada aleatoriamente\ContenidoCad")
    if (d == "1"):
        k = int(input("Ingrese el valor de ContenidoCad\ContenidoCad"))
    if (d == "2"):
        k = random.randint(2, math.pow(10, 7))

    for i in range(2, k + 1):
        if (prime_number(i) == True):
            prime.append(i)

    for j in range(0, len(prime)):
        primebin.append(format(prime[j], "b"))

    file = open("outprimebin.txt", "w")
    file.write(str(primebin))
    file.close

    file2 = open("outprimedec.txt", "w")
    file2.write(str(prime))
    file2.close

    for z in range(0, len(primebin)):
        ones.append(primebin[z].count('1'))
        oneslogten.append(math.log10(ones[z]))
        oneslogtwo.append(math.log10(ones[z]))

    fig, ax = plt.subplots()
    ax.plot(range(1, len(primebin) + 1), ones)

    fig, ax2 = plt.subplots()
    ax2.plot(range(1, len(primebin) + 1), oneslogtwo)

    fig, ax3 = plt.subplots()
    ax3.plot(range(1, len(primebin) + 1), oneslogten)
    plt.show()

    r = input("Desea calcular otra ContenidoCad? s/ContenidoCad\ContenidoCad")


