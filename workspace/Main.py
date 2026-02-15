from typing import List

def rotate(arr) -> None: 
    n = len(arr)
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        arr[i].reverse()

if __name__ == "__main__":
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    print(rotate(arr))
    print(arr)