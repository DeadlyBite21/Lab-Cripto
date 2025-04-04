def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_offset = 65 if caracter.isupper() else 97
            nuevo_caracter = chr((ord(caracter) - ascii_offset + desplazamiento) % 26 + ascii_offset)
        else:
            nuevo_caracter = caracter
        resultado += nuevo_caracter
    return resultado

def main():
    texto = input("Ingrese el texto a cifrar: ")
    desplazamiento = int(input("Ingrese el desplazamiento: "))
    texto_cifrado = cifrar_cesar(texto, desplazamiento)
    print(f"Texto cifrado: {texto_cifrado}")

if __name__ == "__main__":
    main()
