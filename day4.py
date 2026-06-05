# list, array module, indexing, slicing, methods for adding items in list

a = [1,2,3,4,5]
data = [1,2,3,"hello","test",5.5,True,False]
print(data)
print(data[1:6])
print(data[1:])
print(data[:6])
print(data[:])
print(data[1:1]) #empty
print(data[-5:-2])

# Append
data.append(7)
data.append("sagar")
print(data)

# Insert
data.insert(4,"10.0")
data.insert(100,500)
print(data)

# Extend
data.extend(['John', 'sharma'])
print(data)
print("\n")

a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

# concate
ab = a+b
print(ab)

# delete from index
del ab[4]
print(ab)

# remove value
ab.remove(6)
print(ab)

# pop from index or from end
last_data = ab.pop(4)
print(ab)
print(last_data)

# clear
print()
ab.clear()
print(ab)

# print(type(a))
# print(a)
# print(len(a))
# print(a[0])
# print(a[-1])
# print(a[-5])

# a=[]
# print(type(a))

# from array import array
# numbers = array('i', [10, 20, 30, 40])
# numbers2 = array('f', [1.5, 2.5, 3.5])
# character = array('u', ['a', 'b', 'c'])

# print(type(numbers))
# print(numbers)
# print(list(numbers))


# import numpy as np
# arr = np.array([10, 20, 30, 40])

