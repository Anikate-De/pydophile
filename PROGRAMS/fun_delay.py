# Write a Python program that invoke a given function after specific milliseconds.

# Import the time module
import time


# Create a function to execute a function after a delay
def fun_delay(func, delay, *args, **kwargs):

    # Sleep for the specified delay
    time.sleep(delay)

    # Execute the function
    func(*args, **kwargs)

# Get the value of delay from the user
delay = float(input("Enter the delay in seconds: "))

# Use the function to print the current time after the specified delay
fun_delay(print, delay, "The current time is", time.ctime())
