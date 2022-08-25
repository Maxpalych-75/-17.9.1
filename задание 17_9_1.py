array_no_sort = input('введите последовательность чисел = ').split()
array = list(map(int, array_no_sort))
#list.sort(array) - почему нет?
for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print("сортируем полученный список = ", array)

element = int(input('введите любое число = '))

def binary_search_recursive(array, element, left, right):
    if left > right:
        for k in range(len(array)):
            if element < array[k]:
                break
        else:
            k = len(array)
        return k

    mid = (left + right) // 2
    if element == array[mid]:
        return mid
    if element < array[mid]:
        return binary_search_recursive(array, element, left, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, right)

print("Номер позиции меньшего числа: {}".format(binary_search_recursive(array, element, 0, len(array))))

