import level
LEVEL = 0
LEVEL, MINE = level.level_choice()
def level_selected() :
    global LEVEL
    if LEVEL == 0 :
        print(True)
WIDTH=700
HEIGHT=500
GRID_SIZE=LEVEL
CELL_COUNT=GRID_SIZE**2
MINES_COUNT=MINE
