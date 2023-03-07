# FizzBuzz program
#STEP 2 : improve efficiency 
# made change on line 6 - more efficient

for i in range(1, 101): 
    if (i % 15 == 0):
        print("FizzBuzz")
    elif(i % 3 == 0):
        print("Fizz")
    elif(i % 5 ==  0):
        print("Buzz")
    else:
        print(i)


