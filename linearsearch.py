def linearsearch(arr,x):
    for i in range(len(arr)):
        if(arr[i] == x): 
            print("Element Found :", i)
            return
    print("Element Not Found")

arr = [10,20,30,40,50]
target = int(input("Enter an Integer : "))
linearsearch(arr,target)