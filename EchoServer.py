import socketserver
import sys

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('클라이언트 접속 : {0}'.format(self.client_address[0])) #클라이언트의 IP주소 출력
        sock=self.request

        rbuff=sock.recv(1024) #데이터 수신하고 그 결과를 rbuff에 담는다.
        received=str(rbuff,encoding='utf-8')
        print('수신 : {0}'.format(received))

        #return received data in same way
        sock.send(rbuff) #수신한 데이터를 그대로 클라이언트에게 송신한다.
        print('송신 : {0}'.format(received))
        sock.close()
        
if __name__=='__main__':
    if len(sys.argv)<2:
        print('{0} <Bind IP>'.format(sys.argv[0]))

    bindIP=sys.argv[1]
    bindPort=5425 #에코 서버는 5425 포트를 이용한다.

    server=socketserver.TCPServer((bindIP,bindPort),MyTCPHandler) #BaseRequestHandler를 상속한 클래스
    #TCPServer 생성자는 IP주소 문자열과 숫자 형식의 포트 번호로 이루어진 튜플을 매개변수로 받는다.

    print('메아리 서버 시작...')
    server.serve_forever() #클라이언트의 접속 요청을 받을 수 있다.