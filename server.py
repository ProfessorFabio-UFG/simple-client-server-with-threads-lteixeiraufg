# from socket  import *
# from constCS import * #-

# s = socket(AF_INET, SOCK_STREAM) 
# s.bind((HOST, PORT))  #-
# s.listen(1)           #-
# (conn, addr) = s.accept()  # returns new socket and addr. client 
# while True:                # forever
#   data = conn.recv(1024)   # receive data from client
#   if not data: break       # stop if client stopped
#   print(bytes.decode(data))
#   conn.send(str.encode(bytes.decode(data)+"*")) # return sent data plus an "*"
# conn.close()               # close the connection

from socket import *
from constCS import *  #-

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 

# Função de calculadora
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

while True:                # forever
    data = conn.recv(1024)   # receive data from client
    if not data: break       # stop if client stopped
    
    mensagem = bytes.decode(data)  
    print(f"Mensagem recebida: {mensagem}")
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
        resposta = bytes.decode(data) + "*"
    
    conn.send(str.encode(resposta))

conn.close()               # close the connection