i = 0
y = 0
#l = 0

list1 = [0,3,2,5,8,4,9,1,6,7]
print("list = " + str(list1))

#list1length = len(list1) - 1
#for l in range (0, list1length):
for y in range (0, len(list1) - 1 * len(list1) - 1): # Looping too few times
    x = i + 1
#    print("i = " + str(i))
#    print("x = " + str(x))
#    print("list = " + str(list1))
    print("----------")
    print("i = {0}: value = {1}".format(i,list1[i] ))
    print("x = {0}: value = {1}".format(x,list1[x] ))
    print(list1)

    
    if list1[i] > list1[i + 1]: 
        tempi = list1[i] ###
        tempx = list1[x] ###

        # https://docs.python.org/3/tutorial/datastructures.html
        
        #list1.remove(x)
        list1.remove(tempx) # Required value to remove, not index
        #list1.remove(i)
        list1.remove(tempi) # Required value to remove, not index
        
        #list1.insert(tempi, x)
        list1.insert(x, tempi) # Index, value (not value, index)
        #list1.insert(tempx, i)
        list1.insert(i, tempx) # Index, value (not value, index)

    if i == 8:
        i = 0
    else:
        i += 1
	
print("list = " + str(list1))

