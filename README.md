# sorting_algorithm

## Heap sort

Heap sort works by determining the largest (or smallest) element of the list, placing that at the end (or beginning) of the list, then continuing with the rest of the list, but accomplishes this task efficiently by using a data structure called a heap, a special type of binary tree.

## Select sort

Select sort proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

## Quick sort

Quicksort is partition an array an element called a pivot is selected. All elements smaller than the pivot are moved before it and all greater elements are moved after it. The lesser and greater sublists are then recursively sorted.

## Merge sort

Merge sort starts by comparing every two elements (i.e., 1 with 2, then 3 with 4...) and swapping them if the first should come after the second. It then merges each of the resulting lists of two into lists of four, then merges those lists of four, and so on; until at last two lists are merged into the final sorted list.

## Insert sort

Insertion sort works by taking elements from the list one by one and inserting them in their correct position into a new sorted list.

## Shell sort

Shell sort starts by sorting pairs of elements far apart from each other, then progressively reducing the gap between elements to be compared.

## Bubble sort

The bubble sort compares the first two elements, and if the first is greater than the second, it swaps them. It continues doing this for each pair of adjacent elements to the end of the data set. It then starts again with the first two elements, repeating until no swaps have occurred on the last pass.
