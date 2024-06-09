def find_max_min(array):
    max_number = array[0]
    min_number = array[0]

    for number in array:
        if number > max_number:
            max_number = number
        elif number < min_number:
            min_number = number

    return max_number, min_number
