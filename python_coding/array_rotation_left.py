arr = [2, 3, 41, 9, 7, 6, 5, 35, 42, 89]
k = 3

n = len(arr)

k = k % n

rotated_arr = arr[k:] + arr[:k]
print(rotated_arr)

def left_rotate(arr, k):

    arr_len = len(arr)
    k = k % arr_len

    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    reverse(arr, 0, k-1)
    reverse(arr, k, arr_len - 1)
    reverse(arr, 0, arr_len - 1)
    return arr


print(left_rotate(arr, 3))
