# OOP (class and object)\

class Test():
    a = 10
    b = 11

obj = Test()
print(obj)
obj.a = 50
print(obj.a,obj.b)

obj2 = Test()
print(obj2)
print(obj2.a,obj2.b)

print(type(obj))
print(obj == obj2)