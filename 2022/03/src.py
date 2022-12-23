UPPER_SUB = 38
LOWER_SUB = 96


def get_priority(char: str) -> int:
    if char.isupper():
        return ord(char) - UPPER_SUB
    else:
        return ord(char) - LOWER_SUB


def count_priority(file: str) -> int:
    with open(file, 'rt') as file:
        data = file.read().split('\n')
        partitioned_data = [list(set(elem[0:len(elem) // 2]).intersection(set(elem[len(elem) // 2:])))[0] for elem in
                            data]
        print(partitioned_data)
        return sum([get_priority(elem) for elem in partitioned_data])


def count_priority_2(file: str) -> int:
    with open(file, 'rt') as file:
        data = file.read().split('\n')
        partitioned_data = []
        for i in range(0, len(data), 3):
            partitioned_data.append(list(set(data[i]) & set(data[i + 1]) & set(data[i + 2]))[0])
        print(partitioned_data)
        return sum([get_priority(elem) for elem in partitioned_data])


if __name__ == '__main__':
    assert count_priority('input_test.txt') == 157
    assert count_priority_2('input_test.txt') == 70
    print(count_priority('input.txt'))
    print(count_priority_2('input.txt'))
