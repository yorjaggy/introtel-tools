def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

default_shift = 2
shift_amount = int(input("Ingrese un numero para rotar:") or default_shift)
plain_text = input("Ingrese un texto:")
cipher_text = caesar_cipher(plain_text, shift_amount)

print("Texto Plano:", plain_text)
print("Texto Cifrado:", cipher_text)