from typing import List
from heapq import heapify,heappop

def parent(i:int) -> int:
    return i//2


def left(i:int) -> int:
    return 2 * i+1 # we adjust for 0 based indexing; however the text will say 2i


def right(i:int) -> int:
    return 2*i+2   # we adjust for 0 based indexing; however the text will say 2i+1

def max_heapify(arr:List[int], i:int,heap_size:int) -> None:
    l = left(i)
    r = right(i)
    if l < heap_size and arr[l] > arr[i]:
        largest = l
    else: 
        largest = i
    if r < heap_size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,largest,heap_size)


def build_max_heap(arr:List[int], n:int) ->None: 
    heap_size = n
    for i in range(n // 2, -1, -1):
        max_heapify(arr,i,heap_size) 
def heapsort(arr: List[int]) -> List[int]:
    build_max_heap(arr, len(arr))
    n = len(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        n -= 1
        max_heapify(arr,0,n)
    return arr


def inbuilt_heap_sort(arr:List[int]) -> List[int]:
    res = []
    heapify(arr) # this uses a min heap 
    while arr:
        smallest = heappop(arr)
        res.append(smallest)
    return res
if __name__=="__main__":
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    original = arr[:]
    sorted_arr = heapsort(arr)
    print(f"this is the sorted {sorted_arr}")
    print(f"this is the original {original}")