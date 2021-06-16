from neighbours_adder import *


def next_state(cells):
    for row in cells:
        for cell in row:
            if cell.neighbours > 0:
                count_state(cells, cell)
            elif cell.neighbours == 0 and cell.is_alive:
                cell.kill()
    for row in cells:
        for cell in row:
            prev = cell.is_alive
            cell.iterate()
            if cell.is_alive != prev:
                if cell.is_alive:
                    add_neighbour(cells, cell, 1)
                else:
                    add_neighbour(cells, cell, -1)


def count_state(cells, cell):
    nei = neighboors(cells, cell)
    if (nei > 3 or nei < 2) and cell.is_alive:
        cell.kill()
    elif nei == 3 and not cell.is_alive:
        cell.revive()


def neighboors(cells, cell):
    how_many = -1 if cell.is_alive else 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if cells[(cell.y + i) % BOARD_HEIGHT][(cell.x + j) % BOARD_WIDTH].is_alive:
                how_many += 1
    return how_many
