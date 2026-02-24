#print("The sum of 1 to 5 is:",1+2+3+4+5)

# n=1,s=0

# n%2=0

# n=int(input())
# print("*"*n)
# print("# "*n)

# name="David Joe"
# address="1600 Wilshire Blvd #205,Los Angeles CA 90017"
# print(name)
# print(address)

# x=1
# y=0
# print(x and y)
# print(x or y)
# print(not x)
# print(not y)

# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# if a>b:
#     print(a,b)
# else:
#     print(b,a)
            
a = int(input("Are You an adult? 1 for yes and 0 for no: "))
b = int(input("Are You an married? 1 for yes and 0 for no: "))
if (a==1 and b==1):
    print("You are an adult who is married")
elif (a==1 and b==0):
    print("You are an adult who is not married")
else:
    print("You are a child who is not at the age of getting married, dont you think about getting married")
