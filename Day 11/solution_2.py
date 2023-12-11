from math import dist

INPUT = "Day 11\\test_input.txt"


def get_data(data: str) -> list:
    temp = ""
    with open(data) as file:
        temp = file.read()
    return_list = temp.split("\n")
    return return_list


def find_empty_rows(univers: list) -> list:
    empty_rows = []
    for idx, line in enumerate(universe):
        if not "#" in line:
            empty_rows.append(idx)
    return empty_rows

def find_empty_columns(universe: list) -> list:
    empty_columns = []
    for idx_x in range(len(universe[0])):
        is_empty = True
        for idx_y in range(len(universe)):
            if universe[idx_y][idx_x] == "#":
                is_empty = False
                break
        if is_empty:
            empty_columns.append(idx_x)
    return empty_columns

def expand_universe(universe: list) -> list:
    # expand columns
    columns_to_expand = []
    for idx_x in range(len(universe[0])):
        is_empty = True
        for idx_y in range(len(universe)):
            if universe[idx_y][idx_x] == "#":
                is_empty = False
                break
        if is_empty:
            columns_to_expand.append(idx_x)
    x_expanded = []
    for line in universe:
        for column in reversed(columns_to_expand):
            line = line[:column] + "." + line[column:]
        x_expanded.append(line)
    
    # exand rows
    new_universe = []
    for line in x_expanded:
        if "#" in line:
            new_universe.append(line)
        else:
            new_universe.append(line)
            new_universe.append(line)
    return new_universe

def find_galaxies(universe: list) -> list:
    galaxies = []
    for idx_y, line in enumerate(universe):
        if "#" in line:
            for idx_x, char in enumerate(line):
                if char == "#":
                    galaxies.append((idx_x, idx_y))
    return galaxies

def find_distance(galaxy_1: tuple, galaxy_2: tuple, empty_rows:list, empty_columns:list, expansion_amt: int) -> int:
    expansion_to_add_x = 0
    expansion_to_add_y = 0
    for num in empty_columns:
        if max(galaxy_1[0], galaxy_2[0]) > num and num > min(galaxy_1[0], galaxy_2[0]):
            expansion_to_add_x += 1
    for num in empty_rows:
        if galaxy_2[1] > num and num > galaxy_1[1]:
            expansion_to_add_y += 1
    distance_x = max(galaxy_1[0], galaxy_2[0]) - min(galaxy_1[0], galaxy_2[0]) + (expansion_amt * expansion_to_add_x)
    distance_y = galaxy_2[1] - galaxy_1[1] + (expansion_amt * expansion_to_add_y)
    distance = distance_x + distance_y
    # distance = dist(galaxy_1, galaxy_2)
    # int_distance = round(distance)
    return distance

def calculate_distances(galaxy_list: list, empty_rows: list, empty_columns: list, expansion_amt: int = 1) -> int:
    distances = 0
    for idx, galaxy in enumerate(galaxy_list):
        if galaxy == galaxy_list[len(galaxy_list)-1]:
            continue
        for idx_2 in range(idx+1,len(galaxy_list)):
            distance = find_distance(galaxy, galaxy_list[idx_2], empty_rows, empty_columns, expansion_amt)
            # print(f"{idx},{idx_2} = {distance}")
            distances += distance
    return distances

if __name__ == "__main__":
    universe = get_data(INPUT)
    empty_rows = find_empty_rows(universe)
    empty_columns = find_empty_columns(universe)
    galaxy_list = find_galaxies(universe)
    print(empty_rows)
    print(empty_columns)
    total_distance = calculate_distances(galaxy_list, empty_rows, empty_columns, 1000000)
    print(total_distance)
