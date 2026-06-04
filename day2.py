# type casting / type conversion, type checking, operators, string concate using + and *

data = "123"
print(f"Type of data: {type(data)}")
data = int(data)
print(f"Type of data: {type(data)}")
print("\n")

data = 123
print(data, "is", type(data))
data = str(data)
print(data, "is",type(data))
print("\n")

data = "hello"
print(type(data))
# this will give error because "hello" cannot be converted to an integer 
# data = int(data) 
print(type(data))
print("\n")

print(isinstance(data, str)) # to check if data is of type string
print(isinstance(data, int)) # to check if data is of type integer

# not recommended
type(data) == str # to check if data is of type string
type(data) == int # to check if data is of type integer
print(type(data) == str)
print(type(data) == int)



# arithmetic operator
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000

# comparision operator
a = 10
b = 3

print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False

# logical operator
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
print(5>2 and 3<4)  # True
print(5>2 or 3>4)   # True
print(not (5>2))    # False

# assignment operator
x = 5
x += 3   # 8
x -= 2   # 6
x *= 2   # 12
x /= 3   # 4.0

# bitwise operator
a = 5   # 101
b = 3   # 011

print(a & b)  # 1
print(a | b)  # 7
print(a ^ b)  # 6
print(~a)     # -6
print(a << 1) # 10
print(a >> 1) # 2

first = "sagar"
second = "sharma"
print(first+"",second)

print(a*first)
print(first*a)
