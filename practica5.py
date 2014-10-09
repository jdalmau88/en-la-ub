#De: Joan Dalmau Carmona
#Practica 5
import time
import math

def fib1(n):
    if n==1:
        return 1#si el numero introducido es uno directamente retornaremos un 1
    if n==0:
        return 0#si el numero introducido es uno directamente retornaremos un 0
    return fib1(n-1) + fib1(n-2)#por cada valor que tengamos llamaremos sin parar la funcion fib1 (es decir una para el valor anterior y otra por el anterior del anterior y los sumaremos)

def fib():
    try:
        n= input("Di un numero para calcular el enesimo elemento de la secuencia Fibonacci")
        t1 = time.clock()
        print fib1(n)#llamamos la  funcion fib1 y la imprimimos
        t2 = time.clock()
        print "\n"
        print "El temps de proces ha estat %0.3f ms" % ((t2-t1)*1000)
    except:
        print "Numero incorrecto"

def mcd():
    try:
        n,m = input("Escribe dos numeros para hacer el MCD(usa una coma entre medio de cada numero)")
        while m!=0:
            n, m = m, n%m #busca el modulo de n, si n es mas pequeño que m el modulo de n sera m, y a m se le asignara el valor mas pequeño, apartir de alli empezara a calcular,se le asignara a n el valor de m cada vez y en m el modulo de la operacion anterior
        print n
    except:
        print "Numeros introducidos erroneamente"

def eratostenes(n):
    criba = [True] * n
    for i in xrange(2, int(math.sqrt(n)) + 1):#Usamos el xrange es mas rapido que el range, por eso aqui utilizo este.El Bucle ira desde 2 a la raiz del numero introducido
        for j in xrange(i * i, n + 1, i):
            criba[j - 1] = False#Nos pondra False donde en la posicion donde el Numero no es primo
    primos = [p for p in xrange(2, n + 1) if criba[p - 1]==True]#deteminando si es primo o no mediante el false o el true podremos añadirlos en una lista pasando por todos los True y false y añadiendo solamente los true
    #Noprimos = [p for p in xrange(2, n + 1) if criba[p - 1]==False]                      # Si quisieramos los No primos hariamos esta linea pero en este caso no hace falta
    return primos

def era1():
    try:
        n = input("Hasta que numero quieres que le mostremos los primeros?")
        if n>1:
            primeros=eratostenes(n)#llamaremos la funcion para calcular los primeros
            print primeros
        else:
            print "Error usa numeros mayores de 1, ya que sino no podremos mostrales ningun numero ya que no hay ningun numero primero inferior de 1"
    except:
        print "Error, usa solo numeros"
def era2():
    t1 = time.clock()
    n = 10000000
    print "Calculando la cantidad de primeros en el numero 10000000, espere"
    primeros=eratostenes(n)
    print len(primeros)#hacemos un len para saber la cantidad de primeros que hay
    t2 = time.clock()
    print "\n"
    print "El temps de proces ha estat %0.3f ms" % ((t2-t1)*1000)

def factorp():
    i=2
    try:
        t1 = time.clock()
        primero=True
        n = input("Que numero quieres saber si es primero?")
        if n>1:
            while i<=n-1 and primero==True:#Usaremos un while ya que si vemos k es divisible por 2,3,4... o algun numero ya sabremos que no es primero y ya podremos salir del bucle
                if n%i==0:#pasamos por todos los numeros mayores de 2 y menores de "n" y miramos si es primero haciendo el mod 
                    primero=False
                i=i+1
            if primero==False:
                print "No es primero"
            else:
                print "Es primero"
        else:
            print "Error numero no valido"
        t2 = time.clock()
        print "\n"
        print "El temps de proces ha estat %0.3f ms" % ((t2-t1)*1000)
    except:
        print "Error, usa solo numeros"
def fermatp():
    try:
        i=0
        t1 = time.clock()
        valor=0
        a=[2,3,5]
        n = input("Que numero quieres saber si es primero?")
        if n>1:
            while i<=2 and valor==0:#estar en el bucle mientras "i" sea menor que dos ya que "a" solo contiene 3 valores y que "valor" sea 0 ya que si no lo es, sera primero y saldremos del bucle
                valor=(a[i]**(n-1))%n#si el mod da 0 sera compuesto sino primero
                i=i+1
            if valor ==1:
                print "Es primero"
            else:
                print "Es compuesto"
        else:
            print "Error numero no valido"
        t2 = time.clock()
        print "\n"
        print "El temps de proces ha estat %0.3f ms" % ((t2-t1)*1000)
    except:
        print "Numero incorrecto"
    
def main():
    #fib()
    #mcd()
    era1()
    era2()
    factorp()
    fermatp()
    
main()
