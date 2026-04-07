def reverse_matrix(arr):

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            arr[i][j], arr[j][i] =  arr[j][i], arr[i][j]
        
    return [sorted(i, reverse=True ) for i in arr]

arr = [[1,2,3],[4,5,6],[7,8,9]]
print(reverse_matrix(arr))


def reverse_arr(arr):
    for i in range(len(arr)//2):
        arr[len(arr)-1-i],arr[i] = arr[i] , arr[len(arr)-1-i]
    
    return arr 

arr = [1,2,3,4,5,6,7,8,9]
print(reverse_arr(arr))