from .solution import phone_max_depth 

def test_phone_max_depth():

    K1, N1 = 1, 10
    expected1 = 10
    assert phone_max_depth(K1, N1) == expected1, f"Failed K=1, N=10. Expected {expected1}"

    K2, N2 = 2, 10
    expected2 = 4
    assert phone_max_depth(K2, N2) == expected2, f"Failed K=2, N=10. Expected {expected2}"
    
    K3, N3 = 2, 100
    expected3 = 14
    assert phone_max_depth(K3, N3) == expected3, f"Failed K=2, N=100. Expected {expected3}"

    K4, N4 = 3, 25
    expected4 = 5
    assert phone_max_depth(K4, N4) == expected4, f"Failed K=3, N=25. Expected {expected4}"

    print("All phone drop test cases passed!")


if __name__ == "__main__":
    test_phone_max_depth()