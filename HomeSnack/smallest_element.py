numbers = [21,45,24,76,67,3,28,06,246,35]

smallest = numbers[0]

for number in numbers:

    if number < smallest:
        smallest = number

print(smallest)
