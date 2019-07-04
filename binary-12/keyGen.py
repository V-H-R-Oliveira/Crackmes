def keyGen(username: str) -> str:
	sum1, c1, key = 0, 0, ""

	for char in username:
		sum1 += ord(char)

	for i in range(9):
		c1 = sum1 // (len(username) + i)
		key += chr(c1)
		sum1 += (sum1 // c1)
	return key

username: str = input("Digite o seu nome: ")
key: str = keyGen(username)
print("Key:", key)
