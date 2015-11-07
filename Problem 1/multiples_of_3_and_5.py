def sum_m(n, end):
    return sum(x for x in range(n, end, n))

def multiples_of_3_and_5(end):
    return sum_m(3, end) + sum_m(5, end) - sum_m(15, end)


print(multiples_of_3_and_5(10))
print(multiples_of_3_and_5(1000))
