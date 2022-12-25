import functools


def print_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        print(value)
        return value

    return wrapper


@print_result
def find_marker_index(file_name: str, str_length: int) -> int:
    with open(file_name) as file:
        data = file.read()
        for i in range(str_length, len(data)):
            temp_set = set(data[i-str_length:i])
            if len(temp_set) == str_length:
                return i


if __name__ == '__main__':
    assert find_marker_index('input_test.txt', 4) == 11
    assert find_marker_index('input_test.txt', 14) == 26
    find_marker_index('input.txt', 4)
    find_marker_index('input.txt', 14)
