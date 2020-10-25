def binarysearch(arr,l,r,x):
    if r >= 1:
        mid = l+(r-1)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            return binarysearch(arr,l,mid-1,x)
        else:
            return binarysearch(arr,mid+1,r,x)
    else:
        return -1


#Driver Code
arr=[2,3,4,10,60]
x=10


#function call
result = binarysearch(arr,0,len(arr)-1,x)

if result != -1:
    print(f'Element is present at index {index}')
else:
    print('Element is not present in array')
