def count_letters(book_text):
    letters = {}
    for w in book_text.split():
        for l in w.lower():
            if not l.isalpha():
                continue
            if not l in letters:
                letters[l] = 0
            letters[l] += 1

    return letters


def sort_on(dict):
    return dict["count"]

def main():
    fname = "books/frankenstein.txt"
    with open(fname) as book_file:
        book_contents = book_file.read()
        words = len(book_contents.split())

        letters = count_letters(book_contents)
        letters_sorted = []
        for l in letters:
            letters_sorted.append({"count": letters[l], "letter": l})
        letters_sorted.sort(reverse=True, key=sort_on)

        print(f"--- Begin report of {fname} ---")
        print(f"{words} words found in the document\n")

        for letter_dict in letters_sorted:
            letter = letter_dict["letter"]
            letter_count = letter_dict["count"]
            print(f"The '{letter}' character was found {letter_count} times")

        print("--- End report ---")



if __name__ == "__main__":
    main()

