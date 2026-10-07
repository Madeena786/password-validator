password = input("Enter password: ")
u=0
l=0
d=0
s=0
sp="!@#$_"
n=len(password)
for i in password:
    if i.isupper():
        u=u+1
    if i.islower():
        l=l+1
    if i.isdigit():
        d=d+1
    if i in sp:
        s=s+1
if n>=8 and u>0 and l>0 and n>0 and s>0:
    print("Password is valid")
else:
    print("Password is invalid")
