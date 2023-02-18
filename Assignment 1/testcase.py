import unittest
from client import load_private_keys as clientPriKey, load_public_keys as clientPubKey
from server import load_private_keys as serverPriKey, load_public_keys as serverPubKey
import rsa
class TestClientServerCommunication(unittest.TestCase):
    def test_client(self):
        clientMessage = 'Hey, Server'
        # clientMessage = 'Something wrong'
        PubKey = clientPubKey()
        PriKey = serverPriKey()
        encryptMessage = rsa.encrypt(clientMessage.encode(), PubKey)
        decryptMessage = rsa.decrypt(encryptMessage, PriKey).decode()
        self.assertEqual(decryptMessage, 'Hey, Server')

    def test_server(self):
        serverMessage = 'Hey, Sai'
        # serverMessage = 'New me'
        PubKey = serverPubKey()
        PriKey = clientPriKey()
        encryptMessage = rsa.encrypt(serverMessage.encode(), PubKey)
        decryptMessage = rsa.decrypt(encryptMessage, PriKey).decode()
        self.assertEqual(decryptMessage, 'Hey, Client')

if __name__ == '__main__':
    unittest.main()