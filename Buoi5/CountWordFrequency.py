def count_word_frequency(words):
    my_dict = {}
    for i in words:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict

words = ['apple','organe','banna','apple','banna']
print(count_word_frequency(words))