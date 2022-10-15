#In merge sort our approach is to divide the array in 2 equal half and recursively sort them and finally merge them again

def MergeSort(a):
    #Base case for recusion
    if len(a) == 0 or len(a) == 1:
        return 
    
    #finding middle to divide the array in equal half
    mid = len(a)//2
    
    #seprating given array into 2 array
    a1 = a[:mid]
    a2 = a[mid:]
    
    #calling mergesort on them as our recursion hypothesis is that it will give us 2 sorted array
    MergeSort(a1)
    MergeSort(a2)
    
    #merging both sorted array into one
    merge(a1, a2, a)


#for merging 2 sroted array we use 2 pointers which iterate on both of them,compare the elements and add them into final array
def merge(a1, a2, a):
    #here i,j are pointers which will iterate over array and help us to compare the elements
    i = 0
    j = 0
    #we take k as a pointer to add element in main array 
    k = 0
    
    #comparing elements from both array and adding it to main array
    while i < len(a1) and j <len(a2):
        if a1[i] < a2[j]:
            a[k] = a1[i]
            k = k + 1
            i = i + 1
        else:
            a[k] = a2[j]
            k = k + 1
            j = j + 1
    
    #adding rest of elements left in array1 
    while i < len(a1):
        a[k] = a1[i]
        k = k + 1
        i = i + 1
   
    #adding rest of elements left in array2 
    while j < len(a2):
        a[k] = a2[j]
        k = k + 1
        j = j + 1


# Main
arr=list(int(i) for i in input().strip().split(' '))
MergeSort(arr)
print(arr)
