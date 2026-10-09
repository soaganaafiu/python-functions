def square_list(numbers):

    square_list = []
    
    for number in numbers:

        square = number * number
        

        square_list.append(square)

    return square_list

number_list = [2,3,4,5,7]

print(square_list(number_list))
