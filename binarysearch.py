def binarysearch(arr, target, low, high):
    while(low <= high):
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
    
    return -1

arr = [10,20,30,40,50,60,70,80,90,99]
target = int(input("Enter an Integer : "))

res = binarysearch(arr, target, 0, 9)

if res == -1:
    print("Element Not Found")
else:
    print("Element Found :", res)
