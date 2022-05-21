try: import pyautogui
except: print("Erro: import pyautogui")
try: import cv2 #as cv
except: print("Erro: import cv2 as cv")
try: import numpy as np
except: print("Erro: import numpy as np")
try: from PIL import ImageGrab
except: print("Erro: from datetime import datetime")

import socket, pickle, struct


# cv2.namedWindow("Transmitindo tela", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Transmitindo tela",480,270)

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("HOST IP", host_ip)
port = 9999
socket_address = (host_ip,port)
server_socket.bind(socket_address)
server_socket.listen(5)
print("Escutando em:",socket_address)



while(True):
    client_socket,addr = server_socket.accept()
    print("pegar coneção de",addr)
    
    if client_socket:
        vid = cv2.VideoCapture(0)
        while(vid.isOpened()):
            # img = pyautogui.screenshot()
            # img = ImageGrab.grab()
            # frame = np.array(img)
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.cvtColor(np.array(ImageGrab.grab()), cv2.COLOR_BGR2RGB)

            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a 
            client_socket.sendall(message)
            # cv2.imshow("Transmitindo tela",frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()

