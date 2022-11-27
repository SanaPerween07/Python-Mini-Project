# PYTHON PROJECT 

user_input=map(int,input().split("and"))
c=0
a=1
b=1
for i in user_input:
    if i==0 or i==1:
        print(f"{i} is Valid")
    else:
        while c<i:
            c=a+b
            b=a
            a=c
        if c==i:
            print(f"{i} is Valid")
        else:
            print(f"{i} is Invalid")
