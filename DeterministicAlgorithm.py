def partition(arr, low, high, pivot_index):
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index] 
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index] 
    return store_index

def select_deterministic(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    
    medians = [sorted(arr[i:i+5])[len(arr[i:i+5])//2] for i in range(0, len(arr), 5)]
    
    median_of_medians = select_deterministic(medians, len(medians)//2)
    
    pivot_index = arr.index(median_of_medians)
    pivot_index = partition(arr, 0, len(arr)-1, pivot_index)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return select_deterministic(arr[:pivot_index], k)
    else:
        return select_deterministic(arr[pivot_index+1:], k - pivot_index - 1)
