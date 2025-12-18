import string
import random

def generate_substitution_key ():
	letters = list(string.ascii_lowercase)
	shuffled = letters.copy()
	random.shuffle(shuffled)
	return dict(zip(letters, shuffled))
	
def encrypt(message, key):
	encrypted = []
	for char in message.lower():
		if char in key:
			encrypted.append(key[char])
		else :
			encrypted.append(char)
	return ''.join(encrypted)
	
def decrypt(ciphertext, key):
	reverse_key = {v: k for k, v in key.items()}
	decrypted = []
	for char in ciphertext:
		if char in reverse_key:
			decrypted.append(reverse_key[char])
		else:
			decrypted.append(char)
	return ''.join(decrypted)
	
if __name__== "__main__":
	key = generate_substitution_key()
	print("substitution key:" ,key)
	
	message = input("Whats your message?")
	cipher = encrypt(message, key)
	print("Encrypted:" ,cipher)
	
	plain = decrypt(cipher, key)
	print ("Decrypted:", plain)
	
""" Here is how it works:
It replaces each letter of the plaintext with a different letter or symbol. The key to cipher is the mapping of each original letter to its substitute
Breakdown:
1. Both the sender and receiver agree on  the alphabet
2. A substitution key is created which is a permutation of the alphabet
3. Ecryption
4. Decryption
"""
