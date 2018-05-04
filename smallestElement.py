numbers = [5655, 1, 2, 3, 7777, 4, 5, 6, 456]


def smallest_number(num):
    init = numbers[0]
    for x in num:
        if x < init:
            init = x
    return init

smallest_num = smallest_number(numbers)

print(smallest_num)
