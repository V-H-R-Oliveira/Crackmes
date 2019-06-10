from random import choice

def pickKey() -> str:
	key: str = "@"
	for x in range(1, 4):
		key += choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	key += "-"
	for x in range(5, 9):
			key += choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	return key

key: str = pickKey()
print("Key:", key)
