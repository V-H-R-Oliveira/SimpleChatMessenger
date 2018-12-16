import socket
import datetime as dt

HOST = "127.0.0.1"
PORT = 8080

server = socket.socket()
addr = server.bind((HOST, PORT))
server.listen(5)

while True:
    firstDate = dt.datetime.now()
    print("[{}:{}:{}/{}/{}/{}/{}/{}] Listen ....".format(HOST, PORT, firstDate.day, firstDate.month, firstDate.year,
                                                         firstDate.hour, firstDate.minute, firstDate.second))

    try:
        client, address = server.accept()
        date = dt.datetime.now()

        print("[{}:{}:{}/{}/{}/{}/{}/{}] Received a connection from".format(HOST, PORT, date.day, date.month, date.year,
                                                         date.hour, date.minute, date.second), address)

        while True:
            receivedMsg = client.recv(4096).decode('utf-8')

            if receivedMsg.lower() == 'sair':
                server.close()
                break

            ct = dt.datetime.now()
            print('[{}:{}/{}/{}/{}/{}/{}] The received message was:'.format(address, ct.day, ct.month, ct.year,
                                                         ct.hour, ct.minute, ct.second), receivedMsg)

            conversar_server = input("Escreva algo: ")

            if conversar_server.lower() == 'sair':
                client.send(conversar_server.encode('utf-8'), 4096)
                server.close()
                break

            client.send(conversar_server.encode('utf-8'), 4096)
    except (KeyboardInterrupt, OSError) as err:
        finalDate = dt.datetime.now()
        print("[{}:{}:{}/{}/{}/{}/{}/{}] Saindo ...".format(HOST, PORT, finalDate.day, finalDate.month, finalDate.year,
                                                         finalDate.hour, finalDate.minute, finalDate.second))
        server.close()
        break
        #raise err