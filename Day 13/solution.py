INPUT = "Day 13\\test_input.txt"


def get_data(data: str) -> list:
    temp = ""
    with open(data) as file:
        temp = file.read()
    return_list = temp.split("\n")
    return return_list

def make_2d_lists(data: list) -> list:
    patterns = []
    temp_pattern = []
    for idx, line in enumerate(data):
        if line == "" or idx == len(data)-1:
            patterns.append([item for item in temp_pattern])
            temp_pattern.clear()
        else:
            temp_pattern.append(line)
    return patterns

if __name__ == "__main__":
    data = get_data(INPUT)
    patterns = make_2d_lists(data)
    for pattern in patterns:
        print(pattern)