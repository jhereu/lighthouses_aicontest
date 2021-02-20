# Euskal Encounter — AI Contest
Motor del juego

Autor: marcan <marcan@euskalencounter.org>
Licencia: GPLv2/v3

## Requisitos (Linux)

```sh
apt-get install python3
apt-get install python3-pygame
```

## Requisitos (Windows WSL)

Para arrancar el proyecto en Windows es necesaria la instalación de una distribución Windows mediante WSL2 (Windows Subsystem for Linux) y un X-Server para poder visualizar el tablero de juego.

* WSL2 (Windows Subsystem for Linux 2): https://docs.microsoft.com/es-es/windows/wsl/install-win10 
* VcXsrv Windows X-Server: https://sourceforge.net/projects/vcxsrv/

Dentro del subsistema Linux:

```sh
apt-get install python3
apt-get install python3-pygame
```
Importante tener arrancado X-Server en Windows para que el tablero aparezca al arrancar el juego.

## Lanzamiento de aplicación

```sh
# Arg 1: Fichero del juego (game.py)
# Arg 2: Mapa
# Arg 3: Número de rondas
# Arg 4: Intervalo de milisegundos entre rondas
# Arg 5+: Comandos de lanzamiento de los bots, siempre entrecomillados
python3 engine/game.py maps/<mapa.txt> <rondas> <intervalo>  'comando player0' 'comando player1'...

# Ejemplo:
# python3 engine/game.py maps/grid.txt 500 100 'python3 engine/RandBot/randbot.py' 'node bot.js'
```
