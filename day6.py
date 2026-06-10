# # dictionary
# data = {
#     'Name': 'Sagar',
#     'Age': 20,
#     'Status': 'Unmarried',
#     'is_active': True,
#     'Name': 'Shubham'
# }

# print(type(data))
# print(data)
# print(data["Name"], data['Age'])
# data['Age']=25
# print(data['Age'])
# print(data)
# print(len(data))

# print(data.keys())
# print(data.values())
# print(data.items())

# # print(data['Ages'])
# print(data.get('ages',False))

# data['Gender']="Male"
# print(data)

# data.update({
#     'Name': 'Sagar',
#     'Marks': 75,
#     'Age': 22
# })

# print(data)
# print("\n")

# for key, value in data.items():
#     print(key, ":", value)

# student = {
#     "Name": "Sagar",
#     "Age": 22,
#     "Gender": "Male",
#     "Status": "Unmarried",
#     "City": "Kathmandu",
#     "Country": "Nepal",
#     "College": "Boston International College",
#     "Course": "BBA",
#     "Semester": 8,
#     "GPA": 3.30,
#     "Email": "sagar@example.com",
#     "Phone": "9800000000",
#     "is_active": True,
#     "Marks": 75,
#     "Hobby": "Coding"
# }

# for key, value in student.items():
#     print(f"{key}: {value}")

# print("\n")

# del student['Phone']
# del student['Hobby']
# for key, value in student.items():
#     print(f"{key}: {value}")

# a = student.pop("is_active")
# print("\n")
# print(a)

# student.popitem()
# print("\n")
# for key, value in student.items():
#     print(f"{key}: {value}")

user_info = {
    "name":"Suman",
    "number":[
        {
            "type":"ntc",
            "number":9821316788
        },
        {
            "type":"ncell",
            "number":9801677788
        }
    ]
}

print(user_info.values())
print("\n")

print(user_info["name"])
print(user_info["number"][0]['type'])
print(user_info["number"][0]['number'])
print(user_info["number"][1]['type'])
print(user_info["number"][1]['number'])

print("\n")
print(user_info["name"], user_info["number"][0]['type'],"number is", user_info["number"][0]['number'])
print(user_info["name"], user_info["number"][1]['type'],"number is", user_info["number"][1]['number'])

