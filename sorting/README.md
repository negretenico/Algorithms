# Sorting

The goal of these algorithims is to put a elements of a list in order.

## Formal Definition

---
Formally, the output of any sorting algorithm must satisfy two conditions:

1. The output is in monotonic order (each element is no smaller/larger than the previous element, according to the required order).
2. The output is a permutation (a reordering, yet retaining all of the original elements) of the input.

[Credit](https://en.wikipedia.org/wiki/Sorting_algorithm)

## Example

---
[4,32,5,7,1,3] -> [1,3,4,5,7,32]

### Algorithims

1. HeapSort
   1. Uses a heap datastrucutre to achieve the sorting
   2. modifies the provided array and does NOT return a new array rather the modfified version of the given array
   3. θ(nlog(n)) where n is the size of the array
