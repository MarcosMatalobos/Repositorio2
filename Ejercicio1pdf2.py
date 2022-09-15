#-------------------------------------------------------------------------------
# Name:        module7
# Purpose:
#
# Author:      Administrator
#
# Created:     15/09/2022
# Copyright:   (c) Administrator 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a = int(input ("Por favor ingrese numero impar: "))
    while a % 2 == 0:
        a = int(input ("Por favor ingrese numero impar"))
    print("Es un Numero Impar")

if __name__ == '__main__':
    main()
