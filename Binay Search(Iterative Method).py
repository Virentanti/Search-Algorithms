def binarysearch(arr,l,r,x):
    while l<=r:
        mid = l + (r-1)//2
        if arr[mid] == r:
            return mid
        elif arr[mid]< x:
            l = mid + 1
        else:
            r = mid-1
    return -1


#Driver Code
arr=[2,3,4,10,40]
x=10


#Function Call
if result != -1:
    print(f'Element is in present at index {result}')
else:
    print('Element is not present in array')
