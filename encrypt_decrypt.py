import rsa
from keygeneration import publicKey, privateKey

#Encrypting Message Function
def Encrypt(message):
    #Encrypting string with public key
    # encoding to byte string for the encryption
    encryptMessage = rsa.encrypt(message.encode(), publicKey)
    print("Original string: ", message)
    print("Encrypted string: ", encryptMessage)
    return encryptMessage

def Decrypt(msgToDecrypt):
    #Decrypting the message by private key 
    decryptMessage = rsa.decrypt(msgToDecrypt, privateKey).decode()
    print("decrypted string: ", decryptMessage)

