from typing import Tuple

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
M = len(ALPHABET)

def egcd(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        return a,1,0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def modinv(a: int, m: int) -> int:
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}")
    return x % m

def affine_encrypt(text: str, a: int, b: int) -> str:
    if a % 2 == 0 or a % 13 == 0:
        raise ValueError("Key 'a' must be coprime to 26.")
    results = []
    for ch in text:
        if ch.isalpha():
            is_upper = ch.isupper()
            x = ord(ch.upper()) - ord('A')
            y = (a * x + b) % M
            enc = chr(y + ord('A'))
            results.append(enc if is_upper else enc.lower())
        else:
            results.append(ch)
    return ''.join(results)

def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
    a_inv = modinv(a, M)
    results = []
    for ch in ciphertext:
        if ch.isalpha():
            is_upper = ch.isupper()
            y = ord(ch.upper()) - ord('A')
            x = (a_inv * (y - b)) % M
            dec = chr(x + ord('A'))
            results.append(dec if is_upper else dec.lower())
        else:
            results.append(ch)
    return ''.join(results)

input_text = input("Enter text: ")
a = int(input("Enter key 'a' (must be coprime to 26): "))
b = int(input("Enter key 'b': "))
encrypted = affine_encrypt(input_text, a, b)
print(f"Encrypted: {encrypted}")
decrypted = affine_decrypt(encrypted, a, b)
print(f"Decrypted: {decrypted}")

"""
-affine is a mathematical way to scramble the letters
-the cipher uses two keys(numbers), a and b
-a is the multiplier and b is the shift
-the encryption formula is E(x) = (a*x + b)  26
-the decryption formula is D(y) = a^-1 * (y - b)  26
-where x is the plaintext and y is the ciphertext and a^-1 is the modular inverse of a mod 26
"""