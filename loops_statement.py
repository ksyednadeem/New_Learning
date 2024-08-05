ls=[1,2] # square each item

print(ls)

ls[0]=ls[0]*ls[0]
ls[1]=ls[1]*ls[1]
print(ls)

############################3333

ls=[1,2,3,4,5,6,7,8,9]
ls2 = []
for i in ls :
    print(i*i)
#print(f'square of {i} item is ', i*i)
ls2.append(i*i)
print(ls2)