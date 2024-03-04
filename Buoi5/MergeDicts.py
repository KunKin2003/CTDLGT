def merge_dicts(dict1,dict2):
    dict3 = dict2.copy()
    for element in dict1:
        if element in dict2:
            dict3[element] += 1
        else:
            dict3[element] = dict1[element]
    return dict3

dict1 = {'apple':2,'banana':2,'organe':1}
dict2 = {'apple':3,'banana':1}

print(merge_dicts(dict1,dict2))
print(dict2)