def count_positives_negatives(array):
    positive_count = 0
    negative_count = 0

    for number in array:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1

    return positive_count, negative_count
