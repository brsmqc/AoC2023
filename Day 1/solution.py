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
    for char in item:
        if char in ["0","1","2","3","4","5","6","7","8","9"]:
            nums.append(char)
    num = nums[0] + nums[-1]
    num_list.append(num)

total = 0
[total := total + int(num) for num in num_list]

print(total)