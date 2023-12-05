

INPUT = "Day 5\\input.txt"

def get_input():
    input = ""
    with open(INPUT) as file:
        input = file.read()
    return input.split("\n")

def get_seeds(input:list) -> list:
    seed_line = input[0].split(" ")
    seeds = [{"seed_num":int(seed)} for seed in seed_line if seed != "seeds:"]
    return seeds

def map_item(input:list, seed_list:list, search_text:str, curr_category:str, dest_category:str, next_category:str = None) -> None:
    mappings = []
    start_index = 0
    end_index = len(input)
    for index, line in enumerate(input):
        if line == search_text:
            start_index = index+1
        elif line == next_category:
            end_index = index-1
            break
    map = []
    for index in range(start_index, end_index):
        map.append(input[index].split(" "))
    for item in map:
        translation_range = int(item[2])
        source_start = int(item[1])
        dest_start = int(item[0])
        for x in range(translation_range):
            for seed in seed_list:
                if seed[curr_category] == source_start+x:
                    seed[dest_category] = dest_start+x
                if not dest_category in seed.keys():
                    seed[dest_category] = seed[curr_category]


if __name__ == "__main__":
    input = get_input()
    seeds = get_seeds(input)
    # print(seeds)
    map_item(input, seeds, "seed-to-soil map:", "seed_num", "soil", "soil-to-fertilizer map:")
    map_item(input, seeds, "soil-to-fertilizer map:", "soil", "fertilizer", "fertilizer-to-water map:")
    map_item(input, seeds, "fertilizer-to-water map:", "fertilizer", "water", "water-to-light map:")
    map_item(input, seeds, "water-to-light map:", "water", "light", "light-to-temperature map:")
    map_item(input, seeds, "light-to-temperature map:", "light", "temp", "temperature-to-humidity map:")
    map_item(input, seeds, "temperature-to-humidity map:", "temp", "humidity", "humidity-to-location map:")
    map_item(input, seeds, "humidity-to-location map:", "humidity", "location")
    
    smallest = 1000
    for seed in seeds:
        if seed["location"] < smallest:
            smallest = seed["location"]
    
    print(smallest)