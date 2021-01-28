from math import sqrt, floor


def binarySearch(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

        # If we reach here, then the element
        # was not present
    return -1




## Complexity O(root n)
def jump_search(arr, x):
    block_size = floor(sqrt(len(arr)))
    counter = 0
    while arr[counter] <= x:
        counter += block_size
    for i in range(counter - block_size, len(arr)):
        if arr[i] == x:
            return i

arr = [2, 3, 4, 10, 40, 50, 60, 90]
x = 40

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)
print(result)

print(jump_search(arr, x))

