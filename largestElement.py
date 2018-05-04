numbers = [5655, 1, 2, 3, 7777, 4, 5, 6, 456]

#print a list of the numbers


#identify & print which number is the lastest



def maximum_number(num):
    max = 0
    for num in numbers:
        if num > max:
            max = num
    print(max)

maximum_number(numbers)
