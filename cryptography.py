from cryptography.fernet import Fernet
import os 

class SecureFile: 
    def __init__(self, filename, key=None): 
        self.filename = filename
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)
        
        
        self._encryption_mode = True
        
    def encrypt_and_write(self, plaintext: str):
        if not isinstance(plaintext, str): 
            raise TypeError("Plain Text Must be String")
        
        encrypted_data = self.cipher.encrypt(plaintext.encode('utf-8'))
        with open(self.filename, 'wb') as f: 
            f.write(encrypted_data)
            
            
    def read_and_decrypt(self) -> str: 
        if not os.path.exists(self.filename): 
            raise FileNotFoundError(f"File not found: {self.filename}")
        
        with open(self.filename, 'rb') as f: 
            encrypted_data = f.read()
            
            
            return self.cipher.decrypt(encrypted_data).decode('utf-8')
            
            
    def write_plaintext(self, plaintext: str): 
        raise PermissionError("Direct Plaintext permission is not allowed. Use encrypt_and_write().")
    
    
    def get_key(self) -> bytes: 
        
        return self.key
    
    
    
secure = SecureFile("secret_data.bin")
secure.encrypt_and_write("This is a top secret Message")
print(secure.read_and_decrypt())


try: 
    secure.write_plaintext("This should fail.")
except PermissionError as e: 
    print("Error:", e)
        
