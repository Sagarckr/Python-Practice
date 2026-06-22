# Encapsulation (data access modifier) : public,private,protected

# class Test:
#     __password = "sagar"

#     def login(self):
#         return self.__password

# obj = Test()
# print(obj.login())

# print("================================")

# class Test:
#     __password = "sagar"

#     def login(self):
#         password = self.__password
#         return password

# obj = Test()
# print(obj.login())

# print("================================")

# class Test:
#     __password = "sagar"

#     def __login(self):
#         password = self.__password
#         return True

# obj = Test()
# print(obj._Test__login())

# print("================================")


# class Test:
#     __password = "sagar"

#     def __login(self):
#         password = self.__password
#         return True

#     def login(self):
#         return self.__login()

# obj = Test()
# print(obj.login())



print("===============================")

class Wallet:
    owner_name = "Sagar"
    wallet_id = 9821315721

    def __init__(self, balance=100):
        self.__balance = balance
        self.__transaction_logs = []

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be greater than 0."

        self.__balance += amount
        self.__add_transaction_log(f"Deposited Rs.{amount}")

        return f"Rs.{amount} deposited successfully."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be greater than 0."

        if amount > self.__balance:
            return "Insufficient balance."

        self.__balance -= amount
        self.__add_transaction_log(f"Withdrawn Rs.{amount}")

        return f"Rs.{amount} withdrawn successfully."

    def get_balance(self):
        return f"Current Balance: Rs.{self.__balance}"

    def view_transaction_history(self):
        return self.__transaction_logs

    def __add_transaction_log(self, message):
        self.__transaction_logs.append(message)


class PremiumWallet(Wallet):
    cashback_rate = 5  # 5%

    def calculate_cashback(self, amount):
        cashback = amount * self.cashback_rate / 100
        return f"Cashback earned: Rs.{cashback}"


class BusinessWallet(Wallet):

    def __init__(self, balance=100):
        super().__init__(balance)
        self.daily_limit = 50000

    def transfer_to_wallet(self, receiver_wallet, amount):
        result = self.withdraw(amount)

        if result == "Insufficient balance.":
            return result

        receiver_wallet.deposit(amount)

        return f"Transferred Rs.{amount} successfully."

    def set_daily_limit(self, limit):
        self.daily_limit = limit
        return f"Daily limit set to Rs.{limit}"


print("===== Wallet =====")
obj1 = Wallet()

print(obj1.deposit(500))
print(obj1.withdraw(200))
print(obj1.get_balance())
print(obj1.view_transaction_history())


print("\n===== Premium Wallet =====")
premium = PremiumWallet(1000)

print(premium.deposit(500))
print(premium.calculate_cashback(500))
print(premium.get_balance())


print("\n===== Business Wallet =====")
business = BusinessWallet(2000)
receiver = Wallet(500)

print(business.transfer_to_wallet(receiver, 1000))
print(business.set_daily_limit(100000))

print("Business:", business.get_balance())
print("Receiver:", receiver.get_balance())





