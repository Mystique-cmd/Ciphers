def atbash(text:str) -> str:
    import string
    
    upper_in = string.ascii_uppercase
    upper_out = upper_in[::-1]
    lower_in = string.ascii_lowercase
    lower_out = lower_in[::-1]

    trans = str.maketrans(upper_in + lower_in, upper_out + lower_out)
    return text.translate(trans)

message = input("Enter a message to encode/decode with Atbash: ")
encoded = atbash(message)
print("Encoded/Decoded message:", encoded)  