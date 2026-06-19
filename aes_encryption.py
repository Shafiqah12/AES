# =============================================
# AES ENCRYPTION SIMULATION
# Name    : Shafiqah
# Project : Block Cipher (PRESENT, TWINE, AES)
# =============================================

# Install library
!pip install pycryptodome

# Import library yang diperlukan
from Crypto.Cipher import AES
import binascii

# ── INPUT ──────────────────────────────────
# Plaintext mesti tepat 16 aksara (128 bit)
plaintext = b'HiMyNameShafiqah'

# Kunci rahsia mesti tepat 16 aksara (128 bit)
key = b'CipherBlockAES26'

# ── ENCRYPTION ─────────────────────────────
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)

# ── PRINT RESULTS ──────────────────────────
print("=" * 45)
print("     AES ENCRYPTION SIMULATION")
print("     By: Shafiqah")
print("=" * 45)
print(f"Plaintext  : {plaintext.decode()}")
print(f"Key        : {key.decode()}")
print(f"Key Size   : {len(key) * 8} bits")
print(f"Block Size : {len(plaintext) * 8} bits")
print(f"Mode       : ECB")
print(f"Rounds     : 10")
print("-" * 45)
print(f"Ciphertext : {binascii.hexlify(ciphertext).decode().upper()}")

# ── DECRYPTION ─────────────────────────────
decipher = AES.new(key, AES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print(f"Decrypted  : {decrypted.decode()}")
print("=" * 45)

# ── AVALANCHE EFFECT TEST ──────────────────
# Tukar huruf pertama H kepada h (huruf kecil)
plaintext2 = b'hiMyNameShafiqah'
cipher2 = AES.new(key, AES.MODE_ECB)
ciphertext2 = cipher2.encrypt(plaintext2)

print("\n AVALANCHE EFFECT TEST")
print("-" * 45)
print(f"Original plaintext : HiMyNameShafiqah")
print(f"Modified plaintext : hiMyNameShafiqah")
print(f"(Only 1 character changed — H to h)")
print("-" * 45)
print(f"Original ciphertext : {binascii.hexlify(ciphertext).decode().upper()}")
print(f"Modified ciphertext : {binascii.hexlify(ciphertext2).decode().upper()}")
print("-" * 45)
print("Conclusion: Even 1 small change causes")
print("the ciphertext to change completely!")
print("This proves AES has a strong Avalanche Effect.")
print("=" * 45)
