'''
Created on Jan 21, 2018

@author: qiankunhuang
'''
def url_100000():
    num = 0.95*100000
    total = 0
    for i in xrange(4100):
        total += buckt[i]
        if total >= num :
            print i
            break
        
    
    