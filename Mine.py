def locations_list(game_grid):
    mines_locations = []
    for row in range(len(game_grid)):
        for col in range(len(game_grid[0])):
            if game_grid[row][col] == 1:
                mines_locations.append([row, col])
    return mines_locations
