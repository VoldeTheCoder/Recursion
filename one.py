#printing 5 numbers from beginning using recursion

def num_upto(num):
    if num>0:
        print(num_upto(num-1) + 1)
        return num
    else:
        return 1

num_upto(10)