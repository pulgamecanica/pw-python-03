# os.getcwd(), os.listdir(), os.path.isfile(), os.path.isdir().
import os
def pede_pasta():
	while True:
		folderName = input("Please Enter the folder name: ");
		if not os.path.isdir(folderName):
			print(f"The folder '{folderName}' doesn't exists")
			continue
		else:
			return folderName
def calcula_tamanho_pasta(folderName):
	size = 0;
	for element in os.listdir(folderName):
		if os.path.isdir(folderName + "/" + element):
			size += calcula_tamanho_pasta(folderName + "/" + element)
		elif os.path.isfile(folderName + "/" + element):
			size += os.path.getsize(folderName + "/" +(element)) / 1024
	print("Total size of '", folderName, "' is: ", size, "[kBytes]")
	return size
print("*"*20, "\nThe Folder TOTAL Size is: ", calcula_tamanho_pasta(pede_pasta()), "[kBytes].\n", "*"*20)
