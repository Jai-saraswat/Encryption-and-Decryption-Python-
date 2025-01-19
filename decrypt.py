import pickle
import base64

def decrypt_word_repeats(encrypted_text, n):
    words = encrypted_text.split()
    return " ".join(words[::n])


def decrypt_reverse_string(plaintext):
    return plaintext[::-1]

def decrypt_alternate(encrypted_text):
    return encrypted_text[::2]

def decrypt_random_word(encrypted_text, random_string, n):
    words = encrypted_text.split()
    return " ".join([word for word in words if word != random_string])

def decrypt_random_at_start(encrypted_text, n):
    return encrypted_text[n:]

def decrypt_random_at_end(encrypted_text, n):
    return encrypted_text[:-n]


def decrypt_xor_cipher(encrypted_list, key=13):
    return "".join([chr(int(num) ^ key) for num in encrypted_list])


# def decrypt_from_base64(encoded_text):
#     byte_array = base64.b64decode(encoded_text)
#     decoded = byte_array.decode('utf-8')
#     return decoded

def decrypt_caesar_cipher(encrypted_text, shift):
    result = []
    for char in encrypted_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return "".join(result)



def decryption():
    file = open("Encrypted.txt", 'r')
    list1 = []
    x = file.readlines()
    for i in x:
        y = i.split("\n")
        list1.append(y[0])
    with open("Key.bin", "rb") as file:
        key = pickle.load(file)
    data=list1
    data=decrypt_xor_cipher(data)
    print(data)
    # print(key)
    #data=decrypt_from_base64(data)
    key=dict(reversed(list(key.items())))
    for i in key:
        if i == 1:
            data=decrypt_caesar_cipher(data,key[i])
        elif i==2:
            data=decrypt_alternate(data)
        elif i==3:
            data=decrypt_random_at_start(data,key[i])
        elif i==4:
            data=decrypt_random_at_end(data,key[i])
        elif i==5:
            data=decrypt_reverse_string(data)
        elif i==6:
            # print(data)
            # print(key[i][1],key[i][0])
            data=decrypt_random_word(data,key[i][1],key[i][0])
            # print(data)
        elif i==7:
            # print(data)
            data=decrypt_word_repeats(data,key[i])
            # print(data)
    return data



x=decryption()
print(x)