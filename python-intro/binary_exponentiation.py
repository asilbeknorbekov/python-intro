"""POW REC AND ITER"""

def pow_(a,b):
    if b==1:
        return a
    if b==0:
        return 1
    res=pow_(a,b//2)
    if b%2==0:
        return res*res
    else:
        return a*res*res

print(pow_(10,7))


def pow_iterative(a,b):
    res=1
    while b>0:
        if b%2==1:
            res*=a
        a*=a
        b=b//2
    return res
print(pow_iterative(10,7))
