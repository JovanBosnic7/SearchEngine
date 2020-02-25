def partition(result, low, high):
    i = low-1

    pivot = result[high]

    for j in range(low, high):
        element = result[j]

        if element[1] > pivot[1]:
            i = i + 1
            result[i], result[j] = result[j], result[i]

    result[i+1], result[high] = result[high], result[i+1]

    return i+1


def sort(result, low, high):
    if low < high:
        pi = partition(result,low, high)
        sort(result, low, pi-1)
        sort(result, pi+1, high)