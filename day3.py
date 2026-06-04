# # condition

# first_name = "sagar"
# second_name = "sharma"
# if(first_name == "sagar" and second_name == "sharma"):
#     print("Your name is : ", first_name, second_name)
# elif(first_name == "sagar" and second_name != "sharma"):
#     print("Second_name is incorrect !!!")
# elif(first_name != "sagar" and second_name == "sharma"):
#     print("First name is incorrect !!!")
# else:
#     print("Both first name and second name is incorrect !!!",end="\n")
#     print("Please check")

# marks = 65
# if(marks>80 and marks<100):
#     print("Distinction")
#     if(marks==82):
#         print("Great !!!")
#     elif(marks > 90):
#         print("Topper !!!")
# elif(marks>60 and marks<80):
#     if(1==1):
#         print("This is true")
#     print("First Division")
# elif(marks>50 and marks<60):
#     print("Second division")
# elif(marks<0 or marks>100):
#     print("Marks is invalid")
# else:
#     print("You are failed")


# temp = float(input("Enter the temperature: "))
# if(temp>=30):
#     print("It is hot today")
# elif(temp>=20 and temp<30):
#     print("It is warm today")
# elif(temp>=10 and temp<20):
#     print("It is cool today")
# else:
#     print("It is cold today")

# Online Shopping Discount
purchase_amt = int(input("Enter the purchase amount: "))
member = input("Is_Member: (True or False) : ").strip().lower() == "true"
coupon = False

if(purchase_amt<0):
    print("Amount is incorrect !!!", end = "\n")

if(purchase_amt>=100):
    if(member):
        if(coupon):
            print("purchase amount is: ",purchase_amt,end="\n")
            discount = (purchase_amt*20/100)
            final_amt = purchase_amt - discount
            print("You are member", end ="\n")
            print("You have coupan")
            print("You get 20 percent discount", end="\n")
            print("Your final amount is: ",final_amt)
        else:
            print("purchase amount is: ",purchase_amt,end="\n")
            discount = (purchase_amt*10/100)
            final_amt = purchase_amt - discount
            print("You are member", end ="\n")
            print("You don't have coupan")
            print("You get 10 percent discount", end="\n")
            print("Your final amount is: ",final_amt)
    else:
        if(coupon):
            print("purchase amount is: ",purchase_amt,end="\n")
            discount = (purchase_amt*5/100)
            final_amt = purchase_amt - discount
            print("You are not member", end ="\n")
            print("You have coupan")
            print("You get 10 percent discount", end="\n")
            print("Your final amount is: ",final_amt)
else:
    print("purchase amount is: ",purchase_amt,end="\n")
    final_amt = purchase_amt
    print("You are not member", end="\n")
    print("You don't have coupan", end="\n")
    print("No discount", end="\n")
    print("Your final amount is: ", final_amt)