#A simple python program to learn the working of bubble sorting algorithm

a=[]                                                         #create an empty list to store the elements
n=int(input("Enter the number of elements in the list: "))   #input the length of the list to sort
for i in range(n):                                           #input the list of elements to sort
    a.append(int(input("Enter element: ")))
for i in range(len(a)):                                      #the sorting algorithm
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print("The sorted list is: ",a)                              #printing the sorted list