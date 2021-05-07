import os
def calcula_linhas(fileName):
	if not os.path.exists(fileName):
		print(f"The file {fileName} doesn't exists")
	else:
		f = open(fileName, "r")
		return len(f.readlines())
def calcula_carateres(fileName):
	if not os.path.exists(fileName):
		print(f"The file {fileName} doesn't exists")
	else:
		f = open(fileName, "r")
		return len(f.read())
def calcula_palavra_comprida(fileName):
	if not os.path.exists(fileName):
		print(f"The file {fileName} doesn't exists")
	else:
		f = open(fileName, "r")
		wordArray = f.read().split()
		winnerWord = ""
		for word in wordArray:
			if len(word) > len(winnerWord):
				winnerWord = word
		return winnerWord

def calcula_ocorrencia_de_letras(fileName):
	if not os.path.exists(fileName):
		print(f"The file {fileName} doesn't exists")
	else:
		f = open(fileName, "r")
		wordArray = f.read().lower()
		dictionary = {}
		for word in wordArray:
			if word in dictionary:
				dictionary[word] += 1
			else:
				dictionary[word] = 1
		return dictionary
print(calcula_palavra_comprida("lorem.txt"))