# win - 6, draw - 3, lose - 0
# rock - 1, paper - 2, scissors - 3
# A - Rock
# B - Paper
# C - Scissors

RESULT_A = {
    'AX': 4,
    'AY': 8,
    'AZ': 3,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 7,
    'CY': 2,
    'CZ': 6,
}

# X - Lose
# Y - Draw
# Z - Win

RESULT_B = {
    'AX': 3,
    'AY': 4,
    'AZ': 8,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 2,
    'CY': 6,
    'CZ': 7,
}


def count_score(filename: str, strategy) -> int:
    with open(filename) as file:
        data = file.read().split('\n')
        data_cleared = [x.replace(' ', '') for x in data]
        result = sum([strategy[elem] for elem in data_cleared])

        return result


if __name__ == '__main__':
    assert count_score('input_test.txt', RESULT_A) == 15
    assert count_score('input_test.txt', RESULT_B) == 12
    print(count_score('input.txt', RESULT_A))
    print(count_score('input.txt', RESULT_B))
