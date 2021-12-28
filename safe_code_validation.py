def check_code(start=265275, end=781584):

    valid_count = 0

    for i in range(start, end + 1):
        if all(a <= b for a, b in zip(str(i), str(i)[1:])) and \
                any(a == b for a, b in zip(str(i), str(i)[1:])):
            valid_count += 1
    return valid_count


if __name__ == '__main__':
    print(f'Valid codes in given range: {check_code()}')
