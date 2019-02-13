#!/usr/bin/python
import sys
from socket import *
from uuid import getnode as get_mac


def sendeth(dst, eth_type, payload, interface = "eth0"):
  """Send raw Ethernet packet on interface."""

  mac = get_mac()
  addr = [("%012X" % mac)[i:i+2] for i in range(0, 12, 2)]
  addr2 = [chr(int(d,16)) for d in addr]
  addr3 = ''.join(addr2)

  s = socket(AF_PACKET, SOCK_RAW)

  # From the docs: "For raw packet
  # sockets the address is a tuple (ifname, proto [,pkttype [,hatype]])"
  s.bind(("eth0", 0))
  s.send(dst + addr3 + eth_type + payload)
  return


def parse_dir(dir_dst):
    """Converir la direccion destino a bytes"""

    dir = dir_dst.split(":")

    # Tiene que haber 6 bytes en la direccion
    try:
        assert(len(dir) == 6)
    except AssertionError:
        print("ERROR! Direccion destino incorrecta")
        sys.exit()

    #-- Cada byte esta formado por 2 digitos hexa correctos
    try:
      dir2 = [chr(int(d,16)) for d in dir]
    except ValueError:
      print("ERROR! Direccion destino incorrecta")
      sys.exit()

    #-- Convertir la direccion a cadena
    dir3 = ""
    for d in dir2:
      dir3 += d
    return dir3


if __name__ == "__main__":

  # Primer parametro: Direccion destino
  try:
      DIR_DST = sys.argv[1]
  except IndexError:
      # Direccion por defecto
      DIR_DST = "AA:BB:CC:DD:EE:FF"

  # Segundo parametro: mensaje
  try:
      msg = sys.argv[2]
  except IndexError:
      # Mensaje por defecto
      msg = "Testing--->"

  print("")
  print("Parametros: ")
  print(" Dir: %s " % DIR_DST)
  print(" Msg: %s" % msg)
  print("")

  #-- Calcular el relleno. Si la longitud es menor de 46 hay que meter
  #-- relleno
  padding = ""
  print("Longitud mensaje: %d" % len(msg))
  if len(msg) < 46:
      padding = "\x00"*(46 - len(msg))

  print("Longitud padding: %d" % len(padding))

  # Parsear la direccion. En caso de error se termina
  dst = parse_dir(DIR_DST)
  sendeth(dst,"\x7A\x05", msg+padding)
