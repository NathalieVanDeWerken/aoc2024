
def read_input_list_int(data):
    data_parsed = []
    for element in data:
        data_parsed.append(int(element))
    return data_parsed


def read_input_list_line(data):
    data_parsed = []
    for element in data:
        data_parsed.append(element.strip("\n"))
    return data_parsed

def read_input_list_of_lists(data):
    data_parsed = []
    for element in data.split("\n"):
        data_parsed.append([int(x) for x in element.split()])
    return data_parsed
