import socket
import rsa

def load_private_keys():
    with open("Keys/ServerPrivateKey.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    return private_key

def load_public_keys():
    with open("Keys/ServerPublicKey.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    return public_key

def server_program(priKey, pubKey):
    host = socket.gethostname()  # get the hostname
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024)
        decryptMessage = rsa.decrypt(data, priKey).decode()

        if not data:
            break # if data is not received break

        print("from connected user: " + str(decryptMessage))
    
        msg = input(' Send Message, Server -> ')
        encryptMessage = rsa.encrypt(msg.encode(), pubKey)
        conn.send(encryptMessage)  # send data to the client

    conn.close()  # close the connection

if __name__ == '__main__':
    privateKey = load_private_keys()
    publicKey = load_public_keys()
    server_program(privateKey, publicKey)