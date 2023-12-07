from operator import itemgetter

INPUT = "Day 7\\test_input.txt"
ORDER = dict((key, idx) for idx, key in enumerate(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]))


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

def sort_hand(hand:list) -> None:
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
    elif types[0] == 2 and types [1] == 2:
        hand.append(5)
    elif types[0] == 2:
        hand.append(6)
    else:
        hand.append(7)
    

def find_rank(hands:list) -> list:
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

def sort_hands(hands_list:list, letter_pos:int) -> list:
    # sort by the letter in question
    hands_list = sorted(hands_list, key=lambda x: ORDER.get(x[0][letter_pos]))
    
    sorted_hands_list = []
    if hands_list == []:
        return
    temp_list = []
    for idx, hand in enumerate(hands_list):
        # last in list
        if hand == hands_list[len(hands_list)-1]:
            if hand in temp_list:
                pass
            else:
                sorted_hands_list.append(hand)
        # first iteration only
        elif hand == hands_list[0]:
            if hand[0][letter_pos] == hands_list[idx+1][0][letter_pos]:
                temp_list.append(hand)
                temp_list.append(hands_list[idx+1])
            else:
                sorted_hands_list.append(hand)
        # every time after that
        elif hand[0][letter_pos] == hands_list[idx+1][0][letter_pos]:
                    temp_list.append(hands_list[idx+1])
        else:
            sorted_hands_list.append(hand)
    if temp_list != []:
        sorted_hands_list = [hand for hand in sort_hands(temp_list, letter_pos+1) if hand != None]
    return sorted_hands_list


def caulcate_winnings(ranked_list:list) -> int:
    total = 0
    for rank, hand in enumerate(ranked_list):
        total += hand[1] * (len(ranked_list) - rank)
    return total


if __name__ == "__main__":
    raw_list = get_data(INPUT)
    hands = make_hands_and_bids(raw_list)
    for hand in hands:
        sort_hand(hand)
        find_type(hand)
    hands.sort(key= lambda hand: hand[2])
    ranked = find_rank(hands)
    winnings = caulcate_winnings(ranked)
    print(ranked)
    print(winnings)

