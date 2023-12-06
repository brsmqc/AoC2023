import re

INPUT = "Day 6\\test_input.txt"

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

if __name__ == "__main__":
    races = get_data(INPUT)
    print(races)