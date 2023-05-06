import threading
import random
import time

"""
Ejercicio 3:
Modificar el ejercicio anterior de modo que el hilo B haga las iteraciones cada un tiempo aleatorio entre 1 y 4 hasta que todos los hilos B terminen.
Probar para verificar que no se dan condiciones de carrera con cualquier número de hilos A y B concurrentes..
"""

import threading
import random
import time

x = 0
lock = threading.Lock()

# Se agrega una variable global para contar los hilos B que han terminado
hilos_b_terminados = 0
hilos_b_total = 1  # Se lanza un solo hilo B en este ejemplo


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
    global x, hilos_b_terminados
    print(f"Inicio ejecucion de hilo B, con valor de la variable X en: {x}")
    retardo = random.uniform(1, 4)
    while True:
        num_aleatorio = random.randint(2, 5)
        for i in range(num_aleatorio):
            print(
                f"el valor aleatorio generado por el hilo B es:{num_aleatorio} en la iteracion numero {i}"
            )
            time.sleep(retardo)
        # Se protege la variable global de hilos_b_terminados con un lock
        with lock:
            hilos_b_terminados += 1
            if hilos_b_terminados >= hilos_b_total:
                break  # Si todos los hilos B han terminado, se sale del ciclo while
    print(f"El valor de la variable global X cuando ejecuto el hilo B es: {x}")


def main(num_hilos_b):
    print("Inicio programa principal")
    print("Valor Inicial: " + str(x))
    hilos_b = []
    for i in range(num_hilos_b):
        hilo_b = threading.Thread(target=funcionHiloB)
        hilos_b.append(hilo_b)
        hilo_b.start()
        time.sleep(random.uniform(1, 4))
    thread_1a = threading.Thread(target=funcionHiloA)
    thread_2a = threading.Thread(target=funcionHiloA)
    thread_3a = threading.Thread(target=funcionHiloA)
    thread_1a.start()
    thread_2a.start()
    thread_3a.start()
    for hilo_b in hilos_b:
        hilo_b.join()
    thread_1a.join()
    thread_2a.join()
    thread_3a.join()
    print("Valor Final: " + str(x))


num_hilos_b = 4
main(4)
