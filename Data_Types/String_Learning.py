# # """
# #
# # This is to practice string data types
# # """
# #
# str='ETL Automation Testing'
# #
# # # this will count the occurance of character
# #
# # print("E is repated :" ,str.count('E'))
# #
# # print("E is repated :" ,str.count('e'))
# #
# # #Searches the string for a specified value and returns the position of where it was found
# #
# # print("postition of e is :",str.find('e',))
# #
# # #Converts the elements of an iterable into a string
# # key_cols=('name','age','gender')
# # cols=",".join(key_cols)
# # print(cols)
# # query=f" select {cols},count(*) from table group by {cols} having count(*)>1;"
# # print(query)
# #
# # #Searches the string for a specified value and returns the position of where it was found
# # print(str.index("e"))
# #
# # print ( " output in lower case  ",str.lower())
# #
# # print ("first letter capital:",str.capitalize())
# #
# # print("output in lower case ",str.casefold())
# #
# #
# # print(str.center(150))
# #
# # print(str.encode())
# #
# # #every first char of string will be capital
# # print(str.title())
# #
# # #check if it ends with given arg and return true or false
# # print(str.endswith('Testing'))
# #
# # print(str.zfill(2))
# #
# #
# # #it will fill with 0 values n times before given string as 000000040
# # txt="40"
# #
# # print(txt.zfill(9))
# #
# # #['ETL', 'Automation', 'Testing']
#
# #print(str.expandtabs(6))
# # txt = "welcome to the jungle"
# # # split
# # x = txt.split()
# # print(x)
# #
# #
# st=' Testing 1'
# #
# # print("it is alphanumri ",st.isalnum())
#
# print(st.isascii())
# print("is demical",st.isdecimal())
# print(st.lstrip())
# print(st.rstrip())
# print(" it will trim spaces",st.strip())
# print("it will replace char",st.replace('e','a'))
# print("it will swap cases from small to big",st.swapcase())
# print("first char of each word will caps ",str.title())

# count=10
# print("type of count is:",type(count) )
# print("memoery address of count is :",dir(count))
# str="ETL AUTOMATION TESTING"
# print(str.find('TEST'))

#
# name = 'nadeem'
# age = 36
#
# print(f'my name is {name} and age is {age}')


# str='syed nadeem'
# print(len(str))

str = "ETL AUTOMATION TESTING"
# print (str[0:6])
# print(str[6])
# print(str[4:])
# print(str[:])
# print(str[:5])

# Email='syednadeem311@gmail.com'
#
#
# print(f'username from {Email} is :',Email[0:Email.find('@')])
# print(f'domain name from {Email} is :',Email[Email.find('@')+1:])
# print(f'find only .com from {Email}:',Email[Email.find("."):])
# print(str[::1])
# print(str[::2])
# print(str[::4])
#
# columns='col1,col2,col3'
# print(columns.split())

# print(str)
# # #if step is postive then go frim left to right and if step is postive then end is end-1
# print(str[-12:-7:1])
# #if step values is negative then go from right to left and end is end +1
# print(str[-12:-13:-1])

num= 121
# print('t',type(num))
# rev_num=num[::-1]
if str(num)==str(num)[::-1]:
    print('It is pallindrome')
else:
    print('it is not pallindrome')



