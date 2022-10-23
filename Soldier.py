import consts

updated_body_area = consts.SOLDIER_BODY_AREA
updated_legs_area = consts.SOLDIER_LEG_AREA


def legs_area():
    return [updated_body_area[6], updated_body_area[7]]
    # returns list of location indexes of soldier legs


def body_area():
    return updated_body_area


def moved_right():
    for i in updated_body_area:
        i[1] += 1


def moved_left():
    for i in updated_body_area:
        i[1] -= 1


def moved_up():
    for i in updated_body_area:
        i[0] -= 1


def moved_down():
    for i in updated_body_area:
        i[0] += 1


def create(game_grid):
    for row in range(int(len(consts.SOLDIER_BODY_AREA) / 2)):
        for col in range(len(consts.SOLDIER_LEG_AREA)):
            game_grid[row][col] = 3
    return game_grid
