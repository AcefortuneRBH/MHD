from cryptography.fernet import Fernet

class EncryptionSecurity:
    def __init__(self):
        self.keys = {}

    def generate_key(self, user):
        key = Fernet.generate_key()
        self.keys[user] = key
        return key.decode()

    def encrypt_data(self, user, data):
        if user not in self.keys:
            return None
        f = Fernet(self.keys[user])
        return f.encrypt(data.encode()).decode()

    def decrypt_data(self, user, encrypted_data):
        if user not in self.keys:
            return None
        f = Fernet(self.keys[user])
        return f.decrypt(encrypted_data.encode()).decode()
