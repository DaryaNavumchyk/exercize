list = [1, 2, 3, 4, 5, 6, 7]

#list.reverse()
#print(list)

#for x in reversed(list): 
#    print(x)

#list_r=list[::-1]
#print(list_r)


 
def h(liss):
    for i in range(len(liss)-1, -1, -1):
        list_f.append(liss[i])
    return list_f     

print(h(liss))
