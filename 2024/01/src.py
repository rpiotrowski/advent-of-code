import re

def test_calculate_distance_and_occurences(file_path: str):
    assert calculate_distance_and_occurences(file_path='test_input.txt') == (11, 31)


def calculate_distance_and_occurences(file_path: str) -> int:
    distance = 0
    occurences = 0
    a = []
    b = []
    
    with open(file_path) as file:
        for line in file.readlines():
            numbers = re.findall(r'\d+', line)
            a.append(numbers[0]) 
            b.append(numbers[1])

    a.sort()
    b.sort()
    for elem_a, elem_b in zip(a,b):
        distance += abs(int(elem_a)-int(elem_b))
        occurences += int(elem_a) * b.count(elem_a)

    return distance, occurences




if __name__ == '__main__':
    test_calculate_distance_and_occurences('test_input.txt')
    print(calculate_distance_and_occurences('input.txt'))