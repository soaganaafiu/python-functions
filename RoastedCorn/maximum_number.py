
def maximum_number(numbers):

    maximum = numbers[0]

    for number in numbers:


        if number > maximum:

            maximum = number


    return maximum



number_list = [4,3,7,5,9,0,1]
print(maximum_number(number_list))
