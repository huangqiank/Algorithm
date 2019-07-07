'''
Created on Jan 21, 2018

@author: qiankunhuang
'''
def random25():
    return random(5) + 5*(random(5))

def random7():
    num= random25()
    while num>20:
        num = random25()
    return num%7

def random72():
    num= random25()
    while num>6:
        num = random25()
    return num%7

def random125():
    return 25*random(5)+5*random(5)+random(5)

def random1000000():
    cur_max = 1
    num=random(2)
    while cur_max <=1000000 or num > 1000000:
        if num > 10000000:
            num = random(2)
            cur_max = 1
        else:
            cur_max = 2*cur_max+1
            num =num*2+random(2)
    return num
            
        
    

    