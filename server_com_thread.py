from socket import *
from constCS import *
import threading

def calcular(operação, num1, num2):
    if operação == "add":
        return num1 + num2
    elif operação == "subtract":
        return num1 - num2
    elif operação == "multiply":
        return num1 * num2
    elif operação == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Erro: Operação inválida!"

def handle_client(conn, addr):
    print(f"Conectado com {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        mensagem = data.decode()
        print(f"Mensagem recebida de {addr}: {mensagem}")
        partes = mensagem.split()

        if len(partes) == 3:
            try:
                num1 = float(partes[0])
                num2 = float(partes[1])
                operação = partes[2]
                resultado = calcular(operação, num1, num2)
                resposta = f"O resultado de {num1} {operação} {num2} é: {resultado}"
            except ValueError:
                resposta = "Erro: Entrada inválida! Certifique-se de enviar dois números seguidos da operação."
        else:
            resposta = mensagem + "*"

        conn.send(resposta.encode())
    conn.close()
    print(f"Conexão encerrada com {addr}")

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
print("Servidor aguardando conexões...")

while True:
    conn, addr = s.accept()
    t = threading.Thread(target=handle_client, args=(conn, addr))
    t.start()