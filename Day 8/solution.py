INPUT = "Day 8\\test_input.txt"


def get_data(data: str) -> list:
    temp = ""
    with open(data) as file:
        temp = file.read()
    return_list = temp.split("\n")
    return return_list


def format_map(data:str) -> dict:
    desert_network = []
    for line in data[2:]:
        node, net = line.split(" = ")
        connect_left, connect_right = net.split(", ")
        connections = (connect_left.strip("("), connect_right.strip(")"))
        desert_network.append({node: connections})
    return desert_network


def follow_map(instructions:list, network:dict, starting_node:str, starting_index:int = 0) -> int:
    steps = 0
    if starting_node == "ZZZ":
        steps += 1
        return steps
    if starting_index == len(instructions):
        starting_index = 0
    next_move = instructions[starting_index]
    for node in network:
        if starting_node in node.keys():
            next_node = node[starting_node][next_move]
            steps += follow_map(instructions, network, next_node, starting_index+1)
            return steps


if __name__ == "__main__":
    data = get_data(INPUT)
    instructions = [0 if direction == "L" else 1 for direction in data[0]]
    print(instructions)
    desert_map = format_map(data)
    total_steps = follow_map(instructions, desert_map, "AAA")
    print(total_steps)
    for item in desert_map:
        print(item)