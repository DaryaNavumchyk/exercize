a = ["abc", "def"]

def r(a):
     b=[]     
     for string in a[::-1]:
          c=[]               
          for i in string[::-1]:               
               c.append(i)                       
          b.append("".join(c))                    
     return b      
print(r(a))