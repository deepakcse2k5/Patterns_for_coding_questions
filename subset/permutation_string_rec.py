words = "bcd"

def swap_char(word, i, j):
    swap_index = list(word)
    swap_index[i], swap_index[j] = swap_index[j], swap_index[i]
    return ''.join(swap_index)


def permutation_string_rec(word, current_index, result):
    if current_index==1:
        result.append(word)
    for index in range(current_index, len(word)):
        swapped_str = swap_char(word, current_index, index)
        permutation_string_rec(swapped_str, current_index+1, result)


def permute_word(word):
    result = []
    permutation_string_rec(word, 0, result)
    return result


# Driver code
def main():
    input_word = ["ab", "bad", "abcd"]

    for index in range(len(input_word)):
        permuted_words = permute_word(input_word[index])
        print(index + 1, ".\t Input string: '", input_word[index], "'", sep="")
        print("\t All possible permutations are: ",
              "[", ', '.join(permuted_words), "]", sep="")
        print('-' * 100)


if __name__ == '__main__':
    main()

