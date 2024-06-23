# ----- Q1 -----
# O(n) with built-in functions
import copy


def contains_unique_characters_built_in_func(word: str):
    return len(set(word)) == len(word)


# O(n) dictionary
def contains_unique_characters_dict(word: str):
    letter_map = {}
    for letter in word:
        letter_map[letter] = True
    return len(letter_map) == len(word)


# O(n^2)
def contains_unique_characters_stupid_slow(word: str):
    for index, letter1 in enumerate(word):
        for letter2 in word[index + 1:]:
            if letter1 == letter2:
                return False
    return True


# O(n * log(n)) because of sorting
def contains_unique_characters_sorting(word: str):
    if not word:
        return True
    sorted_word = sorted(word)
    for index, letter in enumerate(sorted_word):
        if letter == sorted_word[index - 1]:
            return False
    return True


# ----- Q2 -----
# O(n)
def strings_contain_same_letter_dict(lhs: str, rhs: str):
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
# O(n)
def url_safe_string(input_string: str):
    letters = []
    for letter in input_string:
        if letter == " " and letters and letters[len(letters) - 1] != "%20":
            letters.append("%20")
        elif letter != " ":
            letters.append(letter)

    return "".join(letters).rstrip("%20")


# ----- Q4 -----
# O(n)
def is_palindrome_permutation(word: str):
    letters = {}
    odd_counts = 0

    for letter in word:
        letters[letter] = letters.get(letter, 0) + 1

    for count in letters.values():
        if count % 2 == 1 and odd_counts < 1:
            odd_counts += 1
        elif count % 2 == 1:
            return False

    return True


# ----- Q5 -----
# O(n)
def _one_extra_letter(shorter: str, longer: str):
    mismatches = 0
    idx1 = 0
    idx2 = 0

    while idx1 < len(shorter):
        if shorter[idx1] == longer[idx2]:
            idx1 += 1
            idx2 += 1
        elif shorter[idx1] != longer[idx2] and mismatches > 0:
            return False
        elif shorter[idx1] != longer[idx2]:
            mismatches += 1
            idx2 += 1

    return mismatches <= 1


def _one_mismatch(lhs, rhs: str):
    mismatches = 0

    for idx, letter in enumerate(lhs):
        if rhs[idx] != letter and mismatches > 0:
            return False
        elif rhs[idx] != letter:
            mismatches += 1

    return True


def one_edit_away(lhs: str, rhs: str):
    if abs(len(lhs) - len(rhs)) > 1:
        return False

    if len(lhs) == len(rhs):
        return _one_mismatch(lhs, rhs)

    if len(lhs) < len(rhs):
        return _one_extra_letter(lhs, rhs)

    return _one_extra_letter(rhs, lhs)


# ----- Q6 -----
# O(n)
def compress_string(word: str):
    compressed = []
    count = 1

    if len(word) < 2:
        return word

    def append(character: str):
        if count >= 2:
            compressed.extend([character, str(count)])
        else:
            compressed.append(character)

    for idx in range(0, len(word) - 1):
        if word[idx] == word[idx + 1]:
            count += 1
        else:
            append(word[idx])
            count = 1

    append(word[len(word) - 1])

    return "".join(compressed)


# ----- Q7 -----
def rotate_image(image: list):
    new_image = copy.deepcopy(image)
    for x, column in enumerate(image):
        for y, value in enumerate(column):
            new_image[y][len(column) - x - 1] = value

    return new_image


# ----- Q8 -----
def propagate0(matrix: list):
    new_matrix = copy.deepcopy(matrix)
    columns = []
    rows = []

    for x, column in enumerate(matrix):
        for y, value in enumerate(column):
            if value == 0:
                columns.append(x)
                rows.append(y)

    for x, column in enumerate(matrix):
        for y, value in enumerate(column):
            if x in columns or y in rows:
                new_matrix[x][y] = 0

    return new_matrix


# ----- Q9 -----
def is_rotation(lhs: str, rhs: str):
    return rhs in (lhs + lhs)


def main():
    print("run python3 -m pytest")


if __name__ == "__main__":
    main()
