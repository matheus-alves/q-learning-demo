NUM_OF_ROWS = 4
NUM_OF_COLUMNS = 12
CELL_SIZE = 40

START = (NUM_OF_ROWS - 1, 0)
GOAL = (NUM_OF_ROWS - 1, NUM_OF_COLUMNS - 1)

PENALTY = list()
for i in range(1, NUM_OF_COLUMNS - 1):
    point = (NUM_OF_ROWS - 1, i)
    PENALTY.append(point)
