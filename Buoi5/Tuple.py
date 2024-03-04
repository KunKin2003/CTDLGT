#Create tuple
new_tuple_1 = ('a','b','c')
new_tuple_2 = tuple('abc')
print(new_tuple_1)
print(new_tuple_2)
print('------------------------------------')
#Access tuple
print(new_tuple_1[2])
print('------------------------------------')
#Slice tuple
print(new_tuple_2[1:3])
print('------------------------------------')
#Traverse through Tuple
for i in new_tuple_2:
    print(i)
print('------------------------------------')
#Search element in Tuple
print('b' in new_tuple_2)
print(new_tuple_1.index('c'))
print('------------------------------------')
#Tuple Operations / Functions
print(new_tuple_1 + new_tuple_2)
print(new_tuple_1*4)
print(new_tuple_1.count('b'))
print('------------------------------------')




