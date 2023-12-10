INPUT = "Day 10\\test_input.txt"


def get_data(data: str) -> list:
    temp = ""
    with open(data) as file:
        temp = file.read()
    return_list = temp.split("\n")
    return return_list


def make_map(data: list) -> list:
    map_2D = []
    for line in data:
        line = [char for char in line]
        map_2D.append(line)
    return map_2D


def find_start(map_list: list) -> tuple:
    for idx_y, line in enumerate(map_list):
        for idx_x, column in enumerate(line):
            if column == "S":
                return idx_x, idx_y


def get_next_node(starting_node: tuple, direction: int):
    pass


def look_around_start(map_list: list, starting_node: tuple) -> list:
    x_pos, y_pos = starting_node
    connects_to_start = []
    nodes_to_search = [map_list[y_pos-1][x_pos],  # up
                       map_list[y_pos][x_pos+1],  # right
                       map_list[y_pos+1][x_pos],  # down
                       map_list[y_pos][x_pos-1]]  # left
    if nodes_to_search[0] in ["|", "7", "F"]:
        connects_to_start.append(0)
    if nodes_to_search[1] in ["-", "7", "J"]:
        connects_to_start.append(1)
    if nodes_to_search[2] in ["|", "J", "L"]:
        connects_to_start.append(2)
    if nodes_to_search[3] in ["-", "F", "L"]:
        connects_to_start.append(3)
    # 0 means up, 1 means right, 2 means down, 3 means left
    return connects_to_start


if __name__ == "__main__":
    data = get_data(INPUT)
    map_2D = make_map(data)
    print(map_2D)
    starting_node = find_start(map_2D)
    print(starting_node)
    print(look_around_start(map_2D, starting_node))
