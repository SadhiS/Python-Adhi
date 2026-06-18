def interpolationsearch(arr,target,low,high):
    pos = low + (target - arr[low])//(arr[high] - arr[low]) * (high - low)
    return pos

arr = [1,3,5,7,9,11]
target = int(input("Enter an Integer : "))
res = interpolationsearch(arr, target, 0, 5)
if res == -1:
    print("Element Not Found")
else:
    print("Element Found :", res)