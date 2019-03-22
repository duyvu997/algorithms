def mergeSort(input_list):
    if len(input_list) > 1:
        # SPLITTING
        middle = len(input_list) // 2
        left_half = input_list[:middle]
        right_half = input_list[middle:]

        # RECURSION
        mergeSort(left_half)
        mergeSort(right_half)

        # MERGING
        i = 0
        j = 0
        k = 0
        sorted_list = input_list # just copy. not is a answer
        # after left_half and right_half has sorted. merge them.
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                sorted_list[k] = left_half[i]
                i = i + 1
            else:
                sorted_list[k] = right_half[j]
                j = j + 1
            k = k + 1
        # when right_half is empty, and left_half is not. copy left_half to sorted_list.
        while i < len(left_half):
            sorted_list[k] = left_half[i]
            k = k + 1
            i = i + 1
        # otherwise copy right_half to sorted_list
        while j < len(right_half):
            sorted_list[k] = right_half[j]
            k = k + 1
            j = j + 1

    print("merging", input_list)


def main():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(alist)
    print(alist)


# Call the main function
main()
