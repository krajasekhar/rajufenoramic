import time
import math
start_time = time.time()
def power(x,n,d):
    if d==1:
        return 0
    if x==0:
        return 0
    if n==0:
        return 1
    #Decreasing n value by increasing x value
    while n%7==0:
        x=x*x*x*x*x*x*x
        n=n/7
    while n%11==0:
        x=x*x*x*x*x*x*x*x*x*x*x
        n=n/11
    sepVar=0
    sepVal=1
    while sepVar <=2 and n>sepVar:
        while n%2==0:
            x=x*x
            n=n/2
        while n%3==0:
            x=x*x*x
            n=n/3
        while n%5==0:
            x=x*x*x*x*x
            n=n/5
        sepVar=sepVar+1
        sepVal=sepVal*x
        n=n-1

    # print(x,n,d,sepVar)
    i=1
    prod=1
    while i<=n:
        prod=(prod*x)%d
        # print(prod)
        i=i+1
    prod=prod*sepVal
    prod=prod-d*(int(prod/d))
    return prod



# x = int(raw_input())
# n = int(raw_input())
# d = int(raw_input())
x = 71045970
n = 41535484
d = 64735492
print(power(x,n,d))
# print((time.time() - start_time))