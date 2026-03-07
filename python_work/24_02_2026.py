#1...print("The sum of 1 to 5 is:",1+2+3+4+5)

#2.1... n=1,s=0

#2.2... n%2=0

#3... n=int(input())
# print("*"*n)
# print("# "*n)

#4... name="David Joe"
# address="1600 Wilshire Blvd #205,Los Angeles CA 90017"
# print(name)
# print(address)

#5... x=1
# y=0
# print(x and y)
# print(x or y)
# print(not x)
# print(not y)

#6... a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# if a>b:
#     print(a,b)
# else:
#     print(b,a)
            
#7... a = int(input("Are You an adult? 1 for yes and 0 for no: "))
# b = int(input("Are You an married? 1 for yes and 0 for no: "))
# if (a==1 and b==1):
#     print("You are an adult who is married")
# elif (a==1 and b==0):
#     print("You are an adult who is not married")
# else:
#     print("You are a child who is not at the age of getting married, dont you think about getting married")

#8... for num in range(2, 13):
#     is_prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(f"{num} : Prime number")
#     else:
#         print(f"{num} : Composite number")   

#9...
# for num in range(100, 1000):
#     a = num // 100          
#     b = (num // 10) % 10    
#     c = num % 10            


#     if num == a**3 + b**3 + c**3:
#         print(num) 

#10..
# l1 = ['I like', 'I love']
# l2 = ['pancake.', 'kiwi juice.', 'espresso.']

# for i in l1:
#     for j in l2:
#         print(i, j)


#11...
# person = {'Name': 'David Doe', 'Age': 26, 'Weight': 82, 'Job': 'Data scientist'}

# person['Father'] = 'John Doe'

# # print dictionary
# print(person)

#12...
# lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]
# for i in range(len(lst)):
#     for j in range(len(lst) - 1):
#         if lst[j] > lst[j + 1]:
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]

# print(lst)

#13...
# a = [[1, 2], [3, 4], [5, 6]]
# result = []

# for row in a:
#     for value in row:
#         result.append(value)

# print(result)


#14...
# maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

# avg = sum(maria.values()) / len(maria)

# print(avg)


#15..
# from copy import deepcopy

# school = {
#     'kim': {'age': 16, 'hei': 170, 'grade': 3},
#     'lee': {'age': 15, 'hei': 168, 'grade': 2},
#     'choi': {'age': 14, 'hei': 173, 'grade': 1}
# }

# school2 = deepcopy(school)

# print(school is school2)


#16...
# scores = (('Hyun', 88, 95, 90),
#           ('Kang', 85, 90, 95),
#           ('Park', 70, 90, 80),
#           ('Hong', 90, 90, 95))

# names, eng, math, sci = zip(*scores)

# avg_math = sum(math) / len(math)

# print(avg_math)