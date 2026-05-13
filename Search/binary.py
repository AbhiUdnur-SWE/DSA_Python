def binary_search_recur(arr: list, l, r, val):
    """binary_search"""
    if r >= l:
        mid = (l + r) // 2
        if arr[mid] == val:
            return mid

        if arr[mid] < val:
            return (binary_search_recur(arr, l, mid - 1, val),)

        return binary_search_recur(arr, mid + 1, r, val)

    return -1


def binary_search_iter(arr: list, val: int):
    """binary_search_iter"""
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == val:
            return mid

        if arr[mid] < val:
            r = mid - 1
        else:
            l = mid + 1

    return -1
