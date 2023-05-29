def merge_str(left, right):
    merged = []
    left_string = 0
    right_string = 0

    while left_string < len(left) and right_string < len(right):
        if left[left_string] <= right[right_string]:
            merged.append(left[left_string])
            left_string += 1
        else:
            merged.append(right[right_string])
            right_string += 1

    while left_string < len(left):
        merged.append(left[left_string])
        left_string += 1

    merged.extend(right[right_string:])

    return ''.join(merged)


def merge_sort(string):
    if len(string) <= 1:
        return "".join(string)

    middle = len(string) // 2

    left = merge_sort(string[:middle])
    right = merge_sort(string[middle:])
    return merge_str(left, right)


def is_anagram(first_string, second_string):
    first = merge_sort(first_string.lower())
    second = merge_sort(second_string.lower())

    if first_string == "" and second_string == "":
        return ("".join(first), "".join(second), False)

    if first == second:
        return ("".join(first), "".join(second), True)

    if first != second:
        return ("".join(first), "".join(second), False)

    if len(first) == 0 or len(second) == 0:
        return ("".join(first), "".join(second), True)

    else:
        return ("".join(first), "".join(second), False)

    boole = first == second
    return (first, second, boole)
