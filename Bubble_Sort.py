a = [1,5, 9, 10,2, 8, 12]

# how much time we need to run the loop
for i in range(0,(len(a)-1)): 
    # this loop to access the numbers from the list
    for j in range (0,(len(a)-1)):
        #befolw if is not necessory for undestanding purpose i wrote this one
        if a[j]<a[j+1]:
            continue
        # This is the important step to sort the array
        elif a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            
            #another way of replacing method is,
            """
            temp =a[j]
            a[j+1]=a[j]
            a[j]=temp
            """
            
print(a)


'''
# while loop method:

while True:
    val=True
    for j in range (0,(len(a)-1)):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            val=False
    if val==True:
        break
        
print(a)

'''