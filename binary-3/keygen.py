from random import choice

def pickKey() -> str:
	key: str = ""
	for x in range(16):
		key += choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789')
	return key

def calculaVerificador(key: str) -> int:
	calc = 0
	for i in range(len(key) - 1):
		calc = (calc + ord(key[i]) >> 1) % 0xf00 + 10
	return calc

key: str = ""
verificador: int = 0

while True:
	key = pickKey()
	verificador = calculaVerificador(key)
	if verificador == ord(key[len(key) - 1]):
		print("Key:", key)
		break
