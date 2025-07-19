'''
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.

'''

num1=int(input("Enter a number: "))

if num1%2 == 0:
    print(("{} is an even number").format(num1))
else:
    print(("{} is an odd number").format(num1))

#Result
#Enter a number: 105
#105 is an odd number