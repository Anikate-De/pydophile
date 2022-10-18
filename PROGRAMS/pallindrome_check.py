string=input("Enter a string")
length=len(string)
mid=int(length/2)
rev=-1
for a in range(0,mid):
    if string[a]==string[rev]:
      a+=1
      rev-=1
    else:
       print(string, "is Not a Palindrome ")
       break
else:
    print(string, " is a Palindrome")