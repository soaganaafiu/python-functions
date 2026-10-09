numbers = [21,45,24,76,67,3,28,06,246,35]

add = 0

for number in range (len(numbers)):

    if numbers[number] % 2 == 0:

        add = add + numbers[number]


print(add)
