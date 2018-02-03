
#To to find triplets in the list which gives the sum of zero.

def sumOfZero(Numbers_Entered, Number): # declaring a funtion

    Num = True # if the funtion is True start the loop

    """ for each of x, y and z will check each others matching numbers until the the three x,y and z sum is zero """
    for x in range(0, Number - 2): # starting with x

        for y in range(x + 1, Number - 1): # then y

            for z in range(y + 1, Number): # finally

                if (Numbers_Entered[x] + Numbers_Entered[y] + Numbers_Entered[z] == 0): # here is the condition where x+y+z=zero

                    print("the triples sum equal to zero are: " + str(Numbers_Entered[x]), str(Numbers_Entered[y]), str(Numbers_Entered[z]))
                    Num = True
# in case no triples of sum zero is found
    if (Num == False):
        print("no sum of zeros were found")
Numbers_Entered = [1,3,6,2,-1,2,8,-2,9,-1,-9]
Number = len(Numbers_Entered)
sumOfZero(Numbers_Entered, Number)