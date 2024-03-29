import centuryFromYear

def test_centuryFromYear_1():
    assert centuryFromYear.centuryFromYear(1) == 1

def test_centuryFromYear_2():
    assert centuryFromYear.centuryFromYear(100) == 1

def test_centuryFromYear_3():
    assert centuryFromYear.centuryFromYear(101) == 2

def test_centuryFromYear_4():
    assert centuryFromYear.centuryFromYear(1700) == 17

def test_centuryFromYear_5():
    assert centuryFromYear.centuryFromYear(1901) == 20

def test_centuryFromYear_6():
    assert centuryFromYear.centuryFromYear(2000) == 20

def test_centuryFromYear_7():
    assert centuryFromYear.centuryFromYear(1234) == 13

def test_centuryFromYear_8():
    assert centuryFromYear.centuryFromYear(500) == 5