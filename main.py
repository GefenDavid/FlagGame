import pygame
import random
import Screen
import Soldier
import consts
import Mine


def pressed_enter(game_grid):
    Screen.grid_background(Mine.locations_list(game_grid))
    pygame.time.delay(1000)


def handle_user_input(grid):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        pressed_enter(grid)
    elif keys[pygame.K_LEFT] and not Soldier.updated_body_area[0][1] == 0:
        Soldier.moved_left()
    elif keys[pygame.K_RIGHT] and not Soldier.updated_body_area[0][1] == 48:
        Soldier.moved_right()
    elif keys[pygame.K_UP] and not Soldier.updated_body_area[0][0] == 0:
        Soldier.moved_up()
    elif keys[pygame.K_DOWN] and not Soldier.updated_body_area[0][0] == 21:
        Soldier.moved_down()


def create_grid():
    game_grid = [[0] * consts.GAME_GRID_COLS for _ in
                 range(consts.GAME_GRID_ROWS)]
    for width in range(consts.FLAG_WIDTH):
        for height in range(consts.FLAG_HEIGHT):
            game_grid[21 + height][46 + width] = 2
    game_grid = Soldier.create(game_grid)
    game_grid = plant_mines(game_grid)
    return game_grid


def plant_mines(game_grid):
    count = 0
    while count < consts.NUM_OF_MINES:
        available = True
        row = random.randint(0, 24)
        col = random.randint(0, 47)
        mine = [(row, col), (row, col + 1), (row, col + 2)]
        for i in range(len(mine)):
            if game_grid[mine[i][0]][mine[i][1]] != 0 and (game_grid[mine[i][0]][mine[i][1]] != 3):
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


def is_touching_flag(flag_locations, soldier_body):
    for i in range(len(soldier_body)):
        if (soldier_body[i][0], soldier_body[i][1]) in flag_locations:
            return True
    return False


def is_touching_mine(mine_locations, soldier_legs):
    for i in range(len(soldier_legs)):
        if soldier_legs[i] in mine_locations:
            return True
    return False


def main():
    pygame.init()
    pygame.display.set_caption("Flag Game!")
    clock = pygame.time.Clock()
    grid = create_grid()
    Mine.locations_list(grid)
    Screen.create_random_index()
    run = True
    while run:
        clock.tick(consts.FPS)
        Screen.basic_background()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        handle_user_input(grid)
        if is_touching_mine(Mine.locations_list(grid), Soldier.legs_area()):
            Screen.draw_lose_message()
            pygame.time.delay(3000)
            run = False
        if is_touching_flag(flag_location(grid), Soldier.body_area()):
            Screen.draw_win_message()
            pygame.time.delay(3000)
            run = False


if __name__ == '__main__':
    main()
