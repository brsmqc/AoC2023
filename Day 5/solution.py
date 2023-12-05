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
    start_index = 0
    end_index = len(input)
    for index, line in enumerate(input):
        if line == search_text:
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
    # input = input[end_index+1:]

    for seed in seed_list:
        for x, num in enumerate(orig_nums):
            if x % 2 != 0:
                continue
            if (num <= seed[curr_category]) and (seed[curr_category] <= (orig_nums[x+1])):
                to_add = seed[curr_category] - num
                seed[dest_category] = dest_nums[x] + to_add
        if not dest_category in seed.keys():
            seed[dest_category] = seed[curr_category]

if __name__ == "__main__":
    input = get_input()
    seeds = get_seeds(input)
    map_item(input, seeds, "seed-to-soil map:", "seed_num", "soil", "soil-to-fertilizer map:")
    map_item(input, seeds, "soil-to-fertilizer map:", "soil", "fertilizer", "fertilizer-to-water map:")
    map_item(input, seeds, "fertilizer-to-water map:", "fertilizer", "water", "water-to-light map:")
    map_item(input, seeds, "water-to-light map:", "water", "light", "light-to-temperature map:")
    map_item(input, seeds, "light-to-temperature map:", "light", "temp", "temperature-to-humidity map:")
    map_item(input, seeds, "temperature-to-humidity map:", "temp", "humidity", "humidity-to-location map:")
    map_item(input, seeds, "humidity-to-location map:", "humidity", "location")
    print(seeds)
    
    smallest = float('inf')
    for seed in seeds:
        if seed["location"] < smallest:
            smallest = seed["location"]
    
    print(smallest)