import array as arr 

arr = arr.array("i", [1,2,3,4])

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

