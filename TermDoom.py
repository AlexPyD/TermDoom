import random

MAP_SIZE = 10

PLAYER_SYMBOL = "■"
ENEMY_SYMBOL = "E"

player_x = random.randint(0, MAP_SIZE - 1)
player_y = random.randint(0, MAP_SIZE - 1)

enemy_x = random.randint(0, MAP_SIZE - 1)
enemy_y = random.randint(0, MAP_SIZE - 1)

while True:
    game_map = [["."] * MAP_SIZE for _ in range(MAP_SIZE)]
    game_map[player_y][player_x] = PLAYER_SYMBOL
    game_map[enemy_y][enemy_x] = ENEMY_SYMBOL

    for row in game_map:
        print(" ".join(row))
    
    user_input = input("Enter a move (W/A/S/D): ").upper()

    if user_input == "W":
        player_y -= 1
    elif user_input == "A":
        player_x -= 1
    elif user_input == "S":
        player_y += 1
    elif user_input == "D":
        player_x += 1

    if player_x == enemy_x and player_y == enemy_y:
        game_map[enemy_y][enemy_x] = "."  # Remove enemy from the map
        print("You Win!")
        break
