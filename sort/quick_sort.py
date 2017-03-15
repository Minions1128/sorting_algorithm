def q_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = arr[0]
        return q_sort([a for a in arr[1:] if a < mid]) + [mid] + q_sort([a for a in arr[1:] if a >= mid])


def quick_sort(array, left, right):
    if left >= right:
        return array
    lp, rp = left, right
    mid = array[right]
    while lp < rp:
        while array[lp] <= mid and lp < rp:
            lp += 1
        while array[rp] >= mid and lp < rp:
            rp -= 1
        array[lp], array[rp] = array[rp], array[lp]
    array[lp], array[right] = array[right], array[lp]
    quick_sort(array, left, lp-1)
    quick_sort(array, lp+1, right)
    return array