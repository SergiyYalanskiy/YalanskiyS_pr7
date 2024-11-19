def bubble_sort(arr):
    """Бульбашкове сортування."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Обмін місцями
    return arr


def selection_sort(arr):
    """Сортування вибором."""
    n = len(arr)
    for i in range(n):
        # Знаходимо індекс мінімального елемента в залишку списку
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Обмін місцями поточного елемента і мінімального
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    """Сортування вставками."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Зсув елементів, більших за key, на одну позицію вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Приклад використання
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Бульбашкове сортування:", bubble_sort(data.copy()))
    print("Сортування вибором:", selection_sort(data.copy()))
    print("Сортування вставками:", insertion_sort(data.copy()))