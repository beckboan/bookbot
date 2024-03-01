def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    lowered_text = text.lower()
    char_dict = {}
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


def sort_param(dict):
    return dict["num"]


def sort_dict_key(input_dict):
    sorted_list = []
    for char in input_dict:
        sorted_list.append({"char": char, "num": input_dict[char]})
    sorted_list.sort(reverse=True, key=sort_param)
    return sorted_list


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_dict = count_characters(text)
    char_list = sort_dict_key(char_dict)
    print(f"Word report of {book_path}")
    print(f"{word_count} were found in the document")
    print()

    for e in char_list:
        if not e["char"].isalpha():
            continue
        print(f"Character '{e['char']}' was found {e['num']} times")


main()
