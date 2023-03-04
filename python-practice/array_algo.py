# O(n) with built-in functions
def contains_unique_characters_built_in_func(word):
    return len(set(word)) == len(word)


# O(n) bit vector saves more space
def contains_unique_characters_dict(word):
    letter_map = {}
    for letter in word:
        letter_map[letter] = True
    return len(letter_map) == len(word)


# O(n^2)
def contains_unique_characters_stupid_slow(word):
    for index, letter1 in enumerate(word):
        for letter2 in word[index + 1:]:
            if letter1 == letter2:
                return False
    return True


# O(n * log(n)) because of sorting
def contains_unique_characters_sorting(word):
    if not word:
        return True
    sorted_word = sorted(word)
    for index, letter in enumerate(sorted_word):
        if letter == sorted_word[index - 1]:
            return False
    return True


def main():
    print("run python3 -m pytest")


if __name__ == "__main__":
    main()
