def insertSort(input_list):
    for i in range(1, len(input_list)):
        # current element to compare
        current = input_list[i]

        while i > 0 and input_list[i - 1] > current:
            # swap inputList[i-1] and inputList[i]
            input_list[i] = input_list[i - 1]
            i = i - 1
            input_list[i] = current
        print(input_list)
    return input_list


def main():
    insertSort([5, 4, 3, 2, 1])


# Call the function:
main()
