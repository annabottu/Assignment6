import random

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot_value = arr[high]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

def randomized_select(arr, k, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low == high:
        return arr[low]
    
    pivot_index = randomized_partition(arr, low, high)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return randomized_select(arr, k, low, pivot_index - 1)
    else:
        return randomized_select(arr, k, pivot_index + 1, high)
