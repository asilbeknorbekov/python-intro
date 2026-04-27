def whilefoc():
  import time
  a=time.time()
  x=5
  i=1
  factorial=1
  while i<=x:
    factorial*=i
    i+=1
  print(f'{x}! is equal to {factorial}')
  b=time.time()
  print("Time:",b-a)
  return b-a
def forloopfoc():
     import time
     a=time.time()
     x=5
     factorial=1
     for i in  range(1,x+1):
      factorial*=i
     print(f'{x}! is equal to {factorial}')
     b=time.time()
     print("Time:",b-a)
     return b-a
print("while")
b=whilefoc()
print("for loop")
a=forloopfoc()
print("which is faster?")
if a>b:
    print("While loop")
else:
    print("for loop")

