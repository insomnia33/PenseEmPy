fin = open("words.txt")
for line in fin:
	i = 0
	while (line[i] != "e"):
		word = line.strip()
		print(word)