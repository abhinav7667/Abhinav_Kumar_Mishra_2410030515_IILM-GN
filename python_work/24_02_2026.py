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
            
# a = int(input("Are You an adult? 1 for yes and 0 for no: "))
# b = int(input("Are You an married? 1 for yes and 0 for no: "))
# if (a==1 and b==1):
#     print("You are an adult who is married")
# elif (a==1 and b==0):
#     print("You are an adult who is not married")
# else:
#     print("You are a child who is not at the age of getting married, dont you think about getting married")

# for num in range(2, 13):
#     is_prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(f"{num} : Prime number")
#     else:
#         print(f"{num} : Composite number")   


# for num in range(100, 1000):
#     a = num // 100          
#     b = (num // 10) % 10    
#     c = num % 10            


#     if num == a**3 + b**3 + c**3:
#         print(num) 

# l1 = ['I like', 'I love']
# l2 = ['pancake.', 'kiwi juice.', 'espresso.']

# for i in l1:
#     for j in l2:
#         print(i, j)



# person = {'Name': 'David Doe', 'Age': 26, 'Weight': 82, 'Job': 'Data scientist'}

# person['Father'] = 'John Doe'

# # print dictionary
# print(person)


# lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]
# for i in range(len(lst)):
#     for j in range(len(lst) - 1):
#         if lst[j] > lst[j + 1]:
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]

# print(lst)


# a = [[1, 2], [3, 4], [5, 6]]
# result = []

# for row in a:
#     for value in row:
#         result.append(value)

# print(result)


maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

avg = sum(maria.values()) / len(maria)

print(avg)


