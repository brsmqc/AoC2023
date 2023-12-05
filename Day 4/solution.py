cards = []

with open("Day 4\\input.txt") as file:
    while True:
        line = file.readline()
        if line == "":
            break
        split_1 = line.split(":")
        card_num = int(split_1[0][-3:].strip())
        split_2 = split_1[1].split("|")
        winning_nums = split_2[0].strip().split(" ")
        winning_nums = [int(num.strip()) for num in winning_nums if num != ""]
        have_nums = split_2[1].strip().split(" ")
        have_nums =[int(num.strip()) for num in have_nums if num != ""]

        cards.append({"card_num": card_num, "winning_nums": winning_nums, "have_nums": have_nums})

def calculate_points(card:dict) -> int:
    have_nums = card["have_nums"]
    winning_nums = card["winning_nums"]
    points = 0
    for num in have_nums:
        if num in winning_nums:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points


total = 0
for card in cards:
    total += calculate_points(card)

print(total)