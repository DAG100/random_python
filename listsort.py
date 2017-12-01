def list_sorter(array):
    """A Deven-made function (obviously terribly inefficient) that sorts a numerical list in descending order.
    Takes a list as input and nothing else."""
    unsorted_list = array[1:]
    sorted_list = [array[0], ]
    for i in range(len(unsorted_list)):
        temp = unsorted_list[i]
        j = int(0)
        while temp < sorted_list[j]:
            if j + 1 == len(sorted_list):
                sorted_list.append(temp)  # since j is equal to length of list, temp must be smaller than all of list. Thus, we append it.
                break
            else:
                j += 1  # increment j to compare other value
        else:
            sorted_list.insert(j, temp)
    return sorted_list
