def highest_value(dic):
    max_key = max(dic,key=dic.get)
    return max_key

dict1 = {'apple':2,'banana':3,'organe':1}
print(highest_value(dict1))
