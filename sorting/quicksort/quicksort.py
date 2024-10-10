from typing import List

def partition(arr:List[int],lo:int,hi:int) -> int:
    pivot = arr[hi] 
    temp_pivot = lo-1
    for j in range(lo,hi):
        if arr[j] < pivot:
            temp_pivot +=1
            arr[temp_pivot], arr[j] = arr[j],arr[temp_pivot]
    arr[temp_pivot+1], arr[hi] = arr[hi], arr[temp_pivot+1]
    return temp_pivot+1

def quicksort(arr:List[int],p,r) -> None:
    if p< r: 
        q = partition(arr,p,r)
        quicksort(arr,p,q-1) #low end
        quicksort(arr, q+1,r) #high end
if __name__ == "__main__":
    arr = [5, 3, 21, 6, 9]
    original = arr[:]
    quicksort(arr,0,len(arr)-1)
    print(f"this is the sorted {arr}")
    print(f"this is the original {original}")