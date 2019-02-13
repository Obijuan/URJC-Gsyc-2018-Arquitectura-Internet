#!/usr/bin/python
from uuid import getnode as get_mac
from socket import *
import sys

def get_str_mac():
    """Obtener la direccion fisica de la maquina, y devolverla
       en formato de cadena para mostrarla"""
    mac = get_mac()
    addr = [("%012X" % mac)[i:i+2] for i in range(0, 12, 2)]
    addr2 = [chr(int(d,16)) for d in addr]
    addr3 = ':'.join(addr)
    return addr3


def mac_bin2str(mac):
    """Converir la direccion de bytes a cadena de caracteres"""
    a_dst = []
    for b in mac:
        a_dst.append("%02X" % ord(b))

    dst = ":".join(a_dst)
    return dst


def prot2str(prot):
    """Convertir los bytes del protocolo a cadena"""
    a_dst = []
    for b in prot:
        a_dst.append("%02X" % ord(b))

        dst = "".join(a_dst)
    return dst

def data2ascii(data):
    ascii  = ""
    for d in data:
        if ord(d)>=32 and ord(d)<127:
            ascii += d
        else:
            ascii += '.'
    return ascii


if __name__ == "__main__":
    print("Paquetes recibidos en esta maquina")
    mymac = get_str_mac()
    print("Direccion Ethernet local: " + mymac)
    print("")

    s = socket(AF_PACKET, SOCK_RAW, htons(3))
    s.bind(("eth0", 3))

    print("Esperando tramas por el interfaz eth0....")
    print("")

    while(True):

        # Esperar a que llegue una trama
        try:
            frame = s.recv(65535)
        except KeyboardInterrupt:
            print("Fin")
            sys.exit();

        # Leer la direccion destino de la trama
        dst = mac_bin2str(frame[0:6])

        # Si la trama es para esta maquina (o broacast) la procesamos...
        if (dst == mymac or dst == "FF:FF:FF:FF:FF:FF"):
            print("-----------------------------------------------------")
            print("Desde               bytes   data")

            src = mac_bin2str(frame[6:12])
            datalen = len(frame[14:])
            data = data2ascii(frame[14:])
            # Recortar los datos si son muchos
            if len(data) > 20:
                data = data[0:20]
            print("%s     %d    %s" % (src, datalen, data))
