#!/usr/bin/python3

import sys, time
import engine, botplayer
import view
import time

cfg_file = sys.argv[1]
rounds = int(sys.argv[2])
interval = int(sys.argv[3])
bots = sys.argv[4:]
DEBUG = False
CONTINUE_ON_ERROR = False

config = engine.GameConfig(cfg_file)
game = engine.Game(config, len(bots))
actors = [botplayer.BotPlayer(game, i, cmdline, debug=DEBUG) for i, cmdline in enumerate(bots)]

for actor in actors:
    actor.initialize()

view = view.GameView(game)

# Player color codes (same as view.py)
# 256 color ANSI format: \u001b[48;5;${i}m
colors = [
    1, #(255, 0, 0), red
    4, #(0, 0, 255), blue
    2, #(0, 255, 0), green
    3, #(255, 255, 0), yellow
    6, #(0, 255, 255), cyan
    13, #(255, 0, 255), magenta
    208, #(255, 127, 0), orange
    210 #(255, 127, 127), salmon
]
color_reset = "\u001b[0m"
color_bold = "\033[1m"

round = 0
while round < rounds:
    game.pre_round()
    view.update()

    for actor in actors:
        try:
            actor.turn()
        except botplayer.CommError as e:
            if not CONTINUE_ON_ERROR:
                raise
            else:
                print("CommError: " + str(e))
                actor.close()
        view.update()
    game.post_round()

    s = "%s%sROUND %d / %d\n\n" % (color_reset, color_bold, round, rounds)

    for i in range(len(bots)):
        color_player = "\u001b[38;5;%dm" % colors[i]
        s += "%s%sP%d (%s):\t %d \n" % (color_reset, color_player, i, game.players[i].name, game.players[i].score)
    print(s)

    round += 1
    time.sleep(interval / 1000)

view.update()
