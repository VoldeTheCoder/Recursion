""" def ten_base(num, count):
    num = num//10
    if num ==0:
        return count
    count+=1
    return ten_base(num, count)
     """     

def reverse_num(num, s):
    if num==0:
        return s
    s = s*10 + num%10
    return reverse_num(num//10, s)
    
    #return ((num%10)*(10**ten_base(num, 0))) + reverse_num(num//10)


print(reverse_num(123456789, 0))
     