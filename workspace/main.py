from LinkedList.LinkedListImpl import LinkedList

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
    newLL = LinkedList()
    newLL.append(2345)
    print(newLL.head.val)