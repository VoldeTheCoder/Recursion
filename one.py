#printing 5 numbers using recursion

def num_upto(num):
    if num>0:
        print(num)
        return num_upto(num-1)

num_upto(10)