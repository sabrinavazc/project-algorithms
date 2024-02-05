def sort_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return sort_sort(left) + middle + sort_sort(right)


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return first_string, second_string, False

    first_word = list(first_string.lower())
    second_word = list(second_string.lower())

    first_word[:] = sort_sort(first_word)
    second_word[:] = sort_sort(second_word)

    sorted_first = "".join(first_word)
    sorted_second = "".join(second_word)

    return sorted_first, sorted_second, sorted_first == sorted_second
# result = is_anagram("pedra", "perdaaa")
# print(result)  # Saída: ('amor', 'amor', True)
