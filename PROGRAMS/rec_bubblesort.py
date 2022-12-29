# Bubble sorting algorithm using Recursion.

# Create a recursive function to bubble sort a list
def bubble_sort(lst):
    # If the list is empty or has only one element, return the list
    if len(lst) <= 1:
        return lst
    # Otherwise, bubble sort the list
    else:
        # Bubble sort the list
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        # Bubble sort the list without the last element
        return bubble_sort(lst[:-1]) + [lst[-1]]

# Get the list from the user
lst = eval(input('Enter the list - '))

print(bubble_sort(lst))