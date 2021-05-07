import analisa_ficheiro
import json
import os

def main():
	fileName = analisa_ficheiro.pede_nome()
	jsonFile = open(analisa_ficheiro.gera_nome(fileName), "w")
	jsonText = {	"Lines": analisa_ficheiro.calcula_linhas(fileName),
					"Characters": analisa_ficheiro.calcula_carateres(fileName),
					"Biggest_Word": analisa_ficheiro.calcula_palavra_comprida(fileName),
					"Words_Dictionary": analisa_ficheiro.calcula_ocorrencia_de_letras(fileName)
	}
	json.dump(jsonText, jsonFile, indent = 4, sort_keys=True)


if __name__ == "__main__": 
    main()