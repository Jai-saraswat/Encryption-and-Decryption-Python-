import random
# import base64
import pickle


def caesar_cipher(plaintext, shift):
    result = []
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return "".join(result)


def xor_cipher(plaintext):
    """
    Encrypts the plaintext using XOR encryption with a random key.
    Returns the encrypted text and the random key used.
    """
    # Generate a random key (1-byte integer between 1 and 255)
    key = 13
    # Encrypt the plaintext by XOR-ing each character with the key
    encrypted = [ord(char) ^ key for char in plaintext]
    return encrypted



def add_random_at_start(plaintext, n):
    random_string = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890", k=n))
    return random_string + plaintext

def add_random_at_end(plaintext, n):
    random_string = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890", k=n))
    return plaintext + random_string

def alternate(plaintext):
    all_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    return "".join([char + random.choice(all_chars) for char in plaintext])


def reverse_string(plaintext):
    return plaintext[::-1]


def random_word(plaintext, n):
    random_string = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890", k=n))
    words = plaintext.split()
    result = [word + f" {random_string}" for word in words]
    return " ".join(result), random_string

def word_repeats(plaintext, n):
    words = plaintext.split()
    return " ".join([" ".join([word] * n) for word in words])


# def convert_to_base64(plaintext):
#     byte_array=bytes(plaintext, encoding="utf-8")
#     encoded = base64.b64encode(byte_array).decode('utf-8')
#     return encoded


# 1.caesar_cipher()
# 2.alternate()
# 3.add_random_at_start()
# 4.add_random_at_end()
# 5reverse_string()
# 6.random_word()
# 7.word_repeats()
# 8.convert_to_base64()
# 9.xor_cipher()
def rnum():
    return random.randint(1,5)


def encryption(data):
    key1=[1,2,3,4,5,6,7]
    random.shuffle(key1)
    Key_for_encryption={}
    for i in key1:
        if i == 1:
            num=rnum()
            data=caesar_cipher(data,num)
            Key_for_encryption[1] = num
        if i==2:
            data=alternate(data)
            Key_for_encryption[2]=None
        elif i==3:
            num=rnum()
            data=add_random_at_start(data,num)
            Key_for_encryption[3] = num
        elif i==4:
            num=rnum()
            data=add_random_at_end(data,num)
            Key_for_encryption[4]=num
        elif i==5:
            data=reverse_string(data)
            Key_for_encryption[5]=None
        elif i==6:
            num=rnum()
            data, r_string=random_word(data,num)
            Key_for_encryption[6]=num,r_string
        elif i==7:
            num=rnum()
            data=word_repeats(data,num)
            Key_for_encryption[7]=num

    data=xor_cipher(data)
    return data,Key_for_encryption

x,key=encryption("Hello Duniya, Y@@eehhh!")

file = open("Encrypted.txt", "w+")
for i in x:
    file.write(str(i) + "\n")  # Convert integer to string and write to file
file.close()


file2=open("key.bin","wb")
pickle.dump(key,file2)
file2.close()
