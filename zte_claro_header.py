#!/usr/bin/env python3
#
# https://github.com/ldamasceno38/zte_claro_header
# 
# Corrige os bytes no header do arquivo .bin após editar o .xml e encodar novamente com zte_config_utility
#
# Valido apenas para ZTE F6645P e ZTE F6600P da Claro Fibra
#
#
import os
import sys
import argparse

def editar_header_arquivo(caminho_arquivo):
    try:
        if not os.path.exists(caminho_arquivo) or not os.path.isfile(caminho_arquivo):
            return False
        
        with open(caminho_arquivo, 'rb') as arquivo:
            dados = bytearray(arquivo.read())
        
        if len(dados) < 154:
            return False
        
        with open(caminho_arquivo + ".backup", 'wb') as backup:
            backup.write(dados)
        
        dados[0x40] = 0x02
        dados[0x99] = 0x06
        
        with open(caminho_arquivo, 'wb') as arquivo:
            arquivo.write(dados)
        
        return True
        
    except:
        return False

def parse_arguments():
    parser = argparse.ArgumentParser(description="CLARO F6600P / F6645P Header Fix")
    parser.add_argument('--bin', required=True, metavar='FILE', help='Arquivo .bin para editar')
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    if editar_header_arquivo(args.bin):
        print("Success")
        sys.exit(0)
    else:
        print("Fail")
        sys.exit(1)

if __name__ == "__main__":
    main()