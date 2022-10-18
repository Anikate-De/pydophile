import random
secretnum=random.randint(1,15)
#print("Secretnumber = ",secretnum)
guessnumber=int(input("Guess a number between 1-15 : "))
while guessnumber!=secretnum :
    if guessnumber<secretnum:
       print("Your guess is too low")
    else:
       print("Your guess is too high")
    guessnumber=int(input("Guess a number between 1-15 :"))
print("Congratulations! Guessed the correct number")