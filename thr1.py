import threading
import time

# Semáforo que permite apenas 1 carro no cruzamento por vez
cruzamento = threading.Semaphore(1)

def gerenciar_carro(id_carro, sentido):
    print(f"Carro #{id_carro} chegou ao cruzamento indo para o {sentido}.")
    
    # Tenta entrar no cruzamento (adquire o semáforo)
    with cruzamento:
        print(f">>> Carro #{id_carro} ESTÁ PASSANDO no sentido {sentido}...")
        time.sleep(1.5)  # Simula o tempo cruzando
        print(f"<<< Carro #{id_carro} terminou de passar.")

if __name__ == "__main__":
    sentidos = ["Norte", "Sul", "Leste", "Oeste"]
    threads = []

    # Cria e inicia uma thread para cada carro/sentido
    for i, sentido in enumerate(sentidos):
        t = threading.Thread(target=gerenciar_carro, args=(i + 1, sentido))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()