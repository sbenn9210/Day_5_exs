#function to demonstrate printing pattern of triangle
#def triangle(n):
    # number of spaces

    # outer loop to handle number of rows

        # inner loop to handle number of spaces
        # values changing acc. to requirment

        # decrementing k after each loop

        # inner loop to handle number of columns
        # values changing acc. to outer loop

            #     printing stars

        # ending line after each row
num = int(input("Enter the number of rows: "))
for i in range(0, num):
    for j in range(0, num-i-1):
        print(end=" ")
    for j in range(0, i+1):
        print("*", end="*")
    print()
