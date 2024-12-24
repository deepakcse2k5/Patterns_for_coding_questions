def letter_combinations(digits):
    # edge case
    if len(digits)==0:
        return []
    combinations = []
    digits_mapping = {
        "1": [""],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]}
    
    backtrack(0, [], digits, digits_mapping, combinations)
    return combinations

def backtrack(index, path, digits, letters, combinations):
    if len(path) == len(digits):
        combinations.append(''.join(path))
        return
    possible_letters = letters[digits[index]]
    if possible_letters:
        for letter in possible_letters:
            path.append(letter)
            backtrack(index+1,path, digits, letters, combinations)
            path.pop()


if __name__ == "__main__":
    print(letter_combinations("23"))
    print(letter_combinations("456"))
    
