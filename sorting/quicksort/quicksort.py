from typing import List

def partition(arr:List[int],lo:int,hi:int) -> int:
    pivot = arr[hi] 
    temp_pivot = lo-1
    for j in range(lo,hi-1):
        if arr[j] < pivot:
            temp_pivot +=1
            arr[temp_pivot], arr[j] = arr[j],arr[temp_pivot]
    arr[temp_pivot+1], arr[hi] = arr[hi], arr[temp_pivot+1]
    return temp_pivot+1

def quicksort(arr:List[int]) -> List[int]:
    return []
if __name__ == "__main__":
    arr = [5, 3, 21, 6, 9]
    original = arr[:]
    sorted_arr = quicksort(arr)
    print(f"this is the sorted {sorted_arr}")
    print(f"this is the original {original}")