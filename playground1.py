"""Playground 1: splitting"""
string = "hi,h,ho,wfr,ersg,bs,df,se,frsefd"

a = string.split(',')
print(a)
for item in a:
    print(item, end=",")
print("\n" + string)
