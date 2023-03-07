# FizzBuzz program
#STEP 3 : improve readability


#loop through numbers 1-100, same functionality to example below in other languages
for i in range(1, 101): 
    if (i % 15 == 0):
        print("FizzBuzz")
        #if number is divisible by 3 and 5 print out "FizzBuzz"
    elif(i % 3 == 0):
        print("Fizz")
        #if number is  divisible by 3 print "Fizz"
    elif(i % 5 ==  0):
        print("Buzz")
        #if number is divisible by 5 print "Buzz"
    else:
        print(i)
        #if number is not divisible by either, print the nunber
        
        
        
#similar loop functionality as seen in c or java
# for (int i = 0; i <= 100; i++){
   # ........    
#}
