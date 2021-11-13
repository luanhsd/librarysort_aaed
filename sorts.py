def bubblesort(array):
    status = True
    compare = 0
    moves = 0

    for i in range(len(array)):
        for j in range(1, len(array) - i):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                moves += 3
                status = False
            compare += 1

        if status:
            break

    return compare, moves


def insertionsort(array):
    compare = 0
    moves = 0

    for i in range(len(array)):
        aux = array[i]
        moves += 1
        j = i - 1
        if j >= 0:
            compare += 1
        while j >= 0 and aux < array[j]:
            array[j + 1] = array[j]
            moves += 1
            j -= 1
        array[j + 1] = aux
        moves += 1
    return compare, moves


def selectionsort(array):
    compare = 0
    moves = 0

    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
            compare += 1
        array[i], array[min] = array[min], array[i]
        moves += 3
    return compare, moves


compare_heap = 0
moves_heap = 0


def heapify(array, n, i):
    global compare_heap
    global moves_heap

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        if array[i] < array[left]:
            largest = left
        compare_heap += 1
    if right < n:
        if array[largest] < array[right]:
            largest = right
            compare_heap += 1
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        moves_heap += 3
        heapify(array, n, largest)


def heapsort(array):
    global compare_heap
    global moves_heap

    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        moves_heap += 3
        heapify(array, i, 0)
    return compare_heap, moves_heap


def mergesort(array):
    compare = 0
    moves = 0

    if(len(array) > 1):
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        mergesort(left)
        mergesort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            compare += 1
            if left[i] < right[j]:
                array[k] = left[i]
                moves += 1
                i += 1
            else:
                array[k] = right[j]
                moves += 1
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            moves += 1
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            moves += 1
            j += 1
            k += 1
    return compare, moves


def quicksort(array, inicio=0, fim=None):
    compare = 0
    moves = 0

    if fim is None:
        fim = len(array)-1
    if inicio < fim:
        p, count_compare, count_move = partition(array, inicio, fim)
        compare += count_compare
        moves += count_move
        quicksort(array, inicio, p-1)
        quicksort(array, p+1, fim)
    return compare, moves


def partition(array, inicio, fim):
    compare = 0
    moves = 0

    pivot = array[fim]
    i = inicio
    for j in range(inicio, fim):
        compare += 1
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i = i + 1
            moves += 3
    array[i], array[fim] = array[fim], array[i]
    moves += 3
    return i, compare, moves


def librarysort(array):
    compare = 0
    moves = 0

    length = len(array)
    # cria a lista com espacos em branco e popula com os dados da lista
    auxList = [None]*(length << 1)
    for i in range(length):
        auxList[2*i+1] = array[i]

    a, b = 1, 2
    for i in range(length):
        a <<= 1
        b <<= 1
        for j in range(a, min(b, length+1)):
            p = 2*j-1
            s = auxList[p]
            # Realiza a busca binaria
            x, y = 0, p
            while y-x > 1:
                c = (x+y) >> 1
                if auxList[c] != None:
                    if auxList[c] < s:
                        x = c
                    else:
                        y = c
                    compare += 1
                else:
                    e, f = c-1, c+1
                    while auxList[e] == None:
                        e -= 1
                    while auxList[f] == None:
                        f += 1
                    if auxList[e] > s:
                        y = e
                    elif auxList[f] < s:
                        compare += 1
                        x = f
                    else:
                        compare += 1
                        x, y = e, f
                        break
                    compare += 1
            if y-x > 1:
                auxList[(x+y) >> 1] = s
                moves += 1
            else:
                if auxList[x] != None:
                    if auxList[x] > s:
                        y = x
                    compare += 1
                    while s != None:
                        auxList[y], s = s, auxList[y]
                        y += 1
                        moves += 3
                else:
                    auxList[x] = s
                    moves += 1
            auxList[p] = None
        if b > length:
            break
        if i < length-1:
            s = p
            while s >= 0:
                if auxList[s] != None:
                    auxList[s], auxList[p] = None, auxList[s]
                    p -= 2
                    moves += 3
                s -= 1
    return compare, moves


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print(arr)
    print("Sorted array is: ", end="\n")
    print(heapsort(arr))
