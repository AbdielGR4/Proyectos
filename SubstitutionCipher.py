import random
import string

def generate_key():
    letters = string.ascii_lowercase
    ComLetters= list(letters)
    key = {}
    for c in letters:
        key[c] = ComLetters.pop(random.randint(0, len(ComLetters)-1))
    return key

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += " "
    return cipher

def decrypt(dkey, cipher):
    plain = ""
    for c in cipher:
        if c in dkey:
            plain += dkey[c]
        else:
            plain += " "
    return plain

def dkey(key):
    dkey = {}
    for i in key:
        dkey[key[i]] = i
    return dkey

