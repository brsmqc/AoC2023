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

powers = []
for game in game_list:
    min_red = 0
    min_green = 0
    min_blue = 0
    for result in game[1:]:
        if result[1] == "red":
            if int(result[0]) > min_red:
                min_red = int(result[0])
        elif result[1] == "green":
            if int(result[0]) > min_green:
                min_green = int(result[0])
        elif result[1] == "blue":
            if int(result[0]) > min_blue:
                min_blue = int(result[0])
    power = min_red * min_green * min_blue
    powers.append(power)

print(powers)
total = 0
[total := total + num for num in powers]

print(total)
