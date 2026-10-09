def add_every_third(numbers):

    amount = 0

    for number in range(2, len(numbers), 3):
        total = total + numbers[number]

    return amount


numbers = [21,45,24,76,67,3,28,06,246,35]

answer = add_every_third(numbers)

print(answer)
