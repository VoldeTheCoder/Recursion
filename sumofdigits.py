def sum_of_digits(num):
    if num == 0:
        return 0
    new_num = num//10
    digit = num%10
    return digit + sum_of_digits(new_num)

print(sum_of_digits(532456))