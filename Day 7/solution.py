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
    print(types)
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
    


if __name__ == "__main__":
    raw_list = get_data(INPUT)
    hands = make_hands_and_bids(raw_list)
    for hand in hands:
        sort_hand(hand)
        find_type(hand)
    hands.sort(key= lambda hand: hand[2], reverse=True)
    print(hands)

