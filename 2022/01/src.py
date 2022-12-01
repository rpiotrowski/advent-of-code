def get_max_calories(file_name: str):
    with open(file_name) as file:
        data = file.read().split('\n\n')
        calories_sum = list(map(sum_elf_calories, data))
        print(max(calories_sum))
        calories_sum.sort()
        print(sum(calories_sum[-3:]))


def sum_elf_calories(elf) -> int:
    lst = [int(x) for x in elf.split()]
    return sum(lst)


if __name__ == '__main__':
    get_max_calories("input.txt")
