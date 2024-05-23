from src import calculate_edge_values


def test_calculate_edge_values():
    assert calculate_edge_values('input_test.txt') == 142
