import re

INPUT = "Day 6\\input.txt"

def get_data(data:str) -> list:
    input = ""
    with open(data) as file:
        input = file.read()
    input_list = input.split("\n")
    data_list = []
    for line in input_list:
        times = re.findall("\\d+", line)
        digit_str = ""
        for digit in times:
            digit_str += digit
        data_list.append(int(digit_str))
    return data_list

def calc_num_of_winning_times(time:int, distance:int) -> int:
    winners = 0
    for milisec in range(time):
        if milisec * (time - milisec) > distance:
            winners += 1
    print(winners)
    return winners

if __name__ == "__main__":
    races = get_data(INPUT)
    print(races)
    possibilities = calc_num_of_winning_times(races[0], races[1])
    print(f"total possible ways: {possibilities}")
