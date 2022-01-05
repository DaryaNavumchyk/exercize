#def fibonacci(n):
#    a, b = 1, 1
#    for i in range(n):
#        yield a
#        a, b = b, a + b
#data = list(fibonacci(100))
#print(data)



#fibonacci1 = fibonacci2 = 1
#print(fibonacci1, fibonacci2, end=' ')
 
#for i in range(100):
#    fibonacci1, fibonacci2 = fibonacci2, fibonacci1 + fibonacci2
#    print(fibonacci2, end=' ')
 
 
# def fibonacci(n):
     
#    if (n <= 1):
#        return n
#    else:
#        return (fibonacci(n-1) + fibonacci(n-2))

#for i in range(100):
#    print(fibonacci(i))

  
  def fibonacci(n):
    
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


for i in range(10):
    print(fibonacci(i))
