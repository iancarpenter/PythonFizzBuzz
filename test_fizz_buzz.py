import pytest
from fizz_buzz import fizz_buzz_if_calc, fizz_buzz_using_boolean


@pytest.fixture
def expected_number_of_elements():
    """The fizzbuzz list will have 100 elements"""
    return 100


@pytest.fixture
def fizzbuzz_expected_answer():
    """A list of the fizzbuzz answers for 1 - 100"""
    fizz_buzz = [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz', 16, 17, 'fizz', 19, 'buzz', 'fizz', 22, 23, 'fizz', 'buzz', 26, 'fizz', 28, 29, 'fizzbuzz', 31, 32, 'fizz', 34, 'buzz', 'fizz', 37, 38, 'fizz', 'buzz', 41, 'fizz', 43, 44, 'fizzbuzz', 46, 47, 'fizz', 49, 'buzz', 'fizz', 52, 53, 'fizz', 'buzz', 56, 'fizz', 58, 59, 'fizzbuzz', 61, 62, 'fizz', 64, 'buzz', 'fizz', 67, 68, 'fizz', 'buzz', 71, 'fizz', 73, 74, 'fizzbuzz', 76, 77, 'fizz', 79, 'buzz', 'fizz', 82, 83, 'fizz', 'buzz', 86, 'fizz', 88, 89, 'fizzbuzz', 91, 92, 'fizz', 94, 'buzz', 'fizz', 97, 98, 'fizz', 'buzz']
    
    return fizz_buzz


def test_fizz_buzz_if_calc_has_100_elements(expected_number_of_elements):
    
    actual = fizz_buzz_if_calc()

    assert len(actual) == expected_number_of_elements


def test_fizz_buzz_using_boolean_has_100_elements(expected_number_of_elements):
    
    actual = fizz_buzz_using_boolean()
    
    assert len(actual) == expected_number_of_elements


def test_fizz_buzz_if_calc_has_correct_items(fizzbuzz_expected_answer):
    
    actual = fizz_buzz_if_calc()

    assert actual == fizzbuzz_expected_answer


def test_fizz_buzz_using_boolean_has_correct_items(fizzbuzz_expected_answer):
    
    actual = fizz_buzz_using_boolean()

    assert actual == fizzbuzz_expected_answer
    