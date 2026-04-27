import sys
sys.setrecursionlimit(200000)
n=int(input())
F=[-1]*(n+1)
F[0]=0
mod=(10**9 + 7)
def fib(n):
    if F[n]>=0:
        return F[n]
    else:
        F[n]=(fib(n-1) + fib(n-2))%mod
        return F[n]

n=int(input())
if n>=1:
   print(fib(n))
