from .solution import skyline_solver 

def test_skyline_solver():
    rectangles_1 = [(1, 5, 5)]
    expected_1 = [(1, 5), (5, 0)]
    result_1 = skyline_solver(rectangles_1)
    assert result_1 == expected_1, f"Case 1 Failed (Single Building). Expected {expected_1}, got {result_1}"

    rectangles_2 = [(1, 5, 11), (2, 7, 6), (8, 10, 8)]
    expected_2 = [(1, 11), (5, 6), (7, 0), (8, 8), (10, 0)]
    result_2 = skyline_solver(rectangles_2)
    assert result_2 == expected_2, f"Case 2 Failed (Standard Overlap). Expected {expected_2}, got {result_2}"

    rectangles_3 = [(1, 8, 4), (2, 6, 8)]
    expected_3 = [(1, 4), (2, 8), (6, 4), (8, 0)]
    result_3 = skyline_solver(rectangles_3)
    assert result_3 == expected_3, f"Case 3 Failed (Contained). Expected {expected_3}, got {result_3}"

    rectangles_4 = [(1, 5, 5), (5, 10, 5)]
    expected_4 = [(1, 5), (10, 0)]
    result_4 = skyline_solver(rectangles_4)
    assert result_4 == expected_4, f"Case 4 Failed (Adjacent Merge). Expected {expected_4}, got {result_4}"

    rectangles_5 = [(0, 2, 3), (1, 4, 6), (3, 7, 9), (5, 8, 5)]
    expected_5 = [(0, 3), (1, 6), (3, 9), (7, 5), (8, 0)]
    result_5 = skyline_solver(rectangles_5)
    assert result_5 == expected_5, f"Case 5 Failed (Complex). Expected {expected_5}, got {result_5}"

    print("All Skyline Solver test cases passed successfully!")

if __name__ == "__main__":
    try:
        test_skyline_solver()
    except AssertionError as e:
        print(f"Tests failed: {e}")