# Merge Sort Algorithm

This repository contains a Python implementation of the **Merge Sort** algorithm, a highly efficient, comparison-based sorting algorithm. It's a key example of the "divide and conquer" paradigm in computer science.

---

## What is Merge Sort?

Merge Sort works by:
1.  **Dividing** the unsorted list into `n` sublists, each containing one element (a list of one element is considered sorted).
2.  **Conquering** by recursively splitting the list in half until individual elements are reached.
3.  **Combining** (merging) sublists to produce new sorted sublists until there is only one sorted list remaining.

This algorithm is known for its **stability** (it preserves the relative order of equal elements) and guaranteed **O(n log n)** time complexity, making it efficient for large datasets.

---

## How the Code Works

The `merge_sort` function in `main.py` (or wherever you save your code) implements the algorithm:

* **`merge_sort(array)` function:**
    * **Base Case:** If the input `array` has 1 or fewer elements, it's already sorted, so the function returns.
    * **Divide:** The array is split into two halves: `left_part` and `right_part`.
    * **Conquer (Recursive Calls):** `merge_sort` is called on both `left_part` and `right_part`. This recursive nature continues until arrays of size 1 are reached.
    * **Combine (Merging):** After the recursive calls return, the two sorted `left_part` and `right_part` arrays are merged back into the original `array`.
        * Three index variables (`left_array_index`, `right_array_index`, `sorted_index`) are used to keep track of the current positions in the `left_part`, `right_part`, and the main `array`, respectively.
        * A `while` loop compares elements from `left_part` and `right_part`, placing the smaller one into the correct position in the `array` and incrementing the relevant indices.
        * After the main loop, two additional `while` loops handle any remaining elements in either `left_part` or `right_part` (which would already be sorted) by simply appending them to the `array`.

---

## Getting Started

### Prerequisites

* Python 3.x installed on your system.

### How to Run

1.  **Save the code:** Copy the `merge_sort` function and the `if __name__ == '__main__':` block into a Python file (e.g., `merge_sort_example.py`).

    ```python
    def merge_sort(array):
        if len(array) <= 1:
            return

        middle_point = len(array) // 2
        left_part = array[:middle_point]
        right_part = array[middle_point:]

        merge_sort(left_part)
        merge_sort(right_part)

        left_array_index = 0
        right_array_index = 0
        sorted_index = 0

        while left_array_index < len(left_part) and right_array_index < len(right_part):
            if left_part[left_array_index] < right_part[right_array_index]:
                array[sorted_index] = left_part[left_array_index]
                left_array_index += 1
            else:
                array[sorted_index] = right_part[right_array_index]
                right_array_index += 1
            sorted_index += 1

        while left_array_index < len(left_part):
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
            sorted_index += 1

        while right_array_index < len(right_part):
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
            sorted_index += 1


    if __name__ == '__main__':
        numbers = [4, 10, 6, 14, 2, 1, 8, 5]
        print('Unsorted array: ')
        print(numbers)
        merge_sort(numbers)
        print('Sorted array: ' + str(numbers))
    ```

2.  **Open your terminal or command prompt.**
3.  **Navigate to the directory** where you saved the file.
4.  **Run the script** using the Python interpreter:

    ```bash
    python merge_sort_example.py
    ```

### Expected Output