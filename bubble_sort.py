import numpy as np

def bubble_sort(arr: np.ndarray) -> np.ndarray:
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage:
if __name__ == "__main__":
    sample_arr = np.array([64, 34, 25, 12, 22, 11, 90])
    print(f"Original array: {sample_arr}")
    sorted_arr = bubble_sort(sample_arr)
    print(f"Sorted array: {sorted_arr}")
