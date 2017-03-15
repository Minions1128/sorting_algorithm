def merge(l_arr, r_arr):
    l, r = 0, 0
    result = []
    while l < len(l_arr) and r < len(r_arr):
        if l_arr[l] <= r_arr[r]:
            result.append(l_arr[l])
            l += 1
        else:
            result.append(r_arr[r])
            r += 1
    return result + l_arr[l:] + r_arr[r:]

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = int(len(array)/2)
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)
