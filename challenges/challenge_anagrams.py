def is_anagram(first_string, second_string):

    first = first_string.lower()
    second = second_string.lower()

    def sort_string(word):
        if len(word) <= 1:
            return word
        split = word[len(word) // 2]
        right = [i for i in word if i > split]
        mid = [i for i in word if i == split]
        left = [i for i in word if i < split]
        return sort_string(left) + mid + sort_string(right)

    first_list = sort_string(list(first))
    second_list = sort_string(list(second))
    first = "".join(first_list)
    second = "".join(second_list)

    if len(first_list) != len(second_list):
        return (first, second, False)

    if first_string == '' or second_string == '':
        return (first, second, False)

    word = first == second

    return (first, second, word)
