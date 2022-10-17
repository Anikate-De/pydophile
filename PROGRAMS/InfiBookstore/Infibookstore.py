#INFORMATICS PRACTICES

import mysql.connector as sql
conn = sql.connect(host ='localhost',user ='root',password ='123654789',database ='infi')
if conn.is_connected():
    print("successfully connected")
c1=conn.cursor()
print("                             ****************INFI BOOKSTORE WELCOMES YOU****************        ")
print("                                               BOOK STORE RENTAL/PURCHASE MANAGEMENT            ")
print("1.Customer Details")
print("2.Book pricesheet --as per time(for rental only)")
print("3.Bill")
print("4.View Customer Details")
print("5.Quit")
a=int(input("Enter your choice :"))
if a==1:
    name=input("Enter your name :")
    age=int(input("Enter your age :"))
    address=input("Enter your residential address :")
    phone_no=int(input("Enter your phone number :"))
    email_id=input("Enter your Email ID :")
    ty="insert into Add_new_customer values('{}',{},'{}',{},'{}')".format(name,age,address,phone_no,email_id)
    c1.execute(ty)
    conn.commit()    
    print("                                                THANK YOU! VISIT AGAIN :)               ")
if a==2:
    time=input("Enter the time :") 
    book_name=str(input("Enter the book name :"))
    amount=int("Price of ")
    ss="insert into book_pricesheet values('{}',{})".format(book,amount)
    c1.execute(ss)
    conn.commit()
    print("                                                THANK YOU! VISIT AGAIN :)               ")
if a==3:
    name=input("Enter your name :")
    time=int(input("Enter the time you borrowed book (in days) :"))
    total=time*30
    qw="insert into Bill values('{}',{},{})".format(name,time,total)
    c1.execute(qw)
    conn.commit()
    print("Please pay Rs.",total)
    print("Type YES to pay your bill or NO to pay it later")
    b=input("Type YES or NO:")
    if b=="YES":
        print("Bill paid successfully")
        print("                                            THANK YOU! VISIT AGAIN :)             ")
    else:
        print("*Bill not paid* --make the required payment--")
if a==4:
    phone_no=input("Enter the phone number of the customer you want to search :")
    ea="select * from Add_new_customer where Phone_no=" + str(phone_no)
    c1.execute(ea)
    data=c1.fetchall()
    for row in data:
        print("Name:",row[0])
        print("Age:",row[1])
        print("Address:",row[2])
        print("Phone number:",row[3])
        print("Email ID",row[4])
    print("                   THANK YOU! VISIT AGAIN :)              ")
if a==5:
    print("                   THANK YOU! VISIT AGAIN :)              ")
    