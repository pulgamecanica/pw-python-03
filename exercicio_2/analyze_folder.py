# os.getcwd(), os.listdir(), os.path.isfile(), os.path.isdir().
import os
import csv
import numpy as np
from matplotlib import pyplot as plt
def pede_pasta():
	while True:
		folderName = input("Please Enter the folder name: ");
		if not os.path.isdir(folderName):
			print(f"The folder '{folderName}' doesn't exists")
			continue
		else:
			return folderName
def faz_calculos(folderName):
	dict_info = {}
	for file in os.listdir(folderName):
		if os.path.isdir(folderName + "/" + file):
			continue
		if file.split(".")[-1] in dict_info:
			fileExtension = file.split(".")[-1]
			(dict_info[fileExtension])["volume"] += os.path.getsize(folderName+"/"+(file)) / 1024
			(dict_info[fileExtension])["quantity"] += 1
		else:
			dict_info[file.split(".")[-1]] = {"volume": os.path.getsize(folderName+"/"+(file)) / 1024,"quantity": 1}
	return dict_info
def guarda_resultados(folderName):
	dict_info = faz_calculos(folderName)
	with open(folderName+'.csv', 'w', newline='') as ficheiro:
		fields = ["Extension", "Volume", "Quantity"]
		writer =  csv.DictWriter(ficheiro, fieldnames=fields)
		writer.writeheader()
		for key, value in dict_info.items():
			writer.writerow({"Extension" : key, "Volume" : value["volume"], "Quantity" : value["quantity"] })
		print(f"Saving data to '{folderName}.csv', from {folderName} folder...")
		return folderName+".csv"
def faz_grafico_barras(folderName):
	dict_info = faz_calculos(folderName)
	fields_list = []
	values_volume_list = []
	values_quantity_list = []
	for key, value in dict_info.items():
		fields_list.append("." + key)
		values_volume_list.append(value["volume"])
		values_quantity_list.append(value["quantity"])
	x = np.arange(len(fields_list))
	width = 0.15
	fig, ax = plt.subplots()
	r1 = ax.bar(x-width/2, values_volume_list, width, label="Volume")
	r2 = ax.bar(x+width/2, values_quantity_list, width, label="Quantity")
	ax.set_title("Extension, Volume[kBytes], Quantity")
	ax.set_xticks(x)
	ax.set_xticklabels(fields_list)
	ax.legend()
	ax.bar_label(r1, padding=3)
	ax.bar_label(r2, padding=3)
	fig.tight_layout()
	plt.show()
def faz_grafico_queijos(folderName):
	dict_info = faz_calculos(folderName)
	fields_list = []
	values_volume_list = []
	values_quantity_list = []
	for key, value in dict_info.items():
		fields_list.append("." + key)
		values_volume_list.append(value["volume"])
		values_quantity_list.append(value["quantity"])
	plt.pie(values_volume_list, labels=fields_list, autopct='%1.0f%%')
	plt.title("Extension, Volume[kBytes]")
	plt.show()