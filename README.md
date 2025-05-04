Foi copiada a última tarefa (nela eu fiz uma calculadora), aqui apenas adicionei o uso de threads mesmo.
Logo, o que foi adicionado foram os arquivos client_com_thread.py e server_com_thread.py

!!!!!!!!!!!!!!!!!!!!!!

TAREFA: https://github.com/ProfessorFabio-UFG/simple-client-server-with-threads-lteixeiraufg.git

OBS DE COMPARAÇÃO:
a)  Threads apenas no servidor:
Neste caso, o servidor consegue atender várias conexões simultaneamente, mas como o cliente envia as requisições em sequência, o processamento ainda ocorre uma requisição por vez. Então, o tempo total de execução continua alto, pois o cliente se torna o gargalo do processo.

b) Threads no cliente e no servidor:
Aqui, tanto o cliente quanto o servidor usam threads, permitindo que várias requisições sejam enviadas e processadas ao mesmo tempo. Com isso, o tempo total de execução cai drasticamente, já que todas as requisições são tratadas em paralelo, aproveitando o máximo do desempenho do modelo cliente-servidor com multithreading.
