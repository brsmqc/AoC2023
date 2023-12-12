INPUT = "Day 9\\input.txt"


def get_data(data: str) -> list:
    temp = ""
    with open(data) as file:
        temp = file.read()
    return_list = temp.split("\n")
    return return_list


def format_data(data: list) -> list:
    value_list = []
    for line in data:
        values = [int(value) for value in line.split(" ")]
        value_list.append(values)
    return value_list


def predict_previous_value(history: list) -> int:
    if sum(history) == 0:
        return 0
    next_sequence = []
    for idx, value in enumerate(history):
        if idx == len(history) - 1:
            break
        difference = history[idx + 1] - value
        next_sequence.append(difference)
    next_value = predict_previous_value(next_sequence)
    new_value = history[0] - next_value
    return new_value


if __name__ == "__main__":
    data = get_data(INPUT)
    eco_data = format_data(data)
    # print(eco_data)
    extrapolations = []
    for series in eco_data:
        extrapolation = predict_previous_value(series)
        extrapolations.append(extrapolation)
    sum_of_extraps = sum(extrapolations)
    print(f"sum of extrapolations: {sum_of_extraps}")
