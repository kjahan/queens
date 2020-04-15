import pytest

import src.helper as helper

@pytest.fixture
def A_mock():
    return [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def test_check_all_rows_should_pass(A_mock):
    A_mock[0][0] = 1
    A_mock[1][2] = 1
    assert helper.check_all_rows(A_mock)

def test_check_all_rows_with_two_queens_in_one_row(A_mock):
    A_mock[0][0] = 1
    A_mock[0][2] = 1
    assert not helper.check_all_rows(A_mock)

def test_check_all_columns_should_pass(A_mock):
    A_mock[0][0] = 1
    A_mock[1][2] = 1
    assert helper.check_all_columns(A_mock)

def test_check_all_rows_with_two_queens_in_one_column(A_mock):
    A_mock[0][0] = 1
    A_mock[1][0] = 1
    assert not helper.check_all_columns(A_mock)

def test_check_all_diagonals_should_pass(A_mock):
    A_mock[0][0] = 1
    A_mock[1][2] = 1
    assert helper.check_all_diagonals(A_mock)

def test_check_all_diagonals_with_two_queens_on_diagonal(A_mock):
    A_mock[1][0] = 1
    A_mock[0][1] = 1
    assert not helper.check_all_diagonals(A_mock)

def test_check_all_columns_should_pass(A_mock):
    A_mock[1][3] = 1
    A_mock[2][2] = 1
    A_mock[3][1] = 1
    assert not helper.check_all_diagonals(A_mock)
