def calculate_edge_values(file_name: str):
    with open(file_name) as file:
        lines = [line.strip() for line in file]
        print(lines)


calculate_edge_values('input_test.txt')
