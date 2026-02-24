#...Given a number x and an array of integers arr.
#...Find the smallest subarray with sumgreater than the given value.
#...If such a subarray does not exist, return 0.
 
# def smallest_subarray(arr,x):
#     n=len(arr)
#     current_sum=0
#     left=0
#     min_length=n+1
#     for right in range(n):
#         current_sum+=arr[right]
#         while current_sum > x:
#             min_length=min(min_length,right-left+1)
#             current_sum=current_sum-arr[left]
#             left=left+1
#     if min_length==n+1:
#                 return 0
#     else:
#                 return min_length
# print(smallest_subarray([1,10,5],11))




def smallest_subarray(arr,x):
    n=len(arr)
    current_sum=0
    left=0
    min_length=n+1
    for right in range(n):
        current_sum+=arr[right]
        while current_sum > x:
            min_length=min(min_length,right-left+1)
            current_sum=current_sum-arr[left]
            left=left+1
    if min_length<=n:
       return min_length
    else:
        return 0
print(smallest_subarray([1,10,5],11))





# Given an array of positive integer where each value 
# represents the number of chocolates in the packet each packet
# can have variable no of chocolate,there are m students 
# are there, among m students such that 
# 1 each student get exactly one packet
# 2. the difference b/w max no of chocolate given to student 
# and min no of chocolate given to students is min and return 
# that minimum possible diffrence
# array[3,4,1,9,56,7,9,12]  m=5

def chocolate_distribution(arr, m):
    arr.sort()
    min_diff = arr[-1]
    for i in range(len(arr) - m + 1):
        current_diff = arr[i + m - 1] - arr[i]

        if current_diff < min_diff:
            min_diff = current_diff

    return min_diff
arr = [3,4,1,9,56,7,9,12]
m = 5
print(chocolate_distribution(arr, m))
           

