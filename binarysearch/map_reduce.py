'''
Created on Dec 25, 2017

@author: qiankunhuang
'''
###map-reduce1
a=["apple","b","c","d","sx","sd","das","sd","sx","bc","a","apple","apple"]

def count_map(a):
    lst=[]
    for i in a:
        dict={}
        dict[i]=1
        lst.append((dict)) 
    return lst

def reduce(a):
    dict = {}
    for i in a:
        if i.keys()[0] not in dict:
            dict[i.keys()[0]] = 1
        else:
            dict[i.keys()[0]] += 1
    return dict

def count_map2(a):
    lst =[]
    for i in a:
        lst.append([i,1])
    return sorted(lst)

def reduce2(a):
    lst = []
    s=set()
    for j in a:
        if j[0] not in s:
            s.add(j[0])
            lst.append((j[0],a.count(j))) 
        else:
            continue
    return lst
print(reduce2(count_map2(a)))

###map-reduce2
import heapq
def map2(a,k):
    h =[]
    for i in a:
        heapq.heappush(h,(i[1],i[0]))
        if len(h) > k:
            heapq.heappop(h)
    return help(h)


def help(h):
    lst=[]
    for i in h:
        lst.append((1,i))
    lst.reverse()
    return lst

print(map2(reduce2(count_map2(a)),2))
a =reduce2(count_map2(a))

a=[ [(3, 'apple'), (2, 'sx')],[(5, 'apple'), (4, 'sx')],[(6,'apple'), (7, 'sx')]]

def reduce3(a,k):
    h=a[0]
    heapq.heapify(h)
    for j in xrange(1,len(a),1):
        for i in a[j]:
            if i[0] > h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h,(i[0],i[1]))
    return h


    
        
        
        
        
        
    
        
    



            
        
        
        
        
        



        
        
            