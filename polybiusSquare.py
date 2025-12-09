class PolybiusSquare:
    def __init__(self):
        self.square = [
        ["A","B","C","D","E"],
        ["F","G","H","I/J","K"],
        ["L","M","N","O","P"],
        ["Q","R","S","T","U"],
        ["V","W","X","Y","Z"]
        ]

        self.encode_dict = {}
        self.decode_dict = {}

        for row in range(5):
            for col in range(5):
                val = self.square[row][col]
                code = f"{row+1}{col+1}"

                if val == "I/J":
                    self.encode_dict["I"] = code
                    self.encode_dict["J"] = code
                    self.decode_dict[code] = "I/J"
                else:
                    self.encode_dict[val]=code
                    self.decode_dict[code]=val

    def encrypt(self, message: str) -> str:
        message = message.upper()
        ciphertext = []
        for char in message:
            if char in self.encode_dict:
                ciphertext.append(self.encode_dict[char])
            elif char == " ":
                ciphertext.append(" ")
        return " ".join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        plaintext = []
        for code in ciphertext.split():
            if code in self.decode_dict:
                plaintext.append(self.decode_dict[code])
            elif code == " ":
                plaintext.append(" ")
        return "".join(plaintext)


cipher = PolybiusSquare()
msg = input("Enter the message:")
enc = cipher.encrypt(msg)

print("Encrypted:",enc)

"""
This is how it works :
Each letter is mapped to a row+column  pair. and I and J share the same code.The rows
and columns are labelled 1 to 5 thus concatenation of this labels is what forms the numbers
"""