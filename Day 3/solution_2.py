import re

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = []
engine_schematic = []
ratios = []


def find_above(line_above: str, index: int) -> int | list | None:
    if line_above[max(index-1, 0)] == ".":
        if line_above[min(index+1, len(line_above)-1)] == ".":
            if line_above[index] in symbols or line_above[index] == ".":
                return None
            return int(line_above[index])
        num = re.search("\\d+", line_above[index:])
        if num == None:
            return None
        return int(num.group(0))
    if line_above[min(index+1, len(line_above)-1)] != ".":
        num = re.findall(
            "\\d+", line_above[max(index-3, 0):min(index+4, len(line_above))])
        if len(num) > 1:
            return num
    num = re.findall(
        "\\d+", line_above[max(index-2, 0):min(index+3, len(line_above))])
    if len(num) == 2:
        return int(num[1])
    elif num == None:
        return None
    return int(num[0])


def find_below(line_below: str, index: int) -> int | list |None:
    if line_below[max(index-1, 0)] == ".":
        if line_below[min(index+1, len(line_below)-1)] == ".":
            if line_below[index] in symbols or line_below[index] == ".":
                return None
            return int(line_below[index])
        num = re.search("\\d+", line_below[index:])
        if num == None:
            return None
        return int(num.group(0))
    if line_below[min(index+1, len(line_below)-1)] != ".":
        num = re.findall(
            "\\d+", line_below[max(index-3, 0):min(index+4, len(line_below))])
        if len(num) > 1:
            return num
    num = re.findall(
        "\\d+", line_below[max(index-2, 0):min(index+3, len(line_below))])
    if len(num) == 2:
        return int(num[1])
    if num == None:
        return None
    return int(num[0])


def find_left(line: str, index: int) -> int | None:
    if line[max(index-1, 0)] == ".":
        return None
    num = re.search("\\d+", line[max(index-3, 0):index])
    if num == None:
        return None
    return int(num.group(0))


def find_right(line: str, index: int) -> int | None:
    if line[min(index+1, len(line)-1)] == ".":
        return None
    num = re.search("\\d+", line[index:min(index+4, len(line))])
    if num == None:
        return None
    return int(num.group(0))

#####################
### MAIN FUNCTION ###
#####################

with open("Day 3\\input.txt") as file:
    while True:
        line = file.readline().strip()
        if line == "":
            break
        for char in line:
            if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."] and char not in symbols:
                symbols.append(char)
        engine_schematic.append(line)

# print(engine_schematic)
# print(symbols)

for y, data in enumerate(engine_schematic):
    new_x = 0
    for x, char in enumerate(data):
        if char != "*":
            continue
        above = find_above(engine_schematic[(max(y-1, 0))], x)
        below = find_below(
            engine_schematic[(min(y+1, len(engine_schematic)))], x)
        left = find_left(data, x)
        right = find_right(data, x)
        print(f"line: {y+1} above: {above}, right: {right}, below: {below}, left: {left}")
        ratio = []
        for num in [above, below, left, right]:
            if num != None:
                ratio.append(num)
        if len(ratio) < 1 or len(ratio) > 2:
            pass
        elif len(ratio) == 2 and type(above) != list and type(below) != list:
            ratios.append(ratio[0] * ratio[1])
        elif (type(above) == list and below == None) or (above == None and type(below) == list):
            ratios.append(int(ratio[0][0]) * int(ratio[0][1]))

# print(ratios)
total = 0
[total := total + int(num) for num in ratios]
print(total)
