import threading
import random
import time

"""
Ejercicio 1:
Implemente un programa que lance dos hilos A y B, ambos con acceso a una variable X (global) inicializada en cero. 
El hilo A incrementa X en 1 hasta llegar a una cantidad aleatoria entre 50 y 100 intercalando un retardo aleatorio entre 0 y 1 segundo entre cada incremento de X.
El hilo B hará una número aleatorio entre 10 y 100 iteraciones cada un tiempo aleatorio entre 1 y 2 segundos, imprimiendo el valor de X en cada iteración. 
Tanto A como B deberán imprimir mensajes al arrancar y al terminar, identificando al hilo. 
El hilo A deberá también indicar el valor final de X en el mensajel final.. 

Pregunta: Hay condiciones de carrera? Como las evitaria?
Respuesta: No hay condicion de carrera porque solamente un hilo esta modificando la variable global mientras que el otro hilo solamente esta imprimiendo en pantalla.
Para que exista condicion de carrera ambos hilos tendrian que modificar la varible compartida.
"""
x = 0

lock = threading.Lock()


def funcionHiloA():
    global x
    print(f"Inicio ejecucion de hilo A, con valor de la variable X en: {x}")
    num_aleatorio = random.randint(50, 100)
    retardo = random.uniform(0, 1)
    for i in range(num_aleatorio):
        x += 1
        time.sleep(retardo)
    print(f"Valor de la variable X al finalizar la ejecucion del hilo A es: {x} ")


def funcionHiloB():
    global x
    print(f"Inicio ejecucion de hilo B, con valor de la variable X en: {x}")
    num_aleatorio = random.randint(10, 100)
    retardo = random.uniform(1, 2)
    for i in range(num_aleatorio):
        print(
            f"el valor aleatorio generado por el hilo B es:{num_aleatorio} en la iteracion numero {i}"
        )
        time.sleep(retardo)
    print(f"El valor de la variable global X cuando ejecuto el hilo B es: {x}")


print("Inicio programa principal")

print("Valor Inicial: " + str(x))


thread_1 = threading.Thread(target=funcionHiloA)

thread_2 = threading.Thread(target=funcionHiloB)


thread_1.start()

thread_2.start()


thread_1.join()

thread_2.join()


print("Valor Final: " + str(x))
