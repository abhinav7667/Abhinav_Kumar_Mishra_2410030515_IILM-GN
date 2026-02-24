#...Given an array and a target value we need to identify 
# the indices of those two elements whose sum is equal 
# to target value

def twosum(nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(i+2,n):
                if nums[i] + nums[j] + nums[k] == target:
                    return[i,j,k]
    return[]
print(f"Result:{twosum([0,1,5,6,8,3,2,4,9,7],9)}")


# all possible sum that give target

# def twosum(nums,target):
    
#     n=len(nums)
#     result = []
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if nums[i] + nums[j] + nums[k] == target:
#                     result.append([i,j,k])
#     return result
# print(f"Result:{twosum([0,1,5,6,8,3,2,4,9,7],9)}")
 


# ARRAY=[1,3,5,8,9,2,6,7,6,8,9]
# Max reach = arr[0]
# Step_left=arr[0]
# Jumps=1
# For i in range(1,n-1)
#    Max reach=max(max_reach,i+arr[i])
# Steps_left-= 1  , step_left = Step_left - 1
# if step_left==0:
#    Jumps+=1

def jump_arr(arr, jump):
    n = len(arr)
    max_reach = arr[0]
    step_left = arr[0]
    jump = 1
    for i in range (1,n-1):
        max_reach = max(max_reach , i + arr[i])
        step_left = step_left -1
        if step_left == 0:
            jump = jump + 1
            return i
        else :
            return -1
        
print(f"i:jump_arr{([1,3,5,8,9,2,6,7,6,8,9])}")
