def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return first_string, second_string, False

    first_word = list(first_string.lower())
    second_word = list(second_string.lower())

    merge_sort(first_word)
    merge_sort(second_word)

    sorted_first = "".join(first_word)
    sorted_second = "".join(second_word)

    return sorted_first, sorted_second, sorted_first == sorted_second
# result = is_anagram("pedra", "perdaaa")
# print(result)  # Saída: ('amor', 'amor', True)
