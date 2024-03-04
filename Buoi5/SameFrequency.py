list1 = [1, 3, 3, 2, 1]
list2 = [3, 1 ,2 ,1 ,3]

def count_word_frequency(words):
    my_dict = {}
    for i in words:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict

def check_same_frequency(list1, list2):
    if len(list1) != len(list2):
        return False
    dict1 = count_word_frequency(list1)
    dict2 = count_word_frequency(list2)
    return dict1 == dict2

print(check_same_frequency(list1,list2))

        