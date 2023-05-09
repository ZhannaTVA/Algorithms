from math import *

def bubble_sort(lst):
    #Time Complexity
    #Best               O(n)
    #Worst              O(n^2)
    #Average            O(n^2)
    #Space Complexity   O(1)
    #Stability	        Yes
    for i in range(len(lst)):
        swap = False
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap = True
        if not swap:
            break
    return lst

def selection_sort(lst):
    # Time Complexity
    # Best               O(n^2)
    # Worst              O(n^2)
    # Average            O(n^2)
    # Space Complexity   O(1)
    # Stability	         No
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

def insertion_sort(lst):
    # Time Complexity
    # Best               O(n)
    # Worst              O(n^2)
    # Average            O(n^2)
    # Space Complexity   O(1)
    # Stability	         YES
    for i in range(1, len(lst)):
        elem = lst[i]
        j = i - 1
        while j >= 0 and elem < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = elem
    return lst

def merge_sort(lst):
    # Time Complexity
    # Best               O(n*log n)
    # Worst              O(n*log n)
    # Average            O(n*log n)
    # Space Complexity   O(n)
    # Stability	         YES
    if len(lst) > 1:
        lst1, lst2 = lst[:len(lst) // 2], lst[len(lst) // 2:]
        merge_sort(lst1)
        merge_sort(lst2)
        i = j = k = 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] < lst2[j]:
                lst[k] = lst1[i]
                i += 1
            else:
                lst[k] = lst2[j]
                j += 1
            k += 1
        while i < len(lst1):
            lst[k] = lst1[i]
            i += 1
            k += 1
        while j < len(lst2):
            lst[k] = lst2[j]
            j += 1
            k += 1
    return lst

def partition(lst, start, stop):
    more_index = start - 1
    for j in range(start, stop):
        if lst[j] <= lst[stop]:
            more_index = more_index + 1
            if j != more_index:
                lst[more_index], lst[j] = lst[j], lst[more_index]
    lst[more_index + 1], lst[stop] = lst[stop], lst[more_index + 1]
    return more_index + 1

def quick_sort(lst, start, stop):
    # Time Complexity
    # Best               O(n*log n)
    # Worst              O(n^2)
    # Average            O(n*log n)
    # Space Complexity   O(log n)
    # Stability	         NO
    if start < stop:
        pivot = partition(lst, start, stop)
        quick_sort(lst, start, pivot - 1)
        quick_sort(lst, pivot + 1, stop)
    return lst

def counting_sort(lst):
    # Time Complexity
    # Best               O(n+k)
    # Worst              O(n+k)
    # Average            O(n+k)
    # Space Complexity   O(max)
    # Stability	         YES
    count_elem = {}
    for i in lst:
        count_elem[i] = count_elem.get(i, 0) + 1
    res = []
    for i,j in count_elem.items():
        res.extend([i] * j)
    return res

def radix_sort(lst):
    # Time Complexity
    # Best               O(n+k)
    # Worst              O(n+k)
    # Average            O(n+k)
    # Space Complexity   O(max)
    # Stability	         YES
    maximum, place = max(lst), 1
    while maximum // place > 0:
        output, count = [0] * len(lst), [0] * 10
        for i in lst:
            index = i // place
            count[index % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = len(lst) - 1
        while i >= 0:
            index = lst[i] // place
            output[count[index % 10] - 1] = lst[i]
            count[index % 10] -= 1
            i -= 1
        for i in range(len(lst)):
            lst[i] = output[i]
        place *= 10
    return lst

def heapify(lst, n, i):
    largest, left, right = i, 2 * i + 1, 2 * i + 2
    if left < n and lst[left] > lst[largest]:
        largest = left
    if right < n and lst[right] > lst[largest]:
        largest = right
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)
    return
def heap_sort(lst):
    # Time Complexity
    # Best               O(n*log n)
    # Worst              O(n*log n)
    # Average            O(n*log n)
    # Space Complexity   O(1)
    # Stability	         NO
    res = []
    n = len(lst)
    for i in range(n // 2, -1, -1):
        heapify(lst, n, i)
    for i in range(n - 1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        res.insert(0, lst[i])
        heapify(lst, i, 0)
    return res

def shell_sort(lst):
    interval = len(lst) // 2
    while interval > 0:
        for i in range(interval, len(lst)):
            temp = lst[i]
            j = i
            while j >= interval and lst[j - interval] > temp:
                lst[j] = lst[j - interval]
                j -= interval
            lst[j] = temp
        interval //= 2
    return lst

list = [121, 432, 564, 23, 1, 45, 788]
print(shell_sort(list))