# Escape del Laberinto - Proyecto Final - Inteligencia Artificial

Es un juego por turnos donde un jugador debe atravesar tres laberintos evitando ser capturado por un agente inteligente. Desarrollado en Python.

## Estructura de los Niveles
Cada nivel utiliza una técnica de IA distinta (vistas en clase) para el agente que te persigue:
- **Nivel 1:** Búsqueda $A^{*}$ con distancia Manhattan.
- **Nivel 2:** Búsqueda adversarial (Minimax con Poda Alfa-Beta) limitando la profundidad a 4 movimientos.
- **Nivel 3:** Agente basado en conocimiento (Lógica proposicional) con ruta de patrullaje.

## Requisitos Previos
- Python 3.10 o superior.
- Git (para clonar el repositorio).

## Instalación y Ejecución

1. Clona este repositorio:
   ```bash
   git clone <https://github.com/Lconejo/Escape-del-laberinto.git>
   cd Escape-del-laberinto
