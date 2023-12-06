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
        times = [int(time) for time in times]
        data_list.append(times)
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
    total = 1
    for x in range(len(races[0])):
        total *= calc_num_of_winning_times(races[0][x], races[1][x])
    print(f"total possible ways: {total}")
