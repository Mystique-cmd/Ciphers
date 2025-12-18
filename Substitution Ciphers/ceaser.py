def ceaser_cipher(text, shift, mode='encrypt'):
#shift(int):The number of positions to shift (key)
    result = "" 
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) %26 + base)
        else:
            #non-alphabetic characters are added unchanged
            result += char 
    return result

plaintext = input("Enter text: ")
shift = int(input("Enter shift (key): "))
mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

print("Plaintext:", plaintext)
print("Encrypted:", ceaser_cipher(plaintext, shift, mode='encrypt'))
print("Decrypted:", ceaser_cipher(ceaser_cipher(plaintext, shift, mode='encrypt'), shift, mode='decrypt'))
