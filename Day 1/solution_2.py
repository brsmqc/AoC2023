input_list = []
with open("Day 1\\input.txt","r") as input:
    while True:
        line = input.readline()
        if line != "":
            input_list.append(line)
        else:
            break

num_list = []
for item in input_list:
    nums = []
    while len(item) > 0:
        if item[0] in ["0","1","2","3","4","5","6","7","8","9"]:
            nums.append(item[0])
        elif 3 < len(item) and item[0:3] in ["one", "two", "six"]:
            if item[0:3] == "one": nums.append("1")
            elif item[0:3] == "two": nums.append("2")
            else: nums.append("6")
        elif 4 < len(item) and item[0:4] in ["four", "five", "nine", "zero"]:
            if item[0:4] == "four": nums.append("4")
            elif item[0:4] == "five": nums.append("5")
            elif item[0:4] == "nine": nums.append("9")
            else: nums.append("0")
        elif 5 < len(item) and item[0:5] in ["three", "seven", "eight"]:
            if item[0:5] == "three": nums.append("3")
            elif item[0:5] == "seven": nums.append("7")
            else: nums.append("8")
        item = item[1:]
    num = nums[0] + nums[-1]
    num_list.append(num)

total = 0
[total := total + int(num) for num in num_list]

print(total)
