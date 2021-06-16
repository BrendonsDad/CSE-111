from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name('Jo', 'Mo') == 'Mo; Jo'
    assert make_full_name('Sally', 'Brown') == 'Brown; Sally'
    assert make_full_name('Scarlett', 'Jo\'hanson') == 'Jo\'hanson; Scarlett'
    assert make_full_name('A\'daviant', 'Jones') == 'Jones; A\'daviant'
    assert make_full_name('B\'ig', 'Chu\'ngus') == 'Chu\'ngus; B\'ig'
    assert make_full_name('Leonardo', 'Dicaprio') == 'Dicaprio; Leonardo'
    assert make_full_name('Aubury', 'Orr') == 'Orr; Aubury'
    # assert make_full_name('', '') == ''
    # assert make_full_name('', '') == ''



def test_extract_family_name():
    assert extract_family_name('Orr; Aubury') == 'Orr'
    assert extract_family_name('Brown; Sally') == 'Brown'
    assert extract_family_name('Mo; Jo') == 'Mo'
    assert extract_family_name('Jo\'hanson; Scarlett') == 'Jo\'hanson'
    assert extract_family_name('Jones; A\'daviant') == 'Jones'
    assert extract_family_name('Chu\'ngus; B\'ig') == 'Chu\'ngus'
    assert extract_family_name('Dicaprio; Leonardo') == 'Dicaprio'
    # assert extract_family_name('', '') == ''
    # assert extract_family_name('', '') == ''


def test_extract_given_name():
    assert extract_given_name('Orr; Aubury') == 'Aubury'
    assert extract_given_name('Brown; Sally') == 'Sally'
    assert extract_given_name('Mo; Jo') == 'Jo'
    assert extract_given_name('Jo\'hanson; Scarlett') == 'Scarlett'
    assert extract_given_name('Jones; A\'daviant') == 'A\'daviant'
    assert extract_given_name('Chu\'ngus; B\'ig') == 'B\'ig'
    assert extract_given_name('Dicaprio; Leonardo') == 'Leonardo'
    # assert extract_family_name('', '') == ''
    # assert extract_family_name('', '') == ''



# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])