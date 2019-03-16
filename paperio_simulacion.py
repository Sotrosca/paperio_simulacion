# -*- coding: utf-8 -*-
import numpy as np


class tablero():
	#tamañoCsaInicial es un numero impar que da el caudrado en el que inician 
	#posicionJugadores es una lista coordenadas x e y de cada jugadora al iniciar

	def __init__(self, base, altura, tamanoCasaInicial, cantidadDeJugadores, posicionJugadores): 
																									
		self.base = base
		self.altura = altura
		self.tamanoCasaInicial = tamanoCasaInicial
		self.cantidadDeJugadores = cantidadDeJugadores
		self.posicionJugadores = posicionJugadores
class decision():
	def __init__(self, tablero, listaJugadores):
		

class jugador():
	def __init__(self, nombre, playerID, tablero):

		self.nombre = nombre
		self.playerID = playerID
		self.direccionInicial =  np.random.randint(1, 5)
		self.posicionInicial = tablero.posicionJugadores[playerID - 1]
		self.tamanoCasaInicial = tablero.tamanoCasaInicial
		self.matrizTerritorio = np.zeros((tablero.altura + 2, tablero.base + 2))
		self.posicionJugador = tablero.posicionJugadores[playerID - 1]
		vectorAux1 = np.ones((tablero.base, 1))
		vectorAux2 = np.ones((tablero.altura + 2, 1))
		matrizAux = np.zeros((tablero.base, tablero.altura))
		self.matrizDeCamino = np.concatenate((vectorAux2, np.concatenate((vectorAux1, matrizAux, vectorAux1), axis=1).T, vectorAux2), axis=1)

		for i in list(range(self.posicionInicial[0] - int((self.tamanoCasaInicial - 1) / 2), self.posicionInicial[0] + int((self.tamanoCasaInicial + 1) / 2))):
			for j in list(range(self.posicionInicial[1] - int((self.tamanoCasaInicial - 1) / 2), self.posicionInicial[1] + int((self.tamanoCasaInicial + 1) / 2))):
				self.matrizTerritorio[i, j] = 1

	def avanzar(self)




tablero1 = tablero(10, 10, 3, 2, [(3,3),(7,6)])
Facu = jugadore('Facu', 1, tablero1)

#print(Facu.matrizDeCamino)
#Sol = jugadore('Sol', 2, tablero1)
print(Facu.matrizTerritorio)
#print(Sol.matrizDeCamino)

