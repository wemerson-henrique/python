# é proposto para ser executado em um drone


import socket, cv2, pickle, struct
import imutils
import threading
import cv2

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = '192.168.1.5' # entar com endereço de ip do drone
print("Host IP: ",host_ip)
port = 9999
socket_address = (host_ip,port)
server_socket.bind(socket_address)
server_socket.listen()
print("Escutando em",socket_address)

def start_video_stream():
    client_socket,addr = server_socket.accept()
    camera = False
    if camera == True:
        vid = cv2.VideoCapture(0)
    else:
        vid = cv2.VideoCapture('Videos/boat.mp4')
    try:
        print("CLIENTE {} CONECTADO.".format(addr))
        if client_socket:
            while(vid.isOpened()):
                img,frame = vid.read()

                frame = imutils.reasize(frame,width=320)
                a = pickle.dumps(frame)
                message = struct.pack("Q",len(a))+a 
                client_socket.sendall(message)
                cv2.imshow("transmintindo para o quech do servidor",frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    client_socket.close()
                    break
    except Exception as e:
        print(f"CACHE SERVER {addr} disconetado")
        pass
while True:
    start_video_stream()