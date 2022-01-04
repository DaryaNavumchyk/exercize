#def fibonacci(n):
#    a, b = 1, 1
#    for i in range(n):
#        yield a
#        a, b = b, a + b
#data = list(fibonacci(100))
#print(data)



fibonacci1 = fibonacci2 = 1
print(fibonacci1, fibonacci2, end=' ')
 
for i in range(100):
    fibonacci1, fibonacci2 = fibonacci2, fibonacci1 + fibonacci2
    print(fibonacci2, end=' ')
 