def sum_of_square(numbers):

    square_addition = 0

    for number in numbers:

        square = number * number

        square_addition += square


    return square_addition




number_list = [2,3,4,5,7]
print(sum_of_square(number_list))
