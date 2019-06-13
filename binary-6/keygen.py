from random import choice

def pickKey() -> str:
	index: int = 0
	key: str = ''
	while(index < 16):
		if index & 1 == 0:
			possible_1: str = choice('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
			possible_2: str = choice('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
			if ord(possible_2) - ord(possible_1) == -1:
				key += (possible_2 + possible_1)
				index += 2
			elif ord(possible_1) - ord(possible_2) == -1:
				key += (possible_1 + possible_2)
				index += 2
			else:
				continue
	return key

key: str = pickKey()
print("key:", key)
