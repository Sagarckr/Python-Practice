# inheritance : single, multilevel, multiple

# single interitance
# class Parent():
#     a = 20
#     b = 11

#     def display(self):
#         return "this is from parent class"

#     def add(self):
#         return self.a + self.b

# class Child(Parent):
#     a = 2
#     c = 60
#     d = 200

# obj = Child()
# print(obj.a)
# print(obj.d)
# print(obj.b)
# print(obj.display())
# print(obj.add())


# # constructor
# class Parent():
#     def __init__(self):
#         print("Parent Constructor")

# class Child(Parent):
#     a = 10
#     # def __init__(self):
#     #     print("Child constructor")

# obj = Child()


# class Parent:
#     def __init__(self):
#         print("Parent Constructor")

# class Child(Parent):
#     a = 10

#     def __init__(self):
#         print("Child Constructor")
#         super().__init__()

# obj = Child()

# print("============================")

# # multilevel
# class Parent:
#     def __init__(self):
#         print("Parent Constructor")

# class Child(Parent):
#     a = 10

#     def __init__(self):
#         print("Child Constructor")
#         super().__init__()

# class GrandChild(Child):
#     d = 2

# obj = Child()

# print("============================")


class Course:
    course_name = "Python"
    ins_name = "Sudan"
    duration = "1 hour"

    def show_course_details(self):
        return f"""Course: {self.course_name}
Instructor: {self.ins_name}
Duration: {self.duration}"""


class OnlineCourse(Course):
    platform_name = "Google Meet"
    course_link = "jkslfjd.kljdlfds"

    def show_platform_details(self):
        return f"Platform_name: {self.platform_name}, \nCourse_Link: {self.course_link}"


class PaidOnlineCourse(OnlineCourse):
    price = 124
    payment_status = "Completed"

    def show_payment_detail(self):
        return f"Price: {self.price}, \nPayment Status: {self.payment_status}"


# Creating object
print("===================================")

paid_obj = PaidOnlineCourse()
print(paid_obj.show_course_details())
print(paid_obj.show_platform_details())
print(paid_obj.show_payment_detail())
