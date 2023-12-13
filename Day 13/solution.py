INPUT = "Day 13\\test_input.txt"


def get_data(data: str) -> list:
    temp = ""
    with open(data) as file:
        temp = file.read()
    return_list = temp.split("\n")
    return return_list