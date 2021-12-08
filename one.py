#printing 5 numbers from beginning using recursion


def num_upto(num, switch):
    if num == 1:
        print(num)
        switch = 1
        num_upto(num+1, switch)
    elif num == 4 and switch == 1:
        print(num)
    else:
        print(num)
        if switch == 0:
            num_upto(num-1, switch)
        else:
            num_upto(num+1, switch)

num_upto(4, 0)