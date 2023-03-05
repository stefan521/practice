# ----- Q1 -----
# O(n) with built-in functions
def contains_unique_characters_built_in_func(word):
    return len(set(word)) == len(word)


# O(n) dictionary
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


# ----- Q2 -----
# O(n)
def strings_contain_same_letter_dict(lhs, rhs):
    letter_count = {}

    if len(lhs) != len(rhs):
        return False

    for letter in lhs:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    for letter in rhs:
        letter_count[letter] = letter_count.get(letter, 0) - 1

    for count in letter_count.values():
        if count != 0:
            return False

    return True


# ----- Q3 -----
def url_safe_string(input_string):
    letters = []
    for letter in input_string:
        if letter == " " and letters and letters[len(letters) - 1] != "%20":
            letters.append("%20")
        elif letter != " ":
            letters.append(letter)

    return "".join(letters).rstrip("%20")


def main():
    print("run python3 -m pytest")


if __name__ == "__main__":
    main()