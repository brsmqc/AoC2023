INPUT = "Day 7\\test_input.txt"


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


def find_rank(hand: list) -> None:
    chars = {}
    for char in hand:
        if char in chars.keys():
            chars[char] += 1
        else:
            chars[char] = 1


if __name__ == "__main__":
    raw_list = get_data(INPUT)
    hands = make_hands_and_bids(raw_list)
    for hand in hands:
        find_rank(hand[0])
    # print(hands)
