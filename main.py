def word_count(text):
    words = text.split()

    return len(words)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def count_letters_in_text(text):
    letter_count = {}
    lowered_text = text.lower()

    for char in lowered_text:
        if char.isalpha():
            if not char in letter_count:
                letter_count[char] = 0
            letter_count[char] += 1

    return letter_count

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    list_of_dict = []

    for key in dict:
        list_of_dict.append({"char": key, "num": dict[key]})

    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

def print_report(book, words, letters):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print()

    for i in range(0, len(letters)):
        dict = letters[i]
        print(f"The '{dict["char"]}' character was found {dict["num"]} times")

    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    words = word_count(book_text)
    letter_count = count_letters_in_text(book_text)
    sorted_letter_count = sort_dict(letter_count)

    print_report(book_path, words, sorted_letter_count)

main()