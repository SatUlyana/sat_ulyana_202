def find_index(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == 1 and arr[mid - 1] == 0:
            return mid

        if arr[mid] == 1:
            right = mid - 1
        else:
            left = mid + 1

    return -1


arr = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
result = find_index(arr)
if result != -1:
    print(f"{result}")
else:
    print("Разделение не найдено.")
