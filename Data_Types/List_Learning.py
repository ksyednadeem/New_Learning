"""
This is for list learning
"""
ls = [1, 2, 3]
# print("type of ls is ",type(ls[0]))
# print("meory of ls is :",id(ls[0]))
# ls1=[1,2,3]
# print("type of ls is ",type(ls1[0]))
# print("meory of ls is :",id(ls1[0]))
#
#
# print('methods available in ls',dir(ls))

#if no index specify it will remove last value .
# print(ls.pop(0))
# print(ls)
#to copy values from one variable to another
# ls3=ls.copy()
# print("ls3 values are ",ls3)

# reverse the list of elements
# ls_R = [1, 2, 3]
# ls_R.reverse()
# print(ls_R)

# fruits = ['apple', 'banana', 'cherry']
#
# fruits.reverse()
#
# print(fruits)

#append will add values at the end
ls4 = [1, 2, 3, 4]
# # ls4.append(6)
# # print(ls4)
#it will allow to add multiple values
# ls4.extend([3, 6, 5])
# print(ls4)
# ls4.extend('ETL',)
# print(ls4)

# #it will allow to add values at desired location
# ls4.insert(0,'Automation')
# print(ls4)

# ls4[1]=21
# print(ls4)
#
# ls4.pop(1)
# print(ls4)


ls4.append('ETL')
print(ls4)
ls4.remove(1)
print(ls4)
ls4.extend([1, 2, 3, 4, 5, 5, 5, 6, 2, 3 ])
#ls4.clear()
print(ls4)

ls5=list(set(ls4))
print(ls5)
ls5.remove(3)
print(ls5)
