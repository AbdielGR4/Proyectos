import random
import secrets
import string

def generar_mensaje():
    while True:

        mensaje = input("Ingrese un mensaje: ")
        if mensaje.isalpha():
            return mensaje
        else:
            print("Por favor, ingrese solo letras. Inténtelo de nuevo.")

    return mensaje

mensaje = generar_mensaje()

def generar_llave(mensaje):
    abecedario = list(string.ascii_lowercase)
    numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]  # Lista de números primos
    simbolos = ['@', '$', '^', '&', '*', '(', ')', '_', '+', ':', '£', '?', '~']

    combined = abecedario + numeros_primos + simbolos
    random.shuffle(combined)

    semilla = [secrets.randbelow(37) for _ in range(500)]
    subset = random.sample(semilla, len(mensaje))

    llave = [combined[index] for index in subset]
    llave = [str(item) for item in llave]  # Convertir los elementos de la lista a cadenas

    return ''.join(llave)

def encriptar(llave, mensaje):
    ciphertext = ""
    for i in range(len(mensaje)):
        t = mensaje[i]
        k = llave[i % len(llave)]
        x = ord(k) ^ ord(t)
        ciphertext += chr(x)
    return ciphertext.encode("utf-8").hex()

def desencriptar(llave, ciphertext):
    a_string = bytes.fromhex(ciphertext)
    a_string = a_string.decode("utf-8")
    mensaje = ""
    for i in range(len(a_string)):
        t = a_string[i]
        k = llave[i % len(llave)]
        x = ord(k) ^ ord(t)
        mensaje += chr(x)
    return mensaje

def mostrar_datos(llave,ciphertext):
    print("Mensaje original:", mensaje)
    print("Llave:", llave)
    print("Ciphertext:", ciphertext)
    print("Mensaje desencriptado:", desencriptar(llave, ciphertext))

llave = generar_llave(mensaje)
ciphertext = encriptar(llave, mensaje)

mostrar_datos(llave,ciphertext)
