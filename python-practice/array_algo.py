def contains_unique_characters1(word):
    return len(set(word)) == len(word)


def contains_unique_characters2(word):
    letter_map = {}
    for letter in word:
        letter_map[letter] = True
    return len(letter_map) == len(word)


# sorting makes this better
def contains_unique_characters_stupid_slow(word):
    for index, letter1 in enumerate(word):
        for letter2 in word[index + 1:]:
            if letter1 == letter2:
                return False
    return True


def main():
    print("run python3 -m pytest")


if __name__ == "__main__":
    main()
