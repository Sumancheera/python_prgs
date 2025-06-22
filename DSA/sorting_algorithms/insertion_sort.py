def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    # The first element (index 0) is considered sorted.
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted

        j = i - 1
        while j >= 0 and key < arr[j]: #in comparision if it faild, it inserts
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1
        arr[j + 1] = key  # Place key in its correct position,after comparision
    return arr

# --- Example Usage ---
if __name__ == "__main__":
    my_list = [12, 11, 13, 5, 6]
    print(f"Original list: {my_list}")
    result=insertion_sort(my_list)
    print(result)