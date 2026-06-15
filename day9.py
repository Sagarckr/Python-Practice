# function : builtin function, user_defined function, arguments, return type

count = 0
def test():
    global count
    count += 1
    print("This is test function ",count)

test()
test()
test()

print("----------------")
def add(a,b,c):
    sum = a+b+c
    return(sum)

a,b,c = 3,5,2
sum1 = print(f"The sum of {a,b,c} is :", add(a,b,c))
sum2 = print("The sum is:", add(4,6,5))