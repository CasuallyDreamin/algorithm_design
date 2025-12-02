from .solution import max_auction_profit 

def test_max_auction_profit():
    B1 = [
        [10, 5], 
        [2, 8]
    ]
    expected_profit_1 = 18
    expected_assignment_1 = [(0, 0), (1, 1)]
    profit_1, assignment_1 = max_auction_profit(B1)
    
    assert profit_1 == expected_profit_1, f"Case 1 Failed (Profit). Expected {expected_profit_1}, got {profit_1}"
    assert assignment_1 == expected_assignment_1, f"Case 1 Failed (Assignment). Expected {expected_assignment_1}, got {assignment_1}"

    B2 = [
        [10, 5, 1], 
        [5, 10, 1], 
        [1, 1, 10]
    ]
    expected_profit_2 = 30
    expected_assignment_2 = [(0, 0), (1, 1), (2, 2)]
    profit_2, assignment_2 = max_auction_profit(B2)
    
    assert profit_2 == expected_profit_2, f"Case 2 Failed (Profit). Expected {expected_profit_2}, got {profit_2}"
    assert assignment_2 == expected_assignment_2, f"Case 2 Failed (Assignment). Expected {expected_assignment_2}, got {assignment_2}"

    B3 = [
        [1, 2, 3],
        [3, 1, 2], 
        [2, 3, 1]
    ]
    expected_profit_3 = 9
    expected_assignment_3 = [(0, 2), (1, 0), (2, 1)]
    profit_3, assignment_3 = max_auction_profit(B3)

    assert profit_3 == expected_profit_3, f"Case 3 Failed (Profit). Expected {expected_profit_3}, got {profit_3}"
    assert assignment_3 == expected_assignment_3, f"Case 3 Failed (Assignment). Expected {expected_assignment_3}, got {assignment_3}"

    B4 = [
        [20, 0, 0, 0],
        [0, 5, 15, 0],
        [0, 10, 0, 0],
        [0, 0, 0, 5]
    ]
    expected_profit_4 = 50
    expected_assignment_4 = [(0, 0), (1, 2), (2, 1), (3, 3)]
    profit_4, assignment_4 = max_auction_profit(B4)

    assert profit_4 == expected_profit_4, f"Case 4 Failed (Profit). Expected {expected_profit_4}, got {profit_4}"
    assert assignment_4 == expected_assignment_4, f"Case 4 Failed (Assignment). Expected {expected_assignment_4}, got {assignment_4}"
    
    B5 = []
    expected_profit_5 = 0
    expected_assignment_5 = []
    profit_5, assignment_5 = max_auction_profit(B5)
    
    assert profit_5 == expected_profit_5, f"Case 5 Failed (Profit). Expected {expected_profit_5}, got {profit_5}"
    assert assignment_5 == expected_assignment_5, f"Case 5 Failed (Assignment). Expected {expected_assignment_5}, got {assignment_5}"


    print("All Branch and Bound Auction Solver test cases passed successfully!")

if __name__ == "__main__":
    try:
        test_max_auction_profit()
    except AssertionError as e:
        print(f"Tests failed: {e}")