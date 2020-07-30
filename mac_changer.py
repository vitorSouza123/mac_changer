#!/usr/bin/env python
#Autor: Vitor Oliveira Souza
## Altera o endereço de MAC de determinada interface de rede.

#Bibliotecas
import subprocess
import optparse


#Argumentos
def mac_argumentos():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Alterar a interface de rede.")
    parser.add_option("-m", "--mac", dest="mac", help="Declarar o novo endereço MAC.")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-]Digite uma interface de rede. Digite --help para mais informações.")
    elif not options.mac:
        parser.error("Informe o novo mac. Digite --help para mais informações.")
    return parser.parse_args()


#Programa Principal
def new_mac(interface, mac):
    print("[*]Endereço mac alterado | Interface:",interface," | Novo mac:",mac)
    subprocess.call(["ifconfig",  interface, "down"])
    subprocess.call(["ifconfig", interface, "hw","ether", mac])
    subprocess.call(["ifconfig", interface, "up"])


options = mac_argumentos()
new_mac(options.interface, options.mac)