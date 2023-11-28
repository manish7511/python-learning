def largest(arr,n):
    a=arr[0]
    for i in range(1,n):
        if arr[i]<a:
            a=arr[i]
    return a
arr=[19,11,29,12,13,45,54,23,25]
n=len(arr)
ans=largest(arr,n)
print(ans)