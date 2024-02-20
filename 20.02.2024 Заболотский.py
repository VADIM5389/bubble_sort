#def bubble_sort(arr):
#    n = len(arr)
#    for i in range(n):
#        for j in range(0, n-i-1):
#            if arr[j] > arr[j+1]:
#                arr[j], arr[j+1] = arr[j+1], arr[j]
#    return arr
#
#arr = [64, 34, 25, 12, 22, 11, 90]
#print("Исходный список:", arr)
#sorted_arr = bubble_sort(arr)
#print("Отсортированный список:", sorted_arr)

def naive_search(text, pattern):
    indices = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i: i + len(pattern)] == pattern:
            indices.append(i)
    return indices

text = input("Введите текст")
pattern = input("Введите текст для поиска")
print(naive_search(text, pattern))
