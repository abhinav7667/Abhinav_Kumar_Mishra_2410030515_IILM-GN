#we need to find the leaders and put them all in another array. who will be the leaders?

def find_leader(arr):
    leader = []
    max_val = 0
    
    for x in reversed(arr):
        if x > max_val:
            leader.append(x)
            max_val = x
    
    return leader

print(find_leader([16, 17, 4, 3, 5, 2]))


#.................................

def find_leaders(arr):
    leaders = []
    max_right = arr[-1]

    leaders.append(max_right)

    for x in reversed(arr[:-1]):
        if x > max_right:
            leaders.append(x)
            max_right = x

    return leaders[::-1]
arr = [16, 17, 4, 3, 5, 2]
result = find_leaders(arr)
print(result)



# write another program in python to calculating the factorial of the number

import math
print(math.factorial(5))
n = 5
fact = math.factorial(n)

for digit in str(fact):
    print(digit, end=" ")


    