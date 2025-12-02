from .solution import find_starting_stone 

def test_find_starting_stone():
    stones_1 = [1, 5, 2]
    cost_1 = [0, 3, 1]
    expected_1 = 0
    result_1 = find_starting_stone(stones_1, cost_1)
    assert result_1 == expected_1, f"Case 1 Failed. Expected {expected_1}, got {result_1}"

    stones_2 = [4, 6, 7]
    cost_2 = [5, 4, 3]
    expected_2 = 1
    result_2 = find_starting_stone(stones_2, cost_2)
    assert result_2 == expected_2, f"Case 2 Failed. Expected {expected_2}, got {result_2}"

    stones_3 = [1, 2, 3]
    cost_3 = [2, 3, 1]
    expected_3 = 2
    result_3 = find_starting_stone(stones_3, cost_3)
    assert result_3 == expected_3, f"Case 3 Failed. Expected {expected_3}, got {result_3}"

    stones_4 = [1, 2, 3]
    cost_4 = [3, 3, 3]
    expected_4 = -1
    result_4 = find_starting_stone(stones_4, cost_4)
    assert result_4 == expected_4, f"Case 4 Failed (Impossible). Expected {expected_4}, got {result_4}"

    stones_5 = [5]
    cost_5 = [0]
    expected_5 = 0
    result_5 = find_starting_stone(stones_5, cost_5)
    assert result_5 == expected_5, f"Case 5 Failed (Single Stone). Expected {expected_5}, got {result_5}"

    stones_6 = []
    cost_6 = []
    expected_6 = -1
    result_6 = find_starting_stone(stones_6, cost_6)
    assert result_6 == expected_6, f"Case 6 Failed (Empty). Expected {expected_6}, got {result_6}"

    print("All Magical Stones Circular Path tests passed successfully!")

if __name__ == "__main__":
    try:
        test_find_starting_stone()
    except AssertionError as e:
        print(f"Tests failed: {e}")