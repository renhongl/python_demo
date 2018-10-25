

# sort function

def quick_sort(arr): 
    arr = arr[0:]
    if (len(arr) <= 1):
        return arr

    middle = arr.pop(0)
    left = []
    right = []
    for i in range(len(arr)):
        if (arr[i] < middle):
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [middle] + quick_sort(right)

quick_sort([65, 21, 6, 43, 98, 32])
