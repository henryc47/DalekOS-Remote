#this program runs on the remote PC controlling the Raspberry-Pi, this could by running MacOS (which I developed for), Windows, Linux or another Raspberry Pi
import socket

def run_client():
    print("Connecting to client . . .")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #socket uses IPv4 IP addresses and TCP protocol
    client.connect(("raspberrypi",30701)) #connect socket to server on raspberrypi , port 30699
    while True:
        message = input("Enter Message: ")
        send_message(client,message)
        response = client.recv(1024)
        response = response.decode("utf-8")
        if response=='exited':
            break
        print("Server received : ",response)

    print("Server exited successfully")
    client.close()
        
        
def send_message(client,message):
    client.send(bytes(message,"utf-8"))


if __name__ == '__main__':
    run_client()
