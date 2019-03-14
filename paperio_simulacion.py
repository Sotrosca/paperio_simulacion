import numpy as np


class tablero():
	def __init__(self, base, altura, tamañoCasaInicial, cantidadDeJugadores, posicionJugadores): ##posicionJugadores es un vector con las coordenadas x e y de cada jugadora al iniciar
																									#tamañoCsaInicial es un numero impar que da el caudrado en el que inician 
		self.base = base
		self.altura = altura
		self.tamañoCasaInicial = tamañoCasaInicial
		self.cantidadDeJugadores = cantidadDeJugadores
		self.posicionJugadores = posicionJugadores

class jugadore():
	def __init__(self, nombre, playerID, tablero):

		self.nombre = nombre
		self.playerID = playerID
		self.direccionInicial =  np.random.randint(1, 5)
		self.posicionInicial = tablero.posicionJugadores[playerID - 1]
		self.tamañoCasaInicial = tablero.tamañoCasaInicial
		self.matrizTerritorio = np.zeros((tablero.altura + 2, tablero.base + 2))
		
		vectorAux1 = np.ones((tablero.base, 1))
		vectorAux2 = np.ones((tablero.altura + 2, 1))
		matrizAux = np.zeros((tablero.base, tablero.altura))
		self.matrizDeCamino = np.concatenate((vectorAux2, np.concatenate((vectorAux1, matrizAux, vectorAux1), axis=1).T, vectorAux2), axis=1)

		for i in list(range(self.posicionInicial[0] - int((self.tamañoCasaInicial - 1) / 2), self.posicionInicial[0] + int((self.tamañoCasaInicial + 1) / 2))):
			for j in list(range(self.posicionInicial[1] - int((self.tamañoCasaInicial - 1) / 2), self.posicionInicial[1] + int((self.tamañoCasaInicial + 1) / 2))):
				self.matrizTerritorio[i, j] = 1




tablero1 = tablero(10, 10, 3, 2, [(3,3),(7,6)])
Facu = jugadore('Facu', 1, tablero1)

print(Facu.matrizDeCamino)
#Sol = jugadore('Sol', 2, tablero1)
#print(Facu.matrizTerritorio)
#print(Sol.matrizTerritorio)

