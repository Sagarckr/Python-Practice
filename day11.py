# OOP (class, object, attributes, method)
# output function or string function

# class Test():
#     a = 10
#     b = 11

# obj = Test()
# print(obj)
# obj.a = 50
# print(obj.a,obj.b)

# obj2 = Test()
# print(obj2)
# print(obj2.a,obj2.b)

# print(type(obj))
# print(obj == obj2)

# print("========================")

# class Math():
#     a = 10
#     b = 50

#     def add(self):
#         self.c = 20
#         return self.a + self.b + self.c
    
# obj = Math()
# print(obj.add())
# print(obj.c)

# print("=========================")
# class test():
#     message = "this is test message"

#     def __str__(self):
#         return self.message

# obj = test()  
# print(obj)
# print("\n")
# print("============================")

# class Test():

#     def __init__(self,a,b):
#         self.a1 = a
#         self.b1 = b
#         print("I am from class test")
#         return
    
#     def add(self,c):
#         return self.a1 + self.b1 + c
    
# obj = Test(10,20)
# print(obj.add(15))


# Question : Bank Account

# Create a class called BankAccount.

# Requirements:

# The init method should accept:
# account_holder
# balance
# Create methods:
# deposit(amount)
# withdraw(amount)
# show_balance()
# Prevent withdrawal if the amount is greater than the available balance.

class BankAccount():
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        print(self.account_holder)
        print(self.balance)

    def deposit(self,dep_amt):
        if(dep_amt < 0):
            return "Invalid Amount"
        self.balance = dep_amt + self.balance
        return self.balance

    def withdraw(self,with_amt):
        if(self.balance < with_amt or with_amt < 0):
            return "Invalid Amount"
        self.balance = self.balance - with_amt
        return self.balance

    def show_balance(self):
        return self.balance

obj1 = BankAccount(account_holder="sagar", balance=1000)
print("Deposited: ",obj1.deposit(1000))
print("Withdraw: ",obj1.withdraw(500))
print("Current Balance: ",obj1.show_balance())