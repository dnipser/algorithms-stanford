
def read_input_dataset(dir, file_name):
    input_dataset = []

    path = '{}{}'.format(dir, file_name)
    with open(path) as f:
        for line in f:
            input_dataset.append(int(line))

    return input_dataset
