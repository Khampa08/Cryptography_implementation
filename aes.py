from cryptography.fernet import Fernet

def aes_encrypt_decrypt():
    key = Fernet.generate_key()
    cipher = Fernet(key)

    message = input("Enter message to encrypt: ").encode()

    encrypted = cipher.encrypt(message)
    print("Encrypted:", encrypted)

    decrypted = cipher.decrypt(encrypted)
    print("Decrypted:", decrypted.decode())