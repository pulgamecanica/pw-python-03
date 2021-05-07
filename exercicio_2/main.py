import analyze_folder
print("Welcome! This programm analizes any kind of file inside a folder.")
folder_name = analyze_folder.pede_pasta()
analyze_folder.guarda_resultados(folder_name)
def show_menu(folderName):
	while True:
		print("Options:")
		print("(1) - Open BAR Graph")
		print("(2) - Open PIE Graph")
		print("(0) - EXIT")
		user_input = int(input("Choose an option to continue: "))
		if user_input == 1:
			analyze_folder.faz_grafico_barras(folderName)
		elif user_input == 2:
			analyze_folder.faz_grafico_queijos(folderName)
		elif user_input == 0:
			break
		else:
			print("Invalid, please try again :(")
	print("ByeBye, Have a nice day")
show_menu(folder_name)