#printing numbers in back and forth order

def num_upto(num):
    if num == 1:
        print(num)
    else:
        print(num)
        num_upto(num-1)
        print(num)

num_upto(5)