# Python Lab3

### INDEX
+ ##### Exercise1
	- JSON Exercises
	- package managment
+ ##### Exercise2
	- CSV Execises
	- matplotlib *(graphs: bar & pie)*
	- Modules Importation
+ ##### Exercise3
	- Recursive function exercise
+ ##### Exercise4
	- Classes
	- Car Class

### Usage
Run the python script from the terminal or using a text editor that allows you to run python3 code.
#### Exercise1:

```console
	# Locate the exercice in your enviroment
	# Run python script
	# Enter a file name wich exist on your computer
	# I created a dummy file *<text.txt>* that you can use to test the code.
```

```bash
	$ cd pw_python_03/exercicio_1
	$ python principal.py
	 Please Enter the file name: text.txt
	 Created text.json ! :)
```

#### Exercise2:
```console
	# Locate the exercice in your enviroment
	# Run python script
	# Enter a folder name wich exist on your computer
	# I created a dummy folder *<TEST>* that you can use to test the code
```

```bash
	$ cd pw_python_03/exercicio_2
	$ python main.py
	 Welcome! This programm analizes any kind of file inside a folder.
	 Please Enter the folder name: TEST
	 Saving data to 'TEST.csv', from TEST folder...
	 Options:
	 (1) - Open BAR Graph
	 (2) - Open PIE Graph
	 (0) - EXIT
	 Choose an option to continue: 0
	 ByeBye, Have a nice day
```
#### Exercise3:

```console
	# Locate the exercice in your enviroment
	# Run python script
	# Enter a folder name wich exist on your computer
	# I created a dummy folder *<TEST>* that you can use to test the code
```

```bash
	$ cd pw_python_03/exercicio_3
	$ python folder_calculator.py
	 Welcome! This programm analizes any kind of file inside a folder.
	 Please Enter the folder name: TEST
	 Total size of ' TEST/sd ' is:  1.1484375 [kBytes]
	 Total size of ' TEST ' is:  38.537109375 [kBytes]
	 ******************** 
	 The Folder TOTAL Size is:  38.537109375 [kBytes].
	 ********************
```

#### Exercise4:

```console
	# Locate the exercice in your enviroment
	# Run python script
	# Have Fun
```

```bash
	$ cd pw_python_03/exercicio_4
	$ python carro.py
	 Olá, este programa permite gerir um automovel
	 Queres dar um nome ao teu carro?[y/n]: y
	 Escreve o nome: Rayo McQueen
	 Carros Disponiveis: 
	--------------------------------------------------------------------------------
	(1) - STATS: Capacidade do Deposito: 300L | Consumo: 50/100Km.
	   ______
	 /|_||_\`.__
	(   _    _ _\ 
	=`-(_)--(_)-''
	--------------------------------------------------------------------------------
	(2) - STATS: Capacidade do Deposito: 100L | Consumo: 30/100Km.
	    _-_-  _/\______\__
	 _-_-__  / ,-. -|-  ,-.`-.
	=-- _-_- `( o )----( o )-''
	           `-'      `-'
	--------------------------------------------------------------------------------
	(3) - STATS: Capacidade do Deposito: 250L | Consumo: 40/100Km.
	     ,-----,     
	 ,--'---:---'--,
	==(o)-----(o)==J
	Escolhe um dos carro: 1
	Escolheste a opcao 1
	-----MENU (Rayo McQueen) Model1-----
	 (1) Consultar combustivel.
	 (2) Autonomia.
	 (3) Abastecer!
	 (4) Precorrer!
	 (5) See car
	 (0) EXIT
	Escolhe uma opcao: 1
	O combustivel disponivel é:  100 Litros.
	Escolhe uma opcao: 2
	 Autonomía:  200 Km.
	Escolhe uma opcao: 3
	 Quantidade de combustivel(Litros): 500
	 Erro, nao pode abastecer mais do que o tanque permite...
	Escolhe uma opcao: 3
	 Quantidade de combustivel(Litros): 30
	 Abasteceu...
	Escolhe uma opcao: 4
	 Distancia precorrida(Km): 20
	 Precorreu...
	Escolhe uma opcao: 5
	--------------------------------------------------------------------------------
	 (1) Rayo McQueen - STATS: Capacidade do Deposito: 300L | Consumo: 50/100Km.
	    ______
	  /|_||_\`.__
	 (   _    _ _\ 
	 =`-(_)--(_)-''
	Escolhe uma opcao: 0
	Alright. Bye bye!
```
##### If you have any advice for me, open an Issue and I'll have a look! :)