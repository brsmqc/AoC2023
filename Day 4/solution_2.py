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

        cards.append({"card_num": card_num, "winning_nums": winning_nums, "have_nums": have_nums, "copies": 1})

def calculate_matches(card:dict) -> int:
    have_nums = card["have_nums"]
    winning_nums = card["winning_nums"]
    matches = 0
    for num in have_nums:
        if num in winning_nums:
            matches += 1
    return matches


for index, card in enumerate(cards):
    matches = calculate_matches(card)
    for x in range(matches):
        cards[index + x +1]["copies"] += card["copies"]

total = 0
for card in cards:
    total += card["copies"]
    # print(f"card {card["card_num"]}: copies = {card["copies"]}")
print(f"total: {total}")