from random import choice
from time import sleep

def pickKey(tam:int = 11) -> str:
    key: str = ""
    b_count: int = 0
    c: str = ""

    for x in range(tam - 3):
        if x == 4:
            key += "@"
        key += choice('acdefghizklmnopqrstuvxywzABCDEFGHIZKLMNOPQRSTUVXYWZ0123456789')
    return key + 'bbb'

print(" 11 <= entrada <= 256")
tam: int = int(input("Enter the Key: "))
key: str = ""

'''
264(tamanho do buffer) - len("FL4GiNyOUrMinD") + len("WiNAll")
o login que ter no mínimo 11 caracteres, com um @ na quinta posição ou login[4] e tem que ter 3 caracteres 'b', independentes de posição
'''

if tam >= 11 and tam <= 256:
    key = pickKey(tam)
    print("Key:", key)
else:
    print("Tamanho inválido.")
