import add

def test_add_1():
    assert add.add(1,2) == 3

def test_add_1():
    assert add.add(5,5) == 10

def test_add_1():
    assert add.add(0,50000) == 50000

def test_add_1():
    assert add.add(50000,123) == 50123

def test_add_1():
    assert add.add(123,321) == 444

def test_add_1():
    assert add.add(1000,2000) == 3000

def test_add_1():
    assert add.add(14,7) == 21

def test_add_1():
    assert add.add(21,60) == 81

def test_add_1():
    assert add.add(33,44) == 77

def test_add_1():
    assert add.add(11,12) == 23

def test_add_1():
    assert add.add(11,333) == 344