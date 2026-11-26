# Encryption and Decryption
text = input("Enter a message: ")
key = int(input("Enter key: "))

# Encryption
encrypted = ""

for ch in text:
    encrypted = chr(ord(ch) + key)

print("Encrypted message:", encrypted)

# Decryption
decrypted = ""

for ch in encrypted:
    decrypted = decrypted + chr(ord(ch) - key)

print("Decrypted message:", decrypted)







