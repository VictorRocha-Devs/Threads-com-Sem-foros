import threading
import time
import random

porta = threading.Semaphore(1)

def simular_pessoa(id_pessoa):
    distancia_total = 200
    distancia_percorrida = 0
    # Velocidade aleatória entre 4 e 6 m/s
    velocidade = random.randint(4, 6)
    
    print(f"Pessoa #{id_pessoa} começou a caminhar a {velocidade} m/s.")
    
    # Caminhada no corredor
    while distancia_percorrida < distancia_total:
        time.sleep(1)  # Passa 1 segundo
        distancia_percorrida += velocidade
        if distancia_percorrida > distancia_total:
            distancia_percorrida = distancia_total
        print(f"Pessoa #{id_pessoa} percorreu {distancia_percorrida}m.")
        
    print(f"Pessoa #{id_pessoa} chegou na porta e aguarda sua vez.")
    
    # Sincronização para cruzar a porta
    with porta:
        print(f"-> Pessoa #{id_pessoa} está abrindo e cruzando a porta...")
        tempo_porta = random.uniform(1, 2)  # Entre 1 e 2 segundos
        time.sleep(tempo_porta)
        print(f"<- Pessoa #{id_pessoa} passou pela porta com sucesso!")

if __name__ == "__main__":
    threads = []
    for i in range(1, 5):
        t = threading.Thread(target=simular_pessoa, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()