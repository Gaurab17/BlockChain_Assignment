import rsa

def generateKeysForServerToClientMsg():
    public_key_Server, private_key_Client = rsa.newkeys(1024)
    with open("Keys/ServerPublicKey.pem","wb") as f:
        f.write(public_key_Server.save_pkcs1("PEM"))

    with open("Keys/ClientPrivateKey.pem","wb") as f:
        f.write(private_key_Client.save_pkcs1("PEM"))

def generateKeysForClientToServerMsg():
    public_key_Client, private_key_Server = rsa.newkeys(1024)
    with open("Keys/ClientPublicKey.pem","wb") as f:
        f.write(public_key_Client.save_pkcs1("PEM"))

    with open("Keys/ServerPrivateKey.pem","wb") as f:
        f.write(private_key_Server.save_pkcs1("PEM"))

generateKeysForServerToClientMsg()
generateKeysForClientToServerMsg()