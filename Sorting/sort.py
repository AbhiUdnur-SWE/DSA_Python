from xml.dom import minidom


def bubble_sort(arr: list):
    """bubble_sort"""
    for i in range(len(arr)):
        swapped = False

        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def selection_sort(arr: list):
    """selection_sort"""
    for i in range(len(arr) - 1):
        # initial min
        min_inx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_inx]:
                #  update min
                min_inx = j

        # swap min
        arr[min_inx], arr[i] = arr[i], arr[min_inx]


def insertion_sort(arr: list):
    """insertion_sort"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr: list, left, mid, right):
    """merge"""
    n1 = mid - left + 1
    n2 = right - mid

    # temp arrays
    l = [0] * n1
    r = [0] * n2

    # copy data to temps
    for i in range(n1):
        l[i] = arr[left + i]

    for j in range(n2):
        r[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    # Merge the temp arrays back
    while i < n1 and j < n2:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    # Copy the remaining elements,
    # if there are any
    while i < n1:
        arr[k] = l[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1


def merge_sort(arr: list, left, right):
    """merge_sort"""
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
