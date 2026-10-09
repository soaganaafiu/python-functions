def add_first_middle_last(numbers):

    first = numbers[0]

    middle = 0

    last = numbers[-1]

    amount = first + middle + last

    return amount


numbers = [21,45,24,76,67,3,28,06,246,35]

answer = add_first_middle_last(numbers)

print(answer)
