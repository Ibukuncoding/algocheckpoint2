def insertion_sort(arr):
    # Loop through the array from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be inserted
        j = i - 1     # Index of the last element in the sorted section

        # Move elements of arr[0..i-1] that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1

        arr[j + 1] = key  # Place the key in its correct position

    return arr

# Example usage
if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6]
    sorted_array = insertion_sort(sample_array)
    print("Sorted array:", sorted_array)
