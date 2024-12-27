import re

def test_calculate(file_path):
    calculate(file_path) == 161

def calculate(file_path):
    result = 0
    with open(file_path) as file:
        equation = 'do()' + file.read()
        print(equation)
        mul_parts = re.findall(r'(?=do\(\).*mul\(\d+,\d+\))(?!.*don\'t\(\)).*', equation)
        print(mul_parts)
        for part in mul_parts:
            parts = list(map(int, re.findall(r'\d+', part)))
            a, b = parts[-2], parts[-1]
            result += a*b
    return result

if __name__ == '__main__':
    print(calculate('test_input2.txt'))
    test_calculate('test_input.txt')