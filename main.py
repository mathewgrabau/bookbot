def count_letters(book_text):
    letters = {}
    for w in book_text.split():
        for l in w.lower():
            if not l in letters:
                letters[l] = 0
            letters[l] += 1

    return letters


def main():
    with open("books/frankenstein.txt") as book_file:
        book_contents = book_file.read()
        words = len(book_contents.split())
        print(words)

        letters = count_letters(book_contents)
        print(letters)


if __name__ == "__main__":
    main()

