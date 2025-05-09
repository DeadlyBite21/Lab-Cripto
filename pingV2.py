from scapy.all import IP, ICMP, send

def enviar_mensaje(destino, mensaje):
    for caracter in mensaje:
        paquete = IP(dst=destino)/ICMP()/caracter.encode()
        send(paquete, verbose=False)
        print(f"Enviado: {caracter}")

def main():
    destino = input("Ingrese la IP de destino: ")
    mensaje = input("Ingrese el mensaje a enviar: ")
    enviar_mensaje(destino, mensaje)

if __name__ == "__main__":
    main()