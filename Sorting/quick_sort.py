def pivot(lst: list, pivot_index, end_index):
    """pivot"""
    swap_indx = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if lst[pivot_index] > lst[i]:
            swap_indx += 1
            lst[swap_indx], lst[i] = lst[i], lst[swap_indx]

    lst[pivot_index], lst[swap_indx] = lst[swap_indx], lst[pivot_index]
    return swap_indx


def quicksort(lst: list, left, right):
    """quicksort"""
    if left < right:
        pivot_indx = pivot(lst, left, right)
        quicksort(lst, left, pivot_indx - 1)
        quicksort(lst, pivot_indx + 1, right)
