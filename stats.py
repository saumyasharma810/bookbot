def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    return None

def get_num_words(file_path):
    text = get_book_text(file_path=file_path)
    words = text.split()
    return len(words)

def get_char_count(file_path):
    text = get_book_text(file_path=file_path)
    words = text.split()
    char_dict = {}
    for word in words:
        word_l = word.lower()
        for char in word_l:
            if char in char_dict:
                char_dict[char]+=1
            else:
                char_dict[char] = 1
    return char_dict


def sort_on(items):
    return items["num"]

def get_sorted_chars(file_path):
    char_dict = get_char_count(file_path)
    new_char_list = []
    for key in char_dict.keys():
        new_char_list.append({"char":key, "num":char_dict[key]})
    return sorted(new_char_list, key=sort_on, reverse=True)
