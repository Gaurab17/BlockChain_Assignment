import socket
import rsa

def load_public_keys():
    with open("Keys/ClientPublicKey.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    return public_key

def load_private_keys():
    with open("Keys/ClientPrivateKey.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    return private_key

def client_program(message, pubKey, priKey):
    host = socket.gethostname()  
    port = 5001  # socket server port number

    client_socket = socket.socket()  # instantiate
     # connect to the server
    client_socket.connect((host, port)) 

    while message.lower().strip() != 'bye':
        encryptMessage = rsa.encrypt(message.encode(), pubKey)
        client_socket.send(encryptMessage)
       
        data = client_socket.recv(1024)  # receive response
        decryptMessage = rsa.decrypt(data, priKey).decode()
        print('Server: ' + str(decryptMessage)) 

         # again take input
        message = input("Send Message, Client ->") 

    client_socket.close()  # close the connection
    return message

if __name__ == '__main__':
    message = input(str("Enter message you want to send... \n"))
    publicKey = load_public_keys()
    privateKey = load_private_keys()
    client_program(message, publicKey, privateKey)
