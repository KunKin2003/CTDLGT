def reverse_key_value(my_dict):
    my_dict = {value:key for key, value in my_dict.items()}
    return my_dict

dict1 = {'apple':2,'banana':3,'organe':1}
print(reverse_key_value(dict1))