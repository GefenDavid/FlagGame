def locations(game_grid):
    mine_locations = []
    for row in range(len(game_grid)):
        for col in range(len(game_grid[0])):
            if game_grid[row][col] == 1:
                mine_locations.append((row, col))
    return mine_locations
