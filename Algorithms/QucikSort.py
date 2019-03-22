def quickSort(input_list):
    quickSortProcess(input_list, 0, len(input_list)-1)


def quickSortProcess(input_list, first, last):
    if first < last:
        split_point = partition(input_list, first, last)
        quickSortProcess(input_list, first, split_point - 1)
        quickSortProcess(input_list, split_point + 1, last)


def partition(input_list, first, last):
    pivot_value = input_list[first]  # can choice the pivot_value by another way
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and input_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while right_mark >= left_mark and input_list[right_mark] >= pivot_value:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            # swap
            temp = input_list[right_mark]
            input_list[right_mark] = input_list[left_mark]
            input_list[left_mark] = temp

    # because pivot is a first value of input_list. therefor after finish the while loop, we
    # have to partition, we swap input_list[right_mark] and first element.
    temp = input_list[first]
    input_list[first] = input_list[right_mark]
    input_list[right_mark] = temp

    # return the last index of first partition. which part < pivot_value.
    return right_mark


def main():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    quickSort(alist)
    print(alist)


# Call the function
main()
