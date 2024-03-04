my_dict = {'a':1,'b':2,'c':3,'d':4}

def filter_dict(dic,con):
    return {k:v for k,v in dic.items() if con(k,v)}
        
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
print(filtered_dict)
