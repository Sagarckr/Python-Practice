# # multiple inheritance

class Parent:
    def display(self, name):
        return f"Hello {name} from Parent Class"

class Parent1:
    def display(self, name):
        return f"Hello {name} from Parent1 Class"

class Child(Parent1, Parent):
    a = 20

obj = Child()
print(obj.display("Sagar"))





# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_person(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")


# class Teacher:
#     def __init__(self, subject, salary):
#         self.subject = subject
#         self.salary = salary

#     def teach(self):
#         print(f"Teaching subject: {self.subject}")

#     def show_salary(self):
#         print(f"Salary: ${self.salary}")


# class Researcher:
#     def __init__(self, field):
#         self.field = field

#     def research(self):
#         print(f"Researching in: {self.field}")


# # Multiple Inheritance
# class Professor(Person, Teacher, Researcher):
#     def __init__(self, name, age, subject, salary, field):
#         Person.__init__(self, name, age)
#         Teacher.__init__(self, subject, salary)
#         Researcher.__init__(self, field)

#     def show_all_details(self):
#         print("\n===== Professor Profile =====")
#         self.show_person()
#         self.teach()
#         self.research()
#         self.show_salary()


# prof = Professor(
#     name="Dr. Sharma",
#     age=45,
#     subject="Artificial Intelligence",
#     salary=120000,
#     field="Machine Learning"
# )

# prof.show_all_details()