tuple1 =(1,2,3,4,5)
tuple2 =(4,5,6,7,8)

def common_elements(tuple1, tuple2):
    new_tuple = ()
    for element in tuple1:
        if element in tuple2:
            new_tuple += (element,)
    return new_tuple

out_tuple = common_elements(tuple1, tuple2)
print(out_tuple)