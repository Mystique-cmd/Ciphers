import string
def generate_cipher_alphabet(keyword: str) -> str:
	k = keyword.upper()
	dedup = []
	for ch in k:
		if ch in string.ascii_uppercase and ch not in dedup:
			dedup.append(ch)
	remaining = [ch for ch in string.ascii_uppercase if ch not in dedup]
	return "".join(dedup + remaining)

def encrypt(message: str, cipher_alpha : str ) -> str:
	plain = string.ascii_uppercase
	table_upper = str.maketrans(plain, cipher_alpha)
	table_lower = str.maketrans(plain.lower(), cipher_alpha.lower())
	results = []
	for ch in message:
		if ch.isupper():
			results.append(ch.translate(table_upper))
		else:
			results.append(ch)
	return "".join(results)

def decrypt( ciphertext: str, cipher_alpha: str ) -> str:
	plain = string.ascii_uppercase
	table_lower = str.maketrans(cipher_alpha.lower(), plain.lower())
	table_upper = str.maketrans(cipher_alpha, plain)
	result = []
	for ch in ciphertext:
		if ch.isupper():
			result.append(ch.translate(table_upper))
		elif ch.islower():
			result.append(ch.translate(table_lower))
		else:
			result.append(ch)
	return "".join(result)

message_input = input( "Enter your message:")
kw = input("Enter your keyword:")
cipher_alpha = generate_cipher_alphabet(kw)

print("Do you want to encrypt or decrypt?")
choice = input(">>")
if choice =="encrypt":
	enc = encrypt(message_input,cipher_alpha)
	print(enc)
elif choice == "decrypt":g
	dec = decrypt( message_input, cipher_alpha)
	print(dec)
else:
	print ("Invalid Input")


"""
It is a monoalphabetic substitution cipher - this means that each letter in the  plaintext is replaced by exactly
one letter in the ciphertext, based on a custom alphabet build from the keyword
So this are the steps:
(i) Start by choosing a keyword
(ii)Build the cipher alphabet by removing all the duplicates on the keyword
(iii) Append the keyword to the alphabet
(iv) Now map the plaintext to the ciphertext.
"""
