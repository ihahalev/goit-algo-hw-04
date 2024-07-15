from timeit import timeit
from random import randint

# Сортування вставками (Insertion sort)
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

# Сортування злиттям (Merge sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Залишки додаємо до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

n = 10**5
# підготуємо данні для кожного методу, щоб не втрачати час на сортування
insert_data = []
merge_data = []
sort_data = []
for _ in range(n):
    insert_data.append(randint(1, n))
    merge_data.append(randint(1, n))
    sort_data.append(randint(1, n))

# використовуємо лямбда функції для зменшення впливу на час заміру
insertion_sort_time = timeit(lambda: insertion_sort(insert_data), number=1)
merge_sort_time = timeit(lambda: merge_sort(merge_data), number=1)
timsort_time = timeit(lambda: sort_data.sort(), number=1)

print(f"Insertion Sort time: {insertion_sort_time:.6f} seconds")
print(f"Merge Sort time: {merge_sort_time:.6f} seconds")
print(f"Timsort time: {timsort_time:.6f} seconds")
