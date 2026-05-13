def heapify(arr: list, n, i):
    """heapify"""
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr, n, smallest)


def heapsort(arr: list):
    """heapsort"""
    n = len(arr)

    for i in range((n // 2) - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,i,0)
