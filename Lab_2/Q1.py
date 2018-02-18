"""Consider a shop UMKC with dictionary of all book items with their prices.
Write a program to find the books from the dictionary in the range given by user.
Sample Input: {“python”:50,”web”:3   0,”c”:20,”java”:40}
For range 30 to 40
Sample Output: You can purchase books (web, java) """


    # start Entering the price range Min and Max
print('Enter price range to find the books list ')
    #enter Min
price_Min=input('Min : ')
    #enter max
price_Max=input('Max : ')
    #the books are the keys and the price is the values in this dictionary.
Books_List = { "Introduction to Computing": 120, "Introduction Python": 95, "Introduction C++": 100}
    # the loop for to check the conditions to apply.
for key in Books_List:

    # the condition to make sure the entered values are >= Min and <= Max
    if Books_List[key] >= int(price_Min) and Books_List[key] <= int(price_Max):
        print(str(key) +' Book,  is within the range you entered, its price is $' + str(Books_List[key]))
        # print the books name and it price that are within our range






