import os
def pede_nome():
	while True:
		fileName = input("Please Enter the file name: ");
		if fileName.split(".")[-1] != "txt":
			print("The file should be a '.txt' file!")
			continue
		if not os.path.exists(fileName):
			print(f"The file '{fileName}' doesn't exists")
			continue
		else:
			return fileName
def gera_nome():
	return pede_nome().replace(".txt", ",json")