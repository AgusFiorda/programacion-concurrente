import threading
import random
import time

"""
Ejercicio 2:
Modificar el ejercicio anterior de modo que se lancen 3 hilos tipo A y uno tipo B y que no existan condiciones de carrera.
Probar para verificar que no se dan condiciones de carrera con cualquier número de hilos A y B concurrentes..
"""
x = 0

lock = threading.Lock()


def funcionHiloA():
    global x
    print(f"Inicio ejecucion de hilo A, con valor de la variable X en: {x}")
    num_aleatorio = random.randint(50, 100)
    retardo = random.uniform(0, 1)
    for i in range(num_aleatorio):
        lock.acquire()
        x += 1
        lock.release()
        time.sleep(retardo)
    print(
        f"Variable X al finalizar la ejecucion del hilo A es: {x} y el numero aleatorio fue de: {num_aleatorio}"
    )


def funcionHiloB():
    global x
    print(f"Inicio ejecucion de hilo B, con valor de la variable X en: {x}")
    num_aleatorio = random.randint(10, 12)
    retardo = random.uniform(1, 2)
    for i in range(num_aleatorio):
        print(
            f"el valor aleatorio generado por el hilo B es:{num_aleatorio} en la iteracion numero {i}"
        )
        time.sleep(retardo)
    print(f"El valor de la variable global X cuando ejecuto el hilo B es: {x}")


def main():
    print("Inicio programa principal")
    print("Valor Inicial: " + str(x))
    thread_1a = threading.Thread(target=funcionHiloA)
    thread_2a = threading.Thread(target=funcionHiloA)
    thread_3a = threading.Thread(target=funcionHiloA)
    thread_2 = threading.Thread(target=funcionHiloB)
    thread_1a.start()
    thread_2a.start()
    thread_3a.start()
    thread_2.start()
    thread_1a.join()
    thread_2a.join()
    thread_3a.join()
    thread_2.join()
    print("Valor Final: " + str(x))


main()
