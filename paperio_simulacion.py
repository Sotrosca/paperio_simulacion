import numpy as np


class tablero():
	def __init__(self, largo, ancho, tamañoCasaInicial, cantidadDeJugadores, posicionJugadores): ##posicionJugadores es un vector con las coordenadas x e y de cada jugadora al iniciar
																									#tamañoCsaInicial es un numero impar que da el caudrado en el que inician 
		self.largo = largo
		self.ancho = ancho
		self.tamañoCasaInicial = tamañoCasaInicial
		self.cantidadDeJugadores = cantidadDeJugadores
		self.posicionJugadores = posicionJugadores

class jugadore():
	def __init__(self, nombre, playerID, direccionInicial, tablero):

		self.nombre = nombre
		self.playerID = playerID
		self.direccionInicial =  np.random.random_integers(low=1,high=4)
		self.posicionInicial = tablero.posicionJugadores[playerID-1]
		self.tamañoCasaInicial = tablero.tamañoCasaInicial
		self.matrizterritorio = np.zeros((tablero.ancho + 2, tablero.largo + 2)) 


