# tuple and set

# data = (1, 2, 3, "apple", True)
# print(data)

# print(data[0])
# print(data[3])
# print(data[1:4])
# print(type(data))

# for item in (123, "sagar", "sharma"):
#     print(item)

# my_list = [1, 2, 3]
# print(type(my_list))
# my_tuple = tuple(my_list)

# my_tuple = (1, 2, 3)
# my_list = list(my_tuple)
# print(my_list)

# t1 = (1, 2)
# t2 = (3, 4)
# print(t1 + t2)   # (1, 2, 3, 4)

# t1 = ("sagar",)
# print(t1 * 3)  # ('sagar', 'sagar', 'sagar')

# a ={} # empty dictionary
# a = set() # empty set

# my_set = {1, 1, 1, 2, 3, 4, "banana"}
# print(my_set)

# my_set.add("sagar")
# print(my_set)

# my_set.update([123,"apple"])
# print(my_set)

# my_set.remove(123)
# my_set.discard(123)
# print(my_set)

A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)
print(A & B)
print(A - B)
print(B - A)
print(A ^ B)

data = frozenset([1, 2, 3]) # immutable

s = {"a", "b", "c"}
print("a" in s)   # True
print("d" not in s)   # True

