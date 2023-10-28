def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = chars_dict_to_sorted_list(chars_dict)
    build_report(book_path, num_words, chars_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(e):
    return e[1]

def chars_dict_to_sorted_list(chars_dict):
    chars_list = list(chars_dict.items())
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def build_report(book_path, num_words, chars_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for char in chars_list:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {char[1]} times")
    print("--- End report ---")

main()
