REQ_PARAMS = [
    'byr:',
    'iyr:',
    'eyr:',
    'hgt:',
    'hcl:',
    'ecl:',
    'pid:',
]


def validate_document(input_file):
    valid_count = 0
    with open(input_file, 'r') as f:
        content = f.read()

    content = content.split('\n\n')

    for document in content:
        if all(param in document for param in REQ_PARAMS):
            valid_count += 1

    return f'Number of valid documents: {valid_count}'


if __name__ == '__main__':
    print(validate_document('entry_file.txt'))
