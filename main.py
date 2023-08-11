#print("hello world")
#note to self: need to use "python3 filename.py"
#instead of just "python filename.py"
#in order to run python files from console

#with open("books/frankenstein.txt") as f:
#    file_contents = f.read()
#    words = file_contents.split()
#    print(len(words))
#    words = [word.lower() for word in words]
#    string = "".join(words)
#    alphabet = list(map(chr, range(ord('a'),ord('z')+1)))
#
#    dict = {}
#
#    for letter in alphabet:
#        dict[letter] = string.count(letter)
#    print(dict)


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sort_report = get_sorted_report(chars_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for item in sort_report:
        if not item["char"].isalpha():
            continue
        print(f"the '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def get_sorted_report(num_dict):
    sorted_dict = []
    for ch in num_dict:
        sorted_dict.append({"char": ch, "num": num_dict[ch]})
    sorted_dict.sort(reverse = True, key=sort_on)
    return sorted_dict
    


main()