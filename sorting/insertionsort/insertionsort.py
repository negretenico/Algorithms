from typing import List


def insertion_sort(arr:List[int]) -> None:
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1
        while j >=0 and arr[j] > key:
            arr[j+1] =arr[j]
            j -=1
        arr[j+1] = key
if __name__ =="__main__":
    arr = [5, 3, 21, 6, 9]
    original = arr[:]
    insertion_sort(arr)
    print(f"this is the sorted {arr}")
    print(f"this is the original {original}")