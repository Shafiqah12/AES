from Crypto.Cipher import AES
import binascii

key       = b'mysecretkey1234!'  # 16 characters ✅
plaintext = b'HiMyNameShafiqah'  # 16 characters ✅

# Encrypt
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
print("Plaintext  :", plaintext.decode())
print("Key        :", key.decode())
print("Ciphertext :", binascii.hexlify(ciphertext).decode().upper())

# Decrypt
decipher = AES.new(key, AES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted  :", decrypted.decode())

# Avalanche Effect — change H to h
plaintext2 = b'hiMyNameShafiqah'  # changed capital H to small h
cipher2 = AES.new(key, AES.MODE_ECB)
ciphertext2 = cipher2.encrypt(plaintext2)
print("\n--- Avalanche Effect ---")
print("Original  :", binascii.hexlify(ciphertext).decode().upper())
print("Modified  :", binascii.hexlify(ciphertext2).decode().upper())
