# Sort the List According to the Second Element in Sublist

def sort_list(list1):
    # a lambda function could also be used - `lambda x:x[1]`
    list1.sort(key=ret_2nd_element)
    return list1

# Create a function that returns the second element of the sublist


def ret_2nd_element(sublist):
    return sublist[1]


# Take list input using eval() function
list1 = eval(input('Enter the list in correct format [1,2,3,...]- '))

# Print Sorted List
print(sort_list(list1))
