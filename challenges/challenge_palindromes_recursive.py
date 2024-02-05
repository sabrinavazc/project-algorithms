def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if low_index >= high_index:
        return True
    else:
        return (
            word[low_index] == word[high_index]
            and is_palindrome_recursive(word, low_index + 1, high_index - 1)
            )


print(is_palindrome_recursive("ana", 0, len("ana") - 1))  # True
