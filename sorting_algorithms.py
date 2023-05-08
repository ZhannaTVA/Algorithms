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

def quicksort(lst):


list = [6, 5, 3, 1, 8, 7, 2, 4]
print(merge_sort(list))