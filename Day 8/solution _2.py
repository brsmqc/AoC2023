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


def find_a(network: dict) -> dict:
    a_z_nodes = []
    for node in network:
        node_name = list(node.keys())[0]
        if node_name[2] == "A":
            a_z_nodes.append(list(node.keys())[0])
    return a_z_nodes


def follow_map(instructions: list, network: dict, starting_node: str, starting_index: int = 0) -> int:
    next_move = instructions[starting_index]
    for node in network:
        if starting_node in node.keys():
            next_node = node[starting_node][next_move]
            node_last_letter = next_node[2]
            return next_node, node_last_letter


if __name__ == "__main__":
    data = get_data(INPUT)
    instructions = [0 if direction == "L" else 1 for direction in data[0]]
    # print(instructions)
    desert_map = format_map(data)
    a_nodes = find_a(desert_map)

    total_steps = 0
    next_index = 0
    while True:
        new_nodes = []
        final_letters = set()
        for node in a_nodes:
            next_node, final_letter = follow_map(
                instructions, desert_map, node, next_index)
            new_nodes.append(next_node)
            final_letters.add(final_letter)
        total_steps += 1
        print(f"step {total_steps} complete")
        a_nodes = new_nodes
        if len(final_letters) == 1 and "Z" in final_letters:
            break
        next_index += 1
        if next_index == len(instructions):
            next_index = 0

    print(f"total steps: {total_steps}")
    # for item in desert_map:
    #     print(item)
