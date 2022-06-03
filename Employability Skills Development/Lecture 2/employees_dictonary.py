#dictonary of employees

employee1 = {
    "name" : "phil",
    "age" : 24,
    "address" : {
        "city" : "mumbai",
        "state" : "maharashtra",
        "pincode" : 404405
    },
    "salary" : 1200000
}

employee2 = {
    "name" : "alex",
    "age" : 30,
    "address" : {
        "city" : "ahemdabad",
        "state" : "gujrat",
        "pincode" : 409005
    },
    "salary" : 1000000
}

employee3 = {
    "name" : "hayley",
    "age" : 32,
    "address" : {
        "city" : "jaipur",
        "state" : "rajasthan",
        "pincode" : 400105
    },
    "salary" : 800000
}

print("----------------for employee1----------------")
print(employee1)
print(employee1["address"]["pincode"])
print(employee1["salary"])
print("\n\n")

print("----------------for employee2----------------")
print(employee2)
print(employee2["address"]["pincode"])
print(employee2["salary"])
print("\n\n")

print("----------------for employee3----------------")
print(employee3)
print(employee3["address"]["pincode"])
print(employee3["salary"])
print("\n\n")