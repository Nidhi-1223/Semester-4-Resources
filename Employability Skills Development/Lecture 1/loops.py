# #for loop
# for x in range(0,10):
#     print("hello world", x)

# for x in range (0,10, 2):
#     print(x)

#prime or composite?
a = int(input("enter a number: \n"))
counter = 1
if a>1:
    for x in range(2,a):
        if(a % x == 0):
            counter = 0
            # print("composite",x)

if(counter == 0):
    print("composite")
elif (a == 1):
    print("neither prime nor composite")
else:
    print("prime")