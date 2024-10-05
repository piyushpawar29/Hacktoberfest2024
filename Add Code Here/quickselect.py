import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]
    
    pivot_index = partition(arr, low, high)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

def find_kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        return "Invalid value of k"
    return quickselect(arr, 0, len(arr) - 1, k - 1)

# Example usage
arr = [12, 3, 5, 7, 4, 19, 26]
k = 3
print(f"The {k}-th smallest element is {find_kth_smallest(arr, k)}")
