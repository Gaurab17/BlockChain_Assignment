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
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    while message.lower().strip() != 'bye':
        encryptMessage = rsa.encrypt(message.encode(), pubKey)
        client_socket.send(encryptMessage)
       
        data = client_socket.recv(1024)  # receive response
        decryptMessage = rsa.decrypt(data, priKey).decode()
        print('Received from server: ' + str(decryptMessage)) 

        message = input("Again, enter message to send -> ")  # again take input

    client_socket.close()  # close the connection

if __name__ == '__main__':
    message = input(str("Enter message you want to send... \n"))
    publicKey = load_public_keys()
    privateKey = load_private_keys()
    client_program(message, publicKey, privateKey)
