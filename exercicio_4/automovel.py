class Automovel():
	"""docstring for automovel"""
	def __init__(self, cap_dep, quant_comb, consumo, nome="Herbie"):
		self.nome = nome
		self.cap_dep = cap_dep
		self.quant_comb = quant_comb
		self.consumo = consumo
	def combustivel(self):
		return self.quant_comb
	def autonomia(self):
		return self.quant_comb * 100 / self.consumo
	def abastece(self, n_litros):
		if self.quant_comb + n_litros > self.cap_dep:
			print("Erro, nao pode abastecer mais do que o tanque permite...")
			return -1
		self.quant_comb += n_litros
		print("Abasteceu...")
	def precorre(self, n_km):
		if n_km > self.autonomia():
			print("Erro, nao pode precorrer mais do que o combistivel rende...")
			return -1
		else:
			self.quant_comb -= n_km * self.consumo / 100
		print("Precorreu...")