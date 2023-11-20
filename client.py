#this program runs on the remote PC controlling the Raspberry-Pi, this could by running MacOS (which I developed for), Windows, Linux or another Raspberry Pi
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("raspberrypi",5000))

while True:
    print(s.recv(1024).decode("utf-8"))