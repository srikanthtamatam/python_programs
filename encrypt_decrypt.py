# encryption and decryption
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)

key = chars.copy()

random.shuffle(key)

#print(f"chars : {chars}")
#print(f"key : {key}")


# encryption
plain_text = input("enter the message you want to encrypt: ")
cipher_text  = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message is : {plain_text}")
print(f"encrypted message is : {cipher_text}")

# decryption
cipher_text1 = input("enter the message you want to decrypt : ")
plain_text1 = ""

for letter in cipher_text1:
    index = (key.index(letter))
    plain_text1 += chars[index]

print(f"Given encryped message is        : {cipher_text1}")
print(f"correspoding decryped message is : {plain_text1}")