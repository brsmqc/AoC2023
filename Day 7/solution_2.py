from operator import itemgetter

INPUT = "Day 7\\input.txt"
ORDER = dict((key, idx) for idx, key in enumerate(
    ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]))


def get_data(data: str) -> list:
    temp = ""
    with open(data) as file:
        temp = file.read()
    return_list = temp.split("\n")
    return return_list


def make_hands_and_bids(hands: list) -> list:
    hands_list = []
    for hand in hands:
        hand_str = hand.split(" ")
        hands_list.append([hand_str[0], int(hand_str[1])])
    return hands_list


def sort_hand(hand: list) -> None:
    sorted_hand = sorted(hand[0], key=ORDER.get)
    # print(sorted_hand)
    hand[0] = "".join(sorted_hand)


def find_type(hand: list) -> None:
    chars = {}
    for char in hand[0]:
        if char in chars.keys():
            chars[char] += 1
        else:
            chars[char] = 1
    # print(chars)
    if "J" in chars.keys():
        chars = place_jokers(chars)
    types = []
    for value in chars.values():
        types.append(value)
    types.sort(reverse=True)
    # print(types)
    if types[0] == 5:
        hand.append(1)
    elif types[0] == 4:
        hand.append(2)
    elif types[0] == 3 and types[1] == 2:
        hand.append(3)
    elif types[0] == 3:
        hand.append(4)
    elif types[0] == 2 and types[1] == 2:
        hand.append(5)
    elif types[0] == 2:
        hand.append(6)
    else:
        hand.append(7)


def place_jokers(hand: dict) -> dict:
    sorted_hand = dict(sorted(hand.items(), key=lambda x: x[1], reverse=True))
    # print(sorted_hand)
    jokers = sorted_hand["J"]
    for idx, value in enumerate(sorted_hand.items()):
        if value[0] == "J":
            continue
        if value[1] == 4:
            sorted_hand[value[0]] += jokers
            sorted_hand["J"] -= jokers
            break
        elif value[1] == 3:
            sorted_hand[value[0]] += jokers
            sorted_hand["J"] -= jokers
            break
        elif value[1] == 2:
            sorted_hand[value[0]] += jokers
            sorted_hand["J"] -= jokers
            break
        else:
            sorted_hand[value[0]] += jokers
            sorted_hand["J"] -= jokers
            break
    return sorted_hand


def find_rank(hands: list) -> list:
    type_1 = [hand for hand in hands if hand[2] == 1]
    type_2 = [hand for hand in hands if hand[2] == 2]
    type_3 = [hand for hand in hands if hand[2] == 3]
    type_4 = [hand for hand in hands if hand[2] == 4]
    type_5 = [hand for hand in hands if hand[2] == 5]
    type_6 = [hand for hand in hands if hand[2] == 6]
    type_7 = [hand for hand in hands if hand[2] == 7]

    # sort by first letter
    combined_list = []
    for type in [type_1, type_2, type_3, type_4, type_5, type_6, type_7]:
        if type != []:
            type = sort_hands(type, 0)
        combined_list += type
    return combined_list


def sort_hands(hands_list: list, letter_pos: int) -> list:
    # sort by the letter in question
    hands_list = sorted(hands_list, key=lambda x: ORDER.get(x[0][letter_pos]))

    sorted_hands_list = []
    if hands_list == []:
        return
    temp_list = []
    next_index = 0
    for idx, hand in enumerate(hands_list):
        # get to the next index you haven't looked at yet
        if idx < next_index:
            continue
        # for the last value (since they're in order already)
        if letter_pos == 4:
            sorted_hands_list.append(hand)
        # last in list
        elif hand == hands_list[len(hands_list)-1]:
            if hand in temp_list:
                returned_hands_list = [hand for hand in sort_hands(
                    temp_list, letter_pos+1) if hand != None]
                sorted_hands_list += returned_hands_list
                temp_list.clear()
            else:
                sorted_hands_list.append(hand)
        elif hand[0][letter_pos] == hands_list[idx+1][0][letter_pos]:
            if temp_list == []:
                temp_list.append(hand)
                temp_list.append(hands_list[idx+1])
                next_index = idx
            else:
                temp_list.append(hands_list[idx+1])
                next_index = idx
        else:
            # hands_list = hands_list[idx+1:]
            if temp_list == []:
                sorted_hands_list.append(hand)
            if temp_list != []:
                returned_hands_list = [hand for hand in sort_hands(
                    temp_list, letter_pos+1) if hand != None]
                sorted_hands_list += returned_hands_list
                temp_list.clear()
    return sorted_hands_list


def caulcate_winnings(ranked_list: list) -> int:
    total = 0
    for rank, hand in enumerate(ranked_list):
        total += hand[1] * (len(ranked_list) - rank)
    return total


if __name__ == "__main__":
    raw_list = get_data(INPUT)
    hands = make_hands_and_bids(raw_list)
    for hand in hands:
        # sort_hand(hand)
        find_type(hand)
    hands.sort(key=lambda hand: hand[2])
    ranked = find_rank(hands)
    winnings = caulcate_winnings(ranked)
    # with open("output.txt", "w") as file:
    #     for rank in ranked:
    #         file.write(str(rank)+"\n")
    print(f"Hands: {len(ranked)}")
    print(f"Winnings: {winnings}")
