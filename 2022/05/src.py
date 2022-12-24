import copy

test_list = [None, ['Z', 'N'], ['M', 'C', 'D'], ['P']]
actual_list = [
    None,
    ['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],
    ['L', 'D', 'Z', 'Q', 'W', 'V'],
    ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],
    ['R', 'D', 'H', 'F', 'J', 'V', 'B'],
    ['Z', 'W', 'L', 'C'],
    ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
    ['J', 'R', 'L', 'V', 'M', 'B', 'S'],
    ['D', 'P', 'J'],
    ['D', 'C', 'N', 'W', 'V'],
]


def rearrange_list(file_name: str, list_to_rearrange, f) -> str:
    def parse_commands(commands: str):
        commands = commands.split(' ')
        return int(commands[1]), int(commands[3]), int(commands[5])

    temp_list = copy.deepcopy(list_to_rearrange)

    with open(file_name, 'rt') as file:
        data = file.read().split('\n')
        index_to_get_commands = data.index('') + 1
        data = data[index_to_get_commands:]
        parsed_commands = list(map(parse_commands, data))

    for command in parsed_commands:
        temp_list[command[2]] += f(temp_list[command[1]][-command[0]:])
        del temp_list[command[1]][-command[0]:]

    return ''.join([elem[-1] for elem in temp_list if elem is not None])


if __name__ == '__main__':
    assert rearrange_list('input_test.txt', test_list, reversed) == 'CMZ'
    assert rearrange_list('input_test.txt', test_list, lambda x: x) == 'MCD'
    print('A solution: ', rearrange_list('input.txt', actual_list, reversed))
    print('B solution: ', rearrange_list('input.txt', actual_list, lambda x: x))
