myString=input("Enter a string:\n")
'''
slicing
'''
print("this is the result using slicing:", myString[::-1])
'''
loop
'''
string1=""
length=len(myString)
index=length-1
while index>=0:
    string1= string1 +myString[index]
    index=index-1
print("this is the result using loop:", string1)