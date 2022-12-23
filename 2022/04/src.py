def is_contain(first_area: str, second_area: str, part) -> int:
    range_1 = first_area.split('-')
    range_2 = second_area.split('-')
    first_set = set(range(int(range_1[0]), int(range_1[1]) + 1))
    second_set = set(range(int(range_2[0]), int(range_2[1]) + 1))
    if part == 'a':
        if first_set.issubset(second_set) or first_set.issuperset(second_set):
            return 1
        else:
            return 0
    else:
        if not first_set.isdisjoint(second_set):
            return 1
        else:
            return 0


def count_containment(file_name: str, part) -> int:
    with open(file_name, 'rt') as file:
        data = file.read().split('\n')
        partitioned_data = [elem.split(',') for elem in data]
        data = list(map(lambda x: is_contain(*x, part), partitioned_data))
        return sum(data)


if __name__ == '__main__':
    assert count_containment('input_test.txt', 'a') == 2
    assert count_containment('input_test.txt', 'b') == 4
    print(count_containment('input.txt', 'a'))
    print(count_containment('input.txt', 'b'))
