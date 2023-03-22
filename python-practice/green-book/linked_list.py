# ===== Q1 =====

def remove_duplicates(lst):
    seen = set()
    new_list = []

    for element in lst:
        if element not in seen:
            new_list.append(element)
            seen.add(element)

    return new_list


def main():
    print("run python3 -m pytest")


if __name__ == "__main__":
    main()
