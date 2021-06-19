from setup import *
from drawer import draw
from preparer import next_state, neigh_iterate
from generator import generate_cells


def main():
    cells = generate_cells()
    clock = pygame.time.Clock()
    update_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    run = True
    pause = False
    while run:
        clock.tick(FPS)
        if not pause:
            draw(cells)
            next_state(cells)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False if pause else True
                    draw(cells)
                if pause:
                    if event.key == pygame.K_n:
                        next_state(cells)
                        draw(cells)
                    if event.key == pygame.K_c:
                        for row in cells:
                            for cell in row:
                                cell.kill()
                                neigh_iterate(cells, cell)
                        draw(cells)
            if event.type == pygame.MOUSEBUTTONDOWN and pause:
                poz = pygame.mouse.get_pos()
                x = poz[0] // CELL_WIDTH
                y = poz[1] // CELL_HEIGHT
                cell = cells[y][x]
                cell.kill() if cell.is_alive else cell.revive()
                neigh_iterate(cells, cell)
                draw(cells)
        pygame.display.update(update_rect)
    pygame.quit()


if __name__ == '__main__':
    main()
