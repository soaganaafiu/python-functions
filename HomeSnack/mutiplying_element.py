numbers = [21,45,24,76,67,3,28,06,246,35]

multiplication = 1

for number in range (0, len(numbers), 3):

    multiplication = multiplication * numbers[number]


print(multiplication)
