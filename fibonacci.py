a=0
b=1
n=int(input("enter the fibonacci number to be generated"))
if n<=0:
 print("not possible")
elif n==1:
 print(a)
elif n>=2:
 print(a)
 print(b)
  for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)
