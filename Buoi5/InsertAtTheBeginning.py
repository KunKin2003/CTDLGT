input_tuple = (2,3,4)
value_to_insert = 1

def insert_value_font(tup,value):
    temp_list = [element for element in tup]
    temp_list.insert(0,value)
    return tuple(temp_list)

print(insert_value_font(input_tuple,value_to_insert))