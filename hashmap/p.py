'''
Created on Dec 13, 2017

@author: qiankunhuang
'''
def longest(input):
      if not input or len(input) == 0:
        return 0
      n = len(input)
      Max  = 0
      for i in range(0,n,1):  
        a = set()  
        for j in range(i,n,1):
          if input[j] not in a:
            a.add(input[j])
          else:
            Max =max(Max,len(a))
            break
      return Max
print longest('abcabcbbcda')
             
   
        

            
    
    
                  
            
                    
            
            
            


        
    
        
      
    
            
        
            
    