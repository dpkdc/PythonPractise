def sum_of_n_numbers(num):

    if num==0:
        return 0
    return sum_of_n_numbers(num-1)+num

print(sum_of_n_numbers(5))

