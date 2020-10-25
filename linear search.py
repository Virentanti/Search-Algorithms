def linear_search(arr,n,x):
    for i in range(0,n):
        if arr[i]==x:
            return i
    return -1


#Driver Code
arr=[2,8,5,9,4,7]
x=9
n=len(arr)

#Functional Call
result= linear_search(arr,n,x)
if result == -1:
    print('Element is not present in the array')
else:
    print(f'Element is present at index {result}')
