# """
#
# This is to practice string data types
# """
#
# str='ETL Automation Testing'
#
# # this will count the occurance of character
#
# print("E is repated :" ,str.count('E'))
#
# print("E is repated :" ,str.count('e'))
#
# #Searches the string for a specified value and returns the position of where it was found
#
# print("postition of e is :",str.find('e',))
#
# #Converts the elements of an iterable into a string
# key_cols=('name','age','gender')
# cols=",".join(key_cols)
# print(cols)
# query=f" select {cols},count(*) from table group by {cols} having count(*)>1;"
# print(query)
#
# #Searches the string for a specified value and returns the position of where it was found
# print(str.index("e"))
#
# print ( " output in lower case  ",str.lower())
#
# print ("first letter capital:",str.capitalize())
#
# print("output in lower case ",str.casefold())
#
#
# print(str.center(150))
#
# print(str.encode())
#
# #every first char of string will be capital
# print(str.title())
#
# #check if it ends with given arg and return true or false
# print(str.endswith('Testing'))
#
# print(str.zfill(2))
#
#
# #it will fill with 0 values n times before given string as 000000040
# txt="40"
#
# print(txt.zfill(9))
#
# #['ETL', 'Automation', 'Testing']
#
# print(str.split())
#
# print(str.expandtabs(6))


st='Testing 1'

print("it is alphanumri ",st.isalnum())


