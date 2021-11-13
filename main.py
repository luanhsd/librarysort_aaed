import random
from order import Order
from sorts import *
from fileResult import FileResult
from time import process_time
from sys import setrecursionlimit
from threading import Thread, stack_size

setrecursionlimit(200000)
stack_size(134217728)


# criacao da lista ordenada
def orderedListGenerate(quantity):
    listordered = list(range(quantity))
    return listordered


# criacao da lista ordenada inversalmente
def inverseListGenerate(quantity):
    listinversed = list(reversed(range(quantity)))
    return listinversed


def almostListGenerate(quantity):
    almostlist = list(range(quantity))
    step = int((quantity * 10)/100)
    for i in range(0, quantity - 1, step):
        almostlist[i], almostlist[i+1] = almostlist[i+1], almostlist[i]
    return almostlist


def randomListGenerate(quantity):
    listrandom = list(range(quantity))
    random.shuffle(listrandom)
    return listrandom


def orderFactory(quantity: int, order):
    retriever = {
        1: orderedListGenerate,
        2: inverseListGenerate,
        3: almostListGenerate,
        4: randomListGenerate
    }
    return retriever[order.value](quantity)


def list_generate(quantity: int, order):
    return orderFactory(quantity, order)


def init_thread(algorithm, array, file, key, order, qtd):
    start = process_time()
    compare, moves = algorithm(array)
    end = process_time()

    count_blocked = 0
    while True:
        try:
            file.insert_file(
                f'{key},{order.name},{qtd},{compare},{moves},{end - start}')
            break
        except Exception as error:
            count_blocked += 1
            print(f'File blocked: {count_blocked}')


def main():
    threads = []
    file = FileResult()
    file.insert_file('algorithm,order,quantity,compare,moves,processing_time')
    quantity = [10, 100, 1000, 10000, 100000]  # 1000000
    algorithms = {
        'bubblesort': bubblesort,
        'insertionsort': insertionsort,
        'selectionsort': selectionsort,
        'heapsort': heapsort,
        'mergesort': mergesort,
        'quicksort': quicksort,
        'librarysort': librarysort
    }
    for qtd in quantity:
        for order in Order:
            for key, algorithm in algorithms.items():
                array = list_generate(qtd, order)
                threads.append(Thread(target=init_thread, args=(
                    algorithm, array, file, key, order, qtd, )))
                threads[len(threads)-1].start()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f'Error: {error}')
