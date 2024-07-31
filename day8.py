### Caesar Cipher (dia bisa encode decode a secret message gt)

def encrypt(pesan,geser) :
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text2 = []
    shifted_text = []
    for i in pesan : #cari indexnya per huruf
        shifted_index = (alphabet.index(i) + geser) % len(alphabet) #aku nyontek gpt ini cuma penulisannya dan logika
        text2.append(shifted_index)
    for j in text2 :
        go = alphabet[j]
        shifted_text.append(go)
    final_encode = "".join(shifted_text)
    print(f"To encode, you input : {final_encode}\n with the shift : {geser}")
def decrypt(pesan,geser) :
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text2 = []
    shifted_text = []
    for i in pesan : #cari indexnya per huruf
        shifted_index = (alphabet.index(i) - geser) % len(alphabet) 
        text2.append(shifted_index)
    for j in text2 :
        go = alphabet[j]
        shifted_text.append(go)
    final_decode = "".join(shifted_text)
    print(f"Here's you decode message {final_decode}\n with the shift : {geser}")



while True :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" :
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(pesan=text,geser=shift)
        continue
    elif direction == "decode" :
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(pesan=text,geser=shift)
        continue
    elif direction != "encode" and direction != "decode":
        break
    else :
        break

def caesar (pesan,geser,direction):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text2 = []
    shifted_text = []
    if direction == "encode" :
        for i in pesan : #cari indexnya per huruf
            shifted_index = (alphabet.index(i) + geser) % len(alphabet) #aku nyontek gpt ini cuma penulisannya dan logika
            text2.append(shifted_index)
        for j in text2 :
            go = alphabet[j]
            shifted_text.append(go)
        final_encode = "".join(shifted_text)
        print(f"To encode, you input : {final_encode}\n with the shift : {geser}")
    elif direction == "decode" :
        for i in pesan : #cari indexnya per huruf
            shifted_index = (alphabet.index(i) - geser) % len(alphabet) 
            text2.append(shifted_index)
        for j in text2 :
            go = alphabet[j]
            shifted_text.append(go)
        final_decode = "".join(shifted_text)
        print(f"Here's you decode message {final_decode}\n with the shift : {geser}")
    else :
        pass
        