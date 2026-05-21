import threading
import time
import random

# Limite máximo de 5 carros na pista simultaneamente
pista_geral = threading.Semaphore(5)

# 7 semáforos (um para cada escuderia), limitando a 1 carro por equipe na pista
escuderias = [threading.Semaphore(1) for _ in range(7)]

def treinar_carro(numero_carro, escuderia_id, nome_escuderia):
    print(f"[{nome_escuderia} - Carro {numero_carro}] Aguardando para entrar na pista.")
    
    # Regra 1: Aguarda a vaga na sua própria escuderia
    with escuderias[escuderia_id]:
        # Regra 2: Aguarda espaço na pista geral
        with pista_geral:
            print(f" >>> [{nome_escuderia} - Carro {numero_carro}] ENTROU NA PISTA!")
            
            # Executa as 3 voltas
            for volta in range(1, 4):
                # Simula o tempo de volta (ex: entre 60 e 90 ms rápidos)
                tempo_volta = random.randint(60, 90) / 1000.0 
                time.sleep(tempo_volta)
                # Exibe o tempo formatado na tela
                print(f"[{nome_escuderia} - Carro {numero_carro}] Volta {volta} concluída em {tempo_volta * 10:.2f}s (simulados).")
                
            print(f" <<< [{nome_escuderia} - Carro {numero_carro}] Terminou o treino e SAÍU da pista.")

if __name__ == "__main__":
    threads = []
    
    # Criando os 14 carros (7 equipes * 2 carros por equipe)
    for e in range(7):
        nome_equipe = f"Equipe_{e + 1}"
        # Carro 1 da equipe
        t1 = threading.Thread(target=treinar_carro, args=(1, e, nome_equipe))
        # Carro 2 da equipe
        t2 = threading.Thread(target=treinar_carro, args=(2, e, nome_equipe))
        
        threads.extend([t1, t2])
        t1.start()
        t2.start()

    for t in threads:
        t.join()