INPUT = "Day 10\\test_input.txt"
UP = ["|", "7", "F"]
RIGHT = ["-", "7", "J"]
DOWN = ["|", "J", "L"]
LEFT = ["-", "F", "L"]


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
                return (idx_x, idx_y)


def follow_node(node_map: list, starting_node: tuple, direction: int) -> tuple:
    x_pos, y_pos = starting_node
    match direction:
        case 0:
            next_node_char = node_map[y_pos - 1][x_pos]
            next_node = (y_pos-1, x_pos)
        case 1:
            next_node_char = node_map[y_pos][x_pos + 1]
            next_node = (y_pos, x_pos+1)
        case 2:
            next_node_char = node_map[y_pos + 1][x_pos]
            next_node = (y_pos+1, x_pos)
        case 3:
            next_node_char = node_map[y_pos][x_pos - 1]
            next_node = (y_pos, x_pos-1)
    next_direction = get_next_direction(next_node_char, direction)
    return (next_node, next_direction)


def get_next_direction(node_char: str, enter_direction: int) -> int:
    match enter_direction:
        case 0:  # coming from below
            match node_char:
                case "|":
                    leave_direction = 0
                case "F":
                    leave_direction = 1
                case "7":
                    leave_direction = 3
        case 1:  # coming from left
            match node_char:
                case "-":
                    leave_direction = 1
                case "J":
                    leave_direction = 0
                case "7":
                    leave_direction = 2
        case 2:  # coming from above
            match node_char:
                case "|":
                    leave_direction = 2
                case "J":
                    leave_direction = 3
                case "L":
                    leave_direction = 1
        case 3:  # coming from right
            match node_char:
                case "-":
                    leave_direction = 3
                case "L":
                    leave_direction = 0
                case "F":
                    leave_direction = 2
    return leave_direction


def look_around_start(map_list: list, starting_node: tuple) -> list:
    x_pos, y_pos = starting_node
    connects_to_start = []
    nodes_to_search = [map_list[y_pos-1][x_pos],  # up
                       map_list[y_pos][x_pos+1],  # right
                       map_list[y_pos+1][x_pos],  # down
                       map_list[y_pos][x_pos-1]]  # left
    if nodes_to_search[0] in UP:
        connects_to_start.append(0)
    if nodes_to_search[1] in RIGHT:
        connects_to_start.append(1)
    if nodes_to_search[2] in DOWN:
        connects_to_start.append(2)
    if nodes_to_search[3] in LEFT:
        connects_to_start.append(3)
    # 0 means up, 1 means right, 2 means down, 3 means left
    return connects_to_start


if __name__ == "__main__":
    data = get_data(INPUT)
    map_2D = make_map(data)
    print(map_2D)
    starting_node = find_start(map_2D)
    print(starting_node)
    directions = look_around_start(map_2D, starting_node)

    count_1 = 0
    count_2 = 0
    starting_nodes = [starting_node, starting_node]
    while True:
        # Direction 1
        next_node_1, next_direction_1 = follow_node(
            map_2D, starting_nodes[0], directions[0])
        count_1 += 1
        # Direction 2
        next_node_2, next_direction_2 = follow_node(
            map_2D, starting_nodes[1], directions[1])
        count_2 += 1

        if next_node_1 == next_node_2:
            break

        # clear current lists
        starting_nodes.clear()
        directions.clear()

        # put new data in lists for next iteration
        starting_nodes = [next_node_1, next_node_2]
        directions = [next_direction_1, next_direction_2]

    print(f"The longest distance is {max(count_1, count_2)} steps.")
