#Write a Python Program to Replace all Occurrences of ‘a’ with ‘b’ in a String. If ‘a’ is not present then print appropriate message.
string=str(input("Enter string:"))
import re
if 'a' in string:
    new_string=re.sub("a","b",string)
    print(new_string)
if 'a' not in string:
    print("No occurrence of 'a' in string.")
