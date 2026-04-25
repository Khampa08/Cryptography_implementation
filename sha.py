import hashlib

def sha_hash():
    message = input("Enter message to hash: ").encode()
    hash_value = hashlib.sha256(message).hexdigest()
    print("SHA256 Hash:", hash_value)