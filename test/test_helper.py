import pytest

from src.helper import check_rows

@pytest.fixture
def A_mock():
    return [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def test_check_rows_should_pass(A_mock):
    A_mock[0][0] = 1
    A_mock[1][2] = 1
    assert check_rows(A_mock)

def test_check_rows_with_two_queens_in_first_row(A_mock):
    A_mock[0][0] = 1
    A_mock[0][2] = 1
    assert not check_rows(A_mock)