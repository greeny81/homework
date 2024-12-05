def single_root_words(root_word, *other_words):
    same_words = []
    low_str = root_word.lower()
    low_list = [s.lower() for s in other_words]
    for list_value in low_list:
        #print(list_value)
        if low_str in list_value:
            same_words.append(list_value)
        if list_value in low_str:
            same_words.append(list_value)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)