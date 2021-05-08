import math
from automovel import *
def main():
	cars = {1 : {"art" : ("   ______", " /|_||_\`.__", "(   _    _ _\ ", "=`-(_)--(_)-'"), "deposito" : 300, "consumo" : 50}, 2 : {"art" : ("    _-_-  _/\______\\__", " _-_-__  / ,-. -|-  ,-.`-.", "=-- _-_- `( o )----( o )-'", "           `-'      `-'"),  "deposito" : 100, "consumo" : 30}, 3 : {"art" : ("      ,-----,     ", "  ,--'---:---`--,", " ==(o)-----(o)==J"),  "deposito" : 250, "consumo" : 40}}
	print("Olá, este programa permite gerir um automovel")
	answer = True if input("Queres dar um nome ao teu carro?[y/n]: ").strip().lower() == "y" else False
	if answer:
		nome = input("Escreve o nome: ")
	print("Carros Disponiveis: ")
	for model, values in cars.items():
		print("-"*80)
		print(f"({model}) - STATS: Capacidade do Deposito: {values['deposito']}L | Consumo: {values['consumo']}/100Km.")
		for value in values["art"]:
			print(value)
	car_option = int(input("Escolhe um dos carro: "))
	if car_option == 1:
		deposito = 100
		capacidade = 300
		consumo	= 50
	elif car_option == 2:
		deposito = 100
		capacidade = 100 
		consumo = 30
	elif car_option == 3: 
		deposito = 100
		capacidade = 250 
		consumo	= 40
	else:
		print("Opcao invalida!")
		return -1
	print("Escolheste a opcao", car_option)
	car = Automovel(capacidade, deposito, consumo) if not answer else Automovel(capacidade, deposito, consumo, nome)
	while True:
		print(f"-----MENU ({car.nome}) Model{car_option}-----")
		print(" (1) Consultar combustivel.\n", "(2) Autonomia.\n", "(3) Abastecer!\n","(4) Precorrer!\n", "(5) See car\n","(0) EXIT")
		option = int(input("Escolhe uma opcao: "))
		if option == 1:
			print("O combustivel disponivel é: ", car.combustivel(), "Litros.")
		elif option == 2:
			print("Autonomía: ", math.floor(car.autonomia()), "Km.")
		elif option == 3:
			car.abastece(int(input("Quantidade de combustivel(Litros): ")))
		elif option == 4:
			car.precorre(int(input("Distancia precorrida(Km): ")))
		elif option == 5:
			print("-"*80)
			print(f"({car_option}) {car.nome} - STATS: Capacidade do Deposito: {cars[car_option]['deposito']}L | Consumo: {cars[car_option]['consumo']}/100Km.")
			for value in cars[car_option]["art"]:
				print(value)
		elif option == 0:
			print("Alright. Bye bye!")
			break
		else : 
			print("Opcao invalida!")

if __name__ == "__main__": 
  main()