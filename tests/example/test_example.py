import pytest


def test_example1():
    print('Printing for test')
    assert 1 == 1


# pytest.mark.skip -> skip this test
@pytest.mark.skip
def test_example2():
    assert 1 == 1


# pytest.mark.xfail -> shows that test will fail
@pytest.mark.xfail
def test_example3():
    assert 1 == 2


# смотреть markers в pytest.ini
@pytest.mark.example
def test_example4():
    assert 1 == 1
