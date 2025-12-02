from data_structures.core.matrix import Matrix
from problems.second.problem_1.solution import get_largest_area

def init_matrix(input_data: list[list[int]]) -> Matrix:
    r = len(input_data)
    c = len(input_data[0]) if r > 0 else 0

    game_matrix = Matrix(r, c)

    for i in range(r):
        for j in range(c):
            game_matrix[i, j] = input_data[i][j]
    
    return game_matrix

def test_get_largest_area():
    
    matrix_data_1 = [
        [1, 1, 0, 2, 2],
        [1, 1, 0, 2, 0],
        [0, 0, 3, 0, 0],
        [0, 0, 0, 5, 5],
        [4, 0, 5, 5, 5]
    ]
    game_matrix_1 = init_matrix(matrix_data_1)
    winner_1, size_1 = get_largest_area(game_matrix_1)
    
    assert winner_1 == 5 and size_1 == 5, f"Case 1 Failed: Expected (5, 5), got ({winner_1}, {size_1})"
    
    matrix_data_2 = [
        [1, 1],
        [1, 1]
    ]
    game_matrix_2 = init_matrix(matrix_data_2)
    winner_2, size_2 = get_largest_area(game_matrix_2)
    
    assert winner_2 == 1 and size_2 == 4, f"Case 2 Failed: Expected (1, 4), got ({winner_2}, {size_2})"
    
    matrix_data_3 = [
        [1, 1, 0],
        [2, 2, 2]
    ]
    game_matrix_3 = init_matrix(matrix_data_3)
    winner_3, size_3 = get_largest_area(game_matrix_3)
    
    assert winner_3 == 2 and size_3 == 3, f"Case 3 Failed: Expected (2, 3), got ({winner_3}, {size_3})"

    matrix_data_4 = [
        [1, 1, 0],
        [0, 0, 3],
        [1, 1, 0]
    ]
    game_matrix_4 = init_matrix(matrix_data_4)
    winner_4, size_4 = get_largest_area(game_matrix_4)
    
    assert winner_4 == 1 and size_4 == 2, f"Case 4 Failed: Expected (1, 2), got ({winner_4}, {size_4})"
    
    return "All tests passed successfully!"

if __name__ == "__main__":
    try:
        print(test_get_largest_area())
    except AssertionError as e:
        print(f"Tests failed: {e}")