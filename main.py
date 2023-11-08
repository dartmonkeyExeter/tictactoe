from math import ceil

grid = [1,2,3,4,5,6,7,8,9]

player_one_piece = "O"
player_two_piece = "X"

def display_grid():
    for i in range(0,9,3):
        print(grid[0 + i], grid[1 + i], grid[2 + i])

def win_check():
    # Check rows
    for i in range(0, 9, 3):
        if grid[i] == grid[i+1] == grid[i+2]:
            return True

    # Check columns
    for i in range(3):
        if grid[i] == grid[i+3] == grid[i+6]:
            return True

    # Check diagonals
    if grid[0] == grid[4] == grid[8] or grid[2] == grid[4] == grid[6]:
        return True


def game_loop():
    display_grid()
    while True:
        inp = input("where do you wanna go P1?\n")
        try:
            inp = int(inp)
            if inp > 9 or inp < 1:
                print("please enter a valid number")
                continue
        except ValueError:
            print("please enter valid numby!")
            continue

        if inp not in grid:
            print("someone already placed there!")
        else:
            grid[grid.index(inp)] = player_one_piece
        
        display_grid()
        if win_check() is True:
            print("you won P1!!!")
            break
        inp = input("where do you wanna go P2?\n")
        try:
            inp = int(inp)
            if inp > 9 or inp < 1:
                print("please enter a valid number")
                continue
        except ValueError:
            print("please enter valid numby!")
            continue

        if inp not in grid:
            print("someone already placed there!")
        else:
            grid[grid.index(inp)] = player_two_piece
        
        display_grid()
        if win_check() is True:
            print("you won P2!!!")
            break

game_loop()
