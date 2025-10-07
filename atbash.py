def encrypt_message(message):
    result = ''
    for item in message:
        if item.isalpha():
            if item.isupper():
              
                base = ord('A')
                result += chr(ord('Z') - (ord(item) - base))
            else:
               
                base = ord('a')
                result += chr(ord('z') - (ord(item) - base))
        else:
            
            result += item
    return result


def decrypt_message(encrypted_message):
   
    return encrypt_message(encrypted_message)


plaintext = input("Enter the plaintext: ")


ciphertext = encrypt_message(plaintext)
print("\nEncrypted text:", ciphertext)


decrypted = decrypt_message(ciphertext)
print("Decrypted text:", decrypted)
