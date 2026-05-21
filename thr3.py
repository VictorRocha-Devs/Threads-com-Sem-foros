import threading
import time
import random

DISTANCIA_MAXIMA = 50
posicao_chegada = 1
lock_podio = threading.Lock()  # Protege o contador do pódio

def corrida_sapo(id_sapo):
    global posicao_chegada
    distancia_percorrida = 0
    
    while distancia_percorrida < DISTANCIA_MAXIMA:
        pulo = random.randint(1, 5)
        distancia_percorrida += pulo
        
        if distancia_percorrida > DISTANCIA_MAXIMA:
            distancia_percorrida = DISTANCIA_MAXIMA
            
        print(f"Sapo #{id_sapo} pulou {pulo} cm. Total percorrido: {distancia_percorrida} cm.")
        time.sleep(0.1)  # Pequena pausa para visualização no console
        
    # Zona crítica para definir a classificação de chegada
    with lock_podio:
        podio = posicao_chegada
        posicao_chegada += 1
        
    print(f" Sapo #{id_sapo} CHEGOU! Posição: {podio}º lugar.")

if __name__ == "__main__":
    print(f"--- A CORRIDA COMEÇOU! (Distância: {DISTANCIA_MAXIMA}cm) ---")
    threads = []
    for i in range(1, 6):
        t = threading.Thread(target=corrida_sapo, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()