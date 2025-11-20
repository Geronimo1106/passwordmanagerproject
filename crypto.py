import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KDF_ITERATIONS = 200_000
SALT_SIZE = 16
AES_KEY_SIZE = 32
NONCE_SIZE = 12

def derive_key(password: str, salt: bytes) -> bytes:
    password_bytes = password.encode('utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=AES_KEY_SIZE,
        salt=salt,
        iterations=KDF_ITERATIONS,
    )
    return kdf.derive(password_bytes)

def encrypt_entry(key: bytes, plaintext: str) -> (bytes, bytes):
    aesgcm = AESGCM(key)
    nonce = os.urandom(NONCE_SIZE)
    ct = aesgcm.encrypt(nonce, plaintext.encode('utf-8'), associated_data=None)
    return nonce, ct

def decrypt_entry(key: bytes, nonce: bytes, ciphertext: bytes) -> str:
    aesgcm = AESGCM(key)
    pt = aesgcm.decrypt(nonce, ciphertext, associated_data=None)
    return pt.decode('utf-8')

