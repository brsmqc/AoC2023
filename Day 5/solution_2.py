INPUT = "Day 5\\input.txt"


def get_input():
    input = ""
    with open(INPUT) as file:
        input = file.read()
    return input.split("\n")


def get_seeds(input: list) -> list:
    seed_line = input[0].split(" ")
    seeds = []
    for x in range(len(seed_line)):
        if x % 2 == 0:
            continue
        seed_start = int(seed_line[x])
        seed_length = int(seed_line[x+1])
        seeds.append({"seed_num": [seed_start, seed_start+seed_length]})
    return seeds


def find_location(seed: int, soil: list, fert: list, water: list, light: list, temp: list, humid: list, loc: list) -> int:
    soil_num = fert_num = water_num = light_num = temp_num = humid_num = location = float(
        "-inf")
    for x, data in enumerate(soil[0]):
        if x % 2 != 0:
            continue
        if data <= seed and seed <= soil[0][x+1]:
            to_add = seed - data
            soil_num = soil[1][x] + to_add
    if soil_num == float("-inf"):
        soil_num = seed
    for x, data in enumerate(fert[0]):
        if x % 2 != 0:
            continue
        if data < soil_num and soil_num <= fert[0][x+1]:
            to_add = soil_num - data
            fert_num = fert[1][x] + to_add
    if fert_num == float("-inf"):
        fert_num = soil_num
    for x, data in enumerate(water[0]):
        if x % 2 != 0:
            continue
        if data <= fert_num and fert_num <= water[0][x+1]:
            to_add = fert_num - data
            water_num = water[1][x] + to_add
    if water_num == float("-inf"):
        water_num = fert_num
    for x, data in enumerate(light[0]):
        if x % 2 != 0:
            continue
        if data <= water_num and water_num <= light[0][x+1]:
            to_add = water_num - data
            light_num = light[1][x] + to_add
    if light_num == float("-inf"):
        light_num = water_num
    for x, data in enumerate(temp[0]):
        if x % 2 != 0:
            continue
        if data <= light_num and light_num <= temp[0][x+1]:
            to_add = light_num - data
            temp_num = temp[1][x] + to_add
    if temp_num == float("-inf"):
        temp_num = light_num
    for x, data in enumerate(humid[0]):
        if x % 2 != 0:
            continue
        if data <= temp_num and temp_num <= humid[0][x+1]:
            to_add = temp_num - data
            humid_num = humid[1][x] + to_add
    if humid_num == float("-inf"):
        humid_num = temp_num
    for x, data in enumerate(loc[0]):
        if x % 2 != 0:
            continue
        if data <= humid_num and humid_num <= loc[0][x+1]:
            to_add = humid_num - data
            location = loc[1][x] + to_add
    if location == float("-inf"):
        location = humid_num
    return location


def create_map(input: list, dest_category: str, next_category: str = None) -> list:
    start_index = 0
    end_index = len(input)
    for index, line in enumerate(input):
        if line == dest_category:
            start_index = index+1
        elif line == next_category:
            end_index = index-1
            break
    dest_nums = []
    orig_nums = []
    for index in range(start_index, end_index):
        temp = input[index].split(" ")
        dest_nums.append(int(temp[0]))
        dest_nums.append(int(temp[0])+(int(temp[2])-1))
        orig_nums.append(int(temp[1]))
        orig_nums.append(int(temp[1])+(int(temp[2])-1))
    return [orig_nums, dest_nums]


if __name__ == "__main__":
    input_txt = get_input()
    seeds = get_seeds(input_txt)

    # maps
    soil_map = create_map(input_txt, "seed-to-soil map:",
                          "soil-to-fertilizer map:")
    fertilizer_map = create_map(
        input_txt, "soil-to-fertilizer map:", "fertilizer-to-water map:")
    water_map = create_map(
        input_txt, "fertilizer-to-water map:", "water-to-light map:")
    light_map = create_map(input_txt, "water-to-light map:",
                           "light-to-temperature map:")
    temperature_map = create_map(
        input_txt, "light-to-temperature map:", "temperature-to-humidity map:")
    humidity_map = create_map(
        input_txt, "temperature-to-humidity map:", "humidity-to-location map:")
    location_map = create_map(input_txt, "humidity-to-location map:")

    # finding smallest loc
    smallest_loc = float("inf")
    for seed in seeds:
        start_number = seed["seed_num"][0]
        end_number = seed["seed_num"][1] + 1
        for seed_no in range(start_number, end_number):
            loc = find_location(seed_no, soil_map, fertilizer_map, water_map,
                                light_map, temperature_map, humidity_map, location_map)
            print(loc)
            if loc < smallest_loc:
                smallest_loc = loc
    print(f"smallest location: {smallest_loc}")
