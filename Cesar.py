import string
def generate_key(n):
    letters = string.ascii_lowercase+string.punctuation+string.ascii_uppercase+string.digits
    key = {}
    cnt = 0
    for c in letters:
        key[c] = letters[(cnt+n) % len(letters)]
        cnt += 1
    return key

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

def get_decryption_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey

def decrypt(key, cipher):
    plain = ""
    for c in cipher:
        if c in key:
            letter =key[c]
            plain += key[c]
        else:
            plain += c
    return plain

def bruteForce(dkey, cipher):
    count = 94
    for i in range(94):
        dkey = generate_key(i)
        message =encrypt(dkey, cipher)
        print(f"key{count}: {message}")
        count -= 1
