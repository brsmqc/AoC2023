INPUT = "Day 11\\test_input.txt"


def get_data(data: str) -> list:
    temp = ""
    with open(data) as file:
        temp = file.read()
    return_list = temp.split("\n")
    return return_list


def expand_universe(universe: list) -> list:
    new_universe = []
    for line in universe:
        if "#" in line:
            new_universe.append(line)
        else:
            new_universe.append(line)
            new_universe.append(line)
    return new_universe

def find_galaxies(universe: list) -> list:
    count = 1
    galaxies = []
    for idx_y, line in enumerate(universe):
        if "#" in line:
            for idx_x, char in enumerate(line):
                if char == "#":
                    galaxies.append([count, (idx_x, idx_y)])
                    count += 1
    return galaxies


if __name__ == "__main__":
    universe = get_data(INPUT)
    expanded_universe = expand_universe(universe)
    galaxy_list = find_galaxies(expanded_universe)

    for galaxy in galaxy_list:
        print(galaxy)
