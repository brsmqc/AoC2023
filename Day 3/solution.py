numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = []
engine_schematic = []
part_numbers = []

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
print(symbols)

for y, data in enumerate(engine_schematic):
    new_x = 0
    for x, char in enumerate(data):
        if x < new_x:
            continue
        if char == "." or char in symbols:
            continue
        if x + 2 <= len(data)-1 and data[x+2] in numbers and data[x+1] in numbers:
            for look_y in range(max(y-1, 0),min(y+2, len(engine_schematic))):
                for look_x in range(max(x-1, 0), min(x+4, len(data))):
                    if engine_schematic[look_y][look_x] in symbols:
                        part_numbers.append(data[x:x+3])
                        break
            new_x = x + 3
            continue
        elif x + 1 <= len(data)-1 and data[x+1] in numbers:
            for look_y in range(max(y-1, 0),min(y+2, len(engine_schematic))):
                for look_x in range(max(x-1, 0), min(x+3, len(data))):
                    if engine_schematic[look_y][look_x] in symbols:
                        part_numbers.append(data[x:x+2])
                        break
            new_x = x + 2
            continue
        elif char in numbers:
            for look_y in range(max(y-1, 0),min(y+2, len(engine_schematic))):
                for look_x in range(max(x-1, 0), min(x+2, len(data))):
                    if engine_schematic[look_y][look_x] in symbols:
                        part_numbers.append(data[x])

for index, part in enumerate(part_numbers):
    try: 
        int(part)
    except:
        print(f"found {part} at index: {index}")
print(part_numbers)

total = 0
[total := total + int(num) for num in part_numbers]
print(total)