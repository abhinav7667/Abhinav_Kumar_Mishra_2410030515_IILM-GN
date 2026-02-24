#calculate the median of all the elements of given array
def median(arr):
    arr=sorted(arr)
    n=len(arr)
    mid=n//2
    if n%2==1:
        return arr[mid]
    else:
        return (arr[mid-1]+arr[mid])/2
arr=[2,3,5,7,6,4]
print (median(arr))    
    
