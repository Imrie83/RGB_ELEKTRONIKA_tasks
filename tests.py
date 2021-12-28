import pytest
from safe_code_validation import check_code
from document_validation import validate_document


def test_check_code_1():
    assert check_code(123456, 123467) == 1


def test_check_code_2():
    assert check_code(123456, 123477) == 2


def test_check_code_3():
    assert check_code(123456, 123465) == 0


def file_1(fname):
    with open(fname, 'w') as fp:
        fp.write('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm')


def file_2(fname):
    with open(fname, 'w') as fp:
        fp.write('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147')


def file_3(fname):
    with open(fname, 'w') as fp:
        fp.write(
            """
            ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm\n
            
            iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884hcl:#cfa07d byr:1929\n
            
            hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm\n
            
            hcl:#cfa07d eyr:2025 pid:166559648iyr:2011 ecl:brn hgt:59in\n
            """
        )


def test_document_valid_1(tmpdir):
    file = tmpdir.join('output.txt')
    file_1(file.strpath)

    assert validate_document(file) == f'Number of valid documents: 1'


def test_document_valid_2(tmpdir):
    file = tmpdir.join('output.txt')
    file_2(file.strpath)

    assert validate_document(file) == f'Number of valid documents: 0'


def test_document_valid_3(tmpdir):
    file = tmpdir.join('output.txt')
    file_3(file.strpath)

    assert validate_document(file) == f'Number of valid documents: 2'
