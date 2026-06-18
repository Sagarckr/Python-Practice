# function : builtin function, user_defined function, arguments, return type
# positional arguments, keyword arguments, arbitary positional / variable length arguments
# arbitary keywords arguments/keyword variable length arguments
# lamda function
# list comrehensive

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


# def user_info(fname, lname):
#     return f"my name is: {fname} {lname}"


# # positional args
# result = user_info("sharma", "sagar")
# print(result)

# # keyword args
# result = user_info(lname="sharma", fname="sagar")
# print(result)

# # def test():
# #     # TODO: make this program runnable
# #     # FIXME: fix error here
# #     pass
# # def test():...

# print("------------------------")


# def add():
#     return (1, 2)


# print(add())


# def test():
#     return 1, 2


# a, b = test()
# print(a, b)

# print("------------------------")


# def add_num(data):
#     sum = 0
#     for i in data:
#         sum = sum + i
#     return sum


# result = add_num([1, 2, 3, 4, 5])
# print(result)

# print("------------------------")
# def area(r,pie=3.14):
#     return pie*r*r

# print(area(5))
# print(area(5,4))



# def add(*data):
#     print(type(data))
#     print(data)
#     return data

# add(1,2,"hello")

# print("=================")

# def add_number(*data):
#     print(data)
#     sum = 0
#     for i in data:
#         if(i<0):
#             continue
#         sum = sum + i
#     return sum

# sum = add_number(-1,2,3,4,5,6)
# print(sum)

# print("===================")

# def check(*data):
#     result = [1, 5]

#     for i in data:
#         if i in result:
#             return True

#         result.append(i)

#     print(result)
#     return False

# print(check(2, 3, 4))

# print("==================")


# def filter_string(**kwargs):
#     result = {}
#     for i in kwargs:
#         if isinstance(kwargs[i], str):
#             result[i] = kwargs[i]
#     return result

# result = filter_string(name=1, address="nepal", age=20, role="developer")
# print(result)

# def all_args(data,*args,new_data=100,**kwargs):
#     print(data)
#     print(args)
#     print(new_data)
#     print(kwargs)

# all_args(1,2,3,4,5,name="test")

# print("=======================")

# def student_marks_sheet(*args,**kwargs):
#     total = sum(args)
#     percentage = total/len(args)
#     name = kwargs['name']
#     return name,percentage

# name,percentage = student_marks_sheet(100,50,70,90,name="hari")
# print(name,percentage)
# name,percentage = student_marks_sheet(100,50,70,90,31,name="shayam")
# print(name,percentage)

def enroll(*course, **name):
    total_course = len(course)

    student_name = name.get("name")
    level = name.get("level", "beginner")

    if total_course == 0:
        return f"{student_name} ({level}) has {total_course} subjects enrolled."
    else:
        return f"{student_name} ({level}) has {total_course} subjects enrolled: {course}"


print(enroll("python", "Django", "SQL",
             name="Sagar", level="advanced"))

print(enroll("python", "SQL",
             name="Hari"))

print(enroll(name="Dhiraj"))

print("=========================")

sum = lambda x,y: x+y
print(sum(12,13))

print("=========================")

a = [1,2,3,4,5]
output = []
for i in a:
    output.append(i*i)

print(output)

print("=========================")

data = [i*i for i in a]
print(data)

print("=========================")

sum = lambda *a: [i*i for i in a]
print(sum(1,2,3))





