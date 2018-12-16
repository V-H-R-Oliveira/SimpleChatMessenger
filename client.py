import socket
import datetime as dt

HOST = "127.0.0.1"
PORT = 8080

client = socket.socket()
client.connect((HOST, PORT))

firstDate = dt.datetime.now()
print('[{}:{}:{}/{}/{}/{}/{}/{}] Connected'.format(HOST, PORT, firstDate.day, firstDate.month, firstDate.year, firstDate.hour,
                                                   firstDate.minute, firstDate.second))

while True:
    try:
        conversa_client = input('Escreva algo: ')

        if conversa_client.lower() == 'sair':
            client.send(conversa_client.encode('utf-8'), 4096)
            client.close()
            break

        client.send(conversa_client.encode('utf-8'), 4096)
        receivedMsg = client.recv(4096).decode('utf-8')

        if receivedMsg.lower() == 'sair':
            client.close()
            break

        date = dt.datetime.now()

        print('[{}:{}:{}/{}/{}/{}/{}/{}] The received message was:'.format(HOST, PORT, date.day, date.month, date.year,
                                                                           date.hour, date.minute, date.second),
              receivedMsg)
    except (ConnectionError, ConnectionRefusedError, ConnectionAbortedError) as err:
        print('[{}:{}:{}/{}/{}/{}/{}/{}] Server Disconnected'.format(HOST, PORT, date.day, date.month, date.year,
                                                                           date.hour, date.minute, date.second))
        client.close()
        raise err
