tuple1 = (1,2,3)
tuple2 = (4,8,6)

def tuple_elementwise_sum(tuple1,tuple2):
    temp = list(tuple1)
    i = 0
    for element in tuple2:
        temp[i] += element
        i += 1
    return tuple(temp)

print(tuple_elementwise_sum(tuple1,tuple2))