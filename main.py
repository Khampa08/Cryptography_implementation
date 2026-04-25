from aes import aes_encrypt_decrypt
from rsa import rsa_encrypt_decrypt
from sha import sha_hash

while True:
    print("\n--- Cryptography Project ---")
    print("1. AES Encryption/Decryption")
    print("2. RSA Encryption/Decryption")
    print("3. SHA256 Hashing")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        aes_encrypt_decrypt()
    elif choice == "2":
        rsa_encrypt_decrypt()
    elif choice == "3":
        sha_hash()
    elif choice == "4":
        break
    else:
        print("Invalid choice")