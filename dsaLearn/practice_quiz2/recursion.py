def binSearch(arr, left, right, target):

    if left > right:

        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:

        return mid

    elif arr[mid] < target:

        return binSearch(arr, mid + 1, right, target)

    else:

        return binSearch(arr, left, mid - 1, target)



arr = [2, 4, 6, 8, 10]

n = len(arr)

target = 6

print("Given array:", arr)

print("Target Element to search:", target)

result = binSearch(arr, 0, n - 1, target)

print("Element", target, "found at index:", result)