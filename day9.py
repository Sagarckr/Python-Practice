# function : builtin function, user_defined function, arguments, return type
# positional arguments, keyword arguments

# count = 0
# def test():
#     global count
#     count += 1
#     print("This is test function ",count)

# test()
# test()
# test()

# print("----------------")
# def add(a,b,c):
#     sum = a+b+c
#     return(sum)

# a,b,c = 3,5,2
# sum1 = print(f"The sum of {a,b,c} is :", add(a,b,c))
# sum2 = print("The sum is:", add(4,6,5))


def user_info(fname, lname):
    return f"my name is: {fname} {lname}"


# positional args
result = user_info("sharma", "sagar")
print(result)

# keyword args
result = user_info(lname="sharma", fname="sagar")
print(result)

# def test():
#     # TODO: make this program runnable
#     # FIXME: fix error here
#     pass
# def test():...

print("------------------------")


def add():
    return (1, 2)


print(add())


def test():
    return 1, 2


a, b = test()
print(a, b)

print("------------------------")


def add_num(data):
    sum = 0
    for i in data:
        sum = sum + i
    return sum


result = add_num([1, 2, 3, 4, 5])
print(result)

print("------------------------")
def area(r,pie=3.14):
    return pie*r*r

print(area(5))
print(area(5,4))