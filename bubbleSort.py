import random #To be used to generate the array.

"""Bubble Sort Algorithm"""
def bubbleSort(arrayOne):
    for passing in range(len(arrayOne)-1,0,-1):
        for i in range(passing):
            if arrayOne[i]>arrayOne[i+1]:
                number = arrayOne[i]
                arrayOne[i] = arrayOne[i+1]
                arrayOne[i+1] = number
                
arrayOne = [] #Creating the array.

#Generating the array, currently 5 digits long.
for x in range (0,15):
    arrayOne.append(random.randint(1,100))
"""
arrayOne = [87,5,26,99,24,3,46,77,3,6]
"""
print(arrayOne) #Prints the original array.
bubbleSort(arrayOne) #Calls and executes the function bubbleSort, which is defined above.
print(arrayOne) #Prints the sorted array.
input()
