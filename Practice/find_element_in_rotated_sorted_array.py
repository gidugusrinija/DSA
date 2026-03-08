rot_arr = [5, 7, 8, 1, 2, 3]
t = 9

low = 0
high = len(rot_arr) - 1


while low <= high:

    mid = (low + high)//2

    if rot_arr[mid] == t:
        print(mid)
        break

    # find which part of the array is sorted

    if rot_arr[low] <= rot_arr[mid]:
        if rot_arr[low] <= t < rot_arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        if rot_arr[mid] < t <= rot_arr[high]:
            low = mid + 1
        else:
            high = mid + 1

    if low > high:
        print("-1")








