#Reglas de inferencia
class Nivel3:
    def __init__(self):
        #Definimos la ruta del guardián
        self.ruta_guardian = [(8, 9), (9, 9), (9, 8), (8, 8)]
        self.indice_patrulla = 0

    def percibir(self, pos_agente, pos_jugador):
        x, y = pos_agente
        bc = {
            "Arriba": (x, y + 1) == pos_jugador,
            "Abajo": (x, y - 1) == pos_jugador,
            "Izquierda": (x - 1, y) == pos_jugador,
            "Derecha": (x + 1, y) == pos_jugador,
        }
        return bc