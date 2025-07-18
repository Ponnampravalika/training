def add(a, b):
    return a + b
 
def test_add_numbers():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
if __name__ == "__main__":
    test_add_numbers()
    print("All tests passed!")