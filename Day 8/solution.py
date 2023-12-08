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
    

if __name__ == "__main__":
    data = get_data(INPUT)
    instructions = [direction for direction in data[0]]
    print(instructions)
    desert_map = format_map(data)
    for item in desert_map:
        print(item)