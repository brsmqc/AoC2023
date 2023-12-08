INPUT = "Day 8\\input.txt"


def get_data(data: str) -> list:
    temp = ""
    with open(data) as file:
        temp = file.read()
    return_list = temp.split("\n")
    return return_list


def format_map(data: str) -> dict:
    desert_network = []
    for line in data[2:]:
        node, net = line.split(" = ")
        connect_left, connect_right = net.split(", ")
        connections = (connect_left.strip("("), connect_right.strip(")"))
        desert_network.append({node: connections})
    return desert_network


def follow_map(instructions: list, network: dict, starting_node: str, starting_index: int = 0) -> int:
    steps = 0
    if starting_node == "ZZZ":
        return 0
    if starting_index == len(instructions):
        starting_index = 0
    next_move = instructions[starting_index]
    next_index = starting_index + 1
    for node in network:
        if starting_node in node.keys():
            next_node = node[starting_node][next_move]
            steps += 1
            return steps, next_node, next_index


if __name__ == "__main__":
    data = get_data(INPUT)
    instructions = [0 if direction == "L" else 1 for direction in data[0]]
    # print(instructions)
    desert_map = format_map(data)
    next_node = "AAA"
    total_steps = 0
    step, next_node, next_index = follow_map(
        instructions, desert_map, next_node)
    total_steps += step
    while True:
        if next_node == "ZZZ":
            break
        step, next_node, next_index = follow_map(
            instructions, desert_map, next_node, next_index)
        total_steps += step

    print(f"total steps: {total_steps}")
    # for item in desert_map:
    #     print(item)
