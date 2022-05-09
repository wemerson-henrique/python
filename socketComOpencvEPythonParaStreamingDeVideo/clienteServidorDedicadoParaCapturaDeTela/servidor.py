try: from PIL import ImageGrab
except: print("ERRO: import pillow")
try: import cv2
except: print("ERRO: import cv2")
try: import numpy as np
except: print("ERRO: import numpy")
import socket, pickle, struct

from numpy import block

#Criando soket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("HOST IP", host_ip)
port = 9999
socket_address = (host_ip,port)

#Socket Bind
server_socket.bind(socket_address)

# Escutando socket
server_socket.listen(5)
print("Escutando em:",socket_address)

#Socket Accept
while True:
    client_socket,addr = server_socket.accept()
    print("pegar coneção de",addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a 
            client_socket.sendall(message)
            cv2.imshow("Transmitindo o video",frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()
# while True:
#     img = ImageGrab.grab()
#     frame = np.array(img)
#     # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#     cv2.imshow('frame',frame)
#     key = cv2.waitKey(1) & 0xFF
#     if key == ord('q'):
#         break
# cv2.destroyAllWindows()