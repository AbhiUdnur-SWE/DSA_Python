def find_pairs(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target:
                print(f"{i} {j}")


lst = [1,2,3,4]

lst.pop()