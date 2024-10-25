import string

message = "Hello"
alphabet = string.ascii_uppercase

print(alphabet)
encrypted_message = ""
for char in message.upper():
    if char.isalpha():
        poz = (alphabet.index(char) + 5) % 26
        encrypted_message += alphabet[poz]
    else:
        encrypted_message += char


decrypted_message = ""
for i in range(len(encrypted_message)):
    char = encrypted_message[i]
    if message[i].isalpha():
        original_pos = (alphabet.index(char) - 5) % 26
        decrypted_char = alphabet[original_pos]
        if message[i].islower():
            decrypted_message += decrypted_char.lower()
        else:
            decrypted_message += decrypted_char
    else:
        decrypted_message += char


print("Message original :", message)
print("Message crypté :", encrypted_message)
print("Message décrypté :", decrypted_message)
