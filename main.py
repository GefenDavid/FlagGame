import pygame
import random
import consts


def key_movements(key_input):
    if key_input[pygame.K_LEFT]:
        print("left")
    if key_input[pygame.K_RIGHT]:
        print("right")
    if key_input[pygame.K_UP]:
        print("up")
    if key_input[pygame.K_DOWN]:
        print("down")


def pressed_enter():
    pass


def handle_user_input():
    pass


def create_grid():
    game_grid = [[0] * consts.GAME_GRID_COLS for _ in
                 range(consts.GAME_GRID_ROWS)]
    for width in range(consts.FLAG_WIDTH):
        for height in range(consts.FLAG_HEIGHT):
            game_grid[21 + height][46 + width] = 2
    game_grid = plant_mines(game_grid)
    print(game_grid)
    return game_grid


def plant_mines(game_grid):
    count = 0
    while count < consts.NUM_OF_MINES:
        available = True
        row = random.randint(0, 24)
        col = random.randint(0, 47)
        mine = [(row, col), (row, col + 1), (row, col + 2)]
        for i in range(len(mine)):
            if game_grid[mine[i][0]][mine[i][1]] != 0:
                available = False
        if available:
            for i in range(len(mine)):
                game_grid[mine[i][0]][mine[i][1]] = 1
            count += 1
            available = False
    return game_grid


def flag_location(game_grid):
    flag_locations = []
    for row in range(len(game_grid)):
        for col in range(len(game_grid[0])):
            if game_grid[row][col] == 2:
                flag_locations.append((row, col))
    return flag_locations


def is_touching_flag(flag_locations, soldier):
    soldier_body = soldier.body_area()
    for i in range(len(soldier_body)):
        if soldier.body_area[i] in flag_locations:
            return True
    return False


def is_touching_mine(mine_locations, soldier):
    soldier_legs = soldier.legs_area()
    for i in range(len(soldier_legs)):
        if soldier.body_area[i] in mine_locations:
            return True
    return False


def main():
    pygame.init()
    screen = pygame.display.set_mode(
            (consts.SCREEN_LENGTH, consts.SCREEN_HEIGHT))
    pygame.display.set_caption("Flag Game!")
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.K_RETURN:
                pressed_enter()


if __name__ == '__main__':
    main()
