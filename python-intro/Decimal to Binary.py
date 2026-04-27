#binary
a=int(input())
result=""
if a==0:
    print(0)
else:
    while a>0:
        result=str(a%2)+result
        a=a//2
    print(result)
