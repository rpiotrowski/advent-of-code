import re
    
def test_count_safe_reports(file_path: str):
    assert count_safe_reports(file_path) == 4

def is_sorted(lst: dict) -> bool:
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

def is_adjacent(lst: dict) -> bool:
    """Diff is between 1 to 3"""
    for i in range(len(lst) - 1):
        diff = abs(lst[i] - lst[i+1])
        if not (1 <= diff <= 3):
            return False
    return True

def count_safe_reports(file_path: str):
    count = 0
    with open(file_path) as file:
        for line in file.readlines():
            numbers = list(map(int, re.findall(r'\d+', line)))
            for i in range(len(numbers)):
                sublist = numbers[:i] + numbers[i+1:]
                if is_sorted(sublist) and is_adjacent(sublist):
                    count += 1
                    break
    return count


if __name__ == '__main__':
    test_count_safe_reports('test_input.txt')
    print(count_safe_reports('input.txt'))