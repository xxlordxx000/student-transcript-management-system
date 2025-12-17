# Sorting Algorithms
# Bubble Sort Algorithm
def bubble_sort(data, key):
    """
    Sorts the list of students using bubble sort.
    """
    arr = data[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][key] > arr[j+1][key]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Quick Sort Algorithm
def quick_sort(data, key):
    """
    Sorts the list of students using quick sort.
    """
    if len(data) <= 1:
        return data
    pivot = data[0]
    less = [x for x in data[1:] if x[key] <= pivot[key]]
    greater = [x for x in data[1:] if x[key] > pivot[key]]
    return quick_sort(less, key) + [pivot] + quick_sort(greater, key)
