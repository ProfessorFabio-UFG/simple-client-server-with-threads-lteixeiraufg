from socket import *
from constCS import *
import threading
import time
import random

def fazer_requisicao(num1, num2, operacao, id_thread):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    mensagem = f"{num1} {num2} {operacao}"
    print(f"[Thread-{id_thread}] Enviando: {mensagem}")
    s.send(mensagem.encode())

    data = s.recv(1024)
    print(f"[Thread-{id_thread}] Resposta: {data.decode()}")
    s.close()

def main():
    inicio = time.time()
    threads = []
    operacoes = ["add", "subtract", "multiply", "divide"]

    for i in range(5):  # número de requisições
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        op = random.choice(operacoes)
        t = threading.Thread(target=fazer_requisicao, args=(num1, num2, op, i))
        threads.append(t)
        t.start()
        time.sleep(random.uniform(0.5, 1.5))  # simula tempo de envio diferente

    for t in threads:
        t.join()

    fim = time.time()
    print(f"Tempo total com threads no cliente: {fim - inicio:.2f} segundos")

if __name__ == "__main__":
    main()