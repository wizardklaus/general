import socket
import sys

if __name__=='__main__':

    if len(sys.argv)<4:
        print('{0} <Bind IP> <Server IP> <Message>'.format(sys.argv[0]))
        sys.exit()

    bindIP=sys.argv[1]
    serverIP=sys.argv[2]
    message=sys.argv[3]

    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM은 TCP socket을 의미한다.
    sock.bind((bindIP,0)) #포트를 0으로 지정하면 OS에서 임의의 번호로 포트를 할당해준다.

    try:
        sock.connect((serverIP,5425))
        #서버가 수신대기하고 있는 IP주소와 포트번호를 향해 연결 요청을 수행한다.

        sbuff=bytes(message,encoding='utf-8')
        sock.send(sbuff) #데이터를 담은 bytes 객체를 send() 메소드에 매개변수로 넘긴다.
        print('송신 : {0}'.format(message))

        rbuff=sock.resv(1024)
        #recv() 메소드는 수신할 데이터를 매개변수로 받아 상대방 노드로부터 데이터를 수신한다.
        #상대방 노드가 아니라 OS가 이미 상대방 노드로부터 OS버퍼에 받아놓은 데이터를 읽어온다.
        received=str(rbuff,encoding='utf-8')
        print('수신 : {0}'.format(received))

    finally:
        sock.close()