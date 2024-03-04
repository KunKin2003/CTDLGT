input_tuple = (1,2,3,4)

def sum_product(tup):
    sum = 0
    product = 1
    for element in tup:
        sum += element
        product *= element
    return sum, product

sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)