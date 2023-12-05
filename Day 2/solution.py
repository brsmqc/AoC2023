RED = 12
GREEN = 13
BLUE = 14

game_list = []
with open("Day 2\\input.txt", "r") as file:
    while True:
        line = file.readline()
        if line == "":
            break
        else:
            game = []
            game_id_str, game_data = line.split(":")
            game_id = int(game_id_str.split(" ")[1])
            game.append(game_id)
            game_results = game_data.split(";")
            for round in game_results:
                grabs = round.split(",")
                for grab in grabs:
                    die = grab.split(" ")
                    game.append((die[1], die[2].strip()))
            game_list.append(game)

possible_games = []
for game in game_list:
    possible = True
    for result in game[1:]:
        if result[1] == "red":
            if int(result[0]) > RED:
                possible = False
        elif result[1] == "green":
            if int(result[0]) > GREEN:
                possible = False
        elif result[1] == "blue":
            if int(result[0]) > BLUE:
                possible = False
    if possible:
        possible_games.append(game[0])

total = 0
[total := total + num for num in possible_games]

print(total)
