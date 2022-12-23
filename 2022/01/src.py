def get_calories(file_name: str):
    with open(file_name) as file:
        data = file.read().split('\n\n')
        return list(map(sum_elf_calories, data))


def get_max_calories(file_name) -> int:
    calories_list = get_calories(file_name)
    return max(calories_list)


def get_sum_of_last_three(file_name) -> int:
    calories_list = get_calories(file_name)
    calories_list.sort()
    return sum(calories_list[-3:])


def sum_elf_calories(elf) -> int:
    lst = [int(x) for x in elf.split()]
    return sum(lst)


if __name__ == '__main__':
    assert get_max_calories('input_test.txt') == 24000
    assert get_sum_of_last_three('input_test.txt') == 45000
    print(get_max_calories("input.txt"))
    print(get_sum_of_last_three("input.txt"))
