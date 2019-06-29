from random import choice

def pickKey() -> str:
	key: str = ""
	for i in range(9):
		key += choice('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	return key

offset: int = 990
soma: int = 0
key: str = ""

while True:
	if soma == offset:
		print("Key:", key)
		break
	else:
		soma = 0
		key = pickKey()
		for x in key:
			soma += ord(x)

