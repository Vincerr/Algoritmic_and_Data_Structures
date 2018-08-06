import time
import random

def fast_max(a):
    n = len(a)


    index1=1
    index2=1
    result=0

    for i in range (2,n):
        if a[i]>=a[index1]:
            index2=index1
            index1=i

    result=a[index1]*a[index2]

    return result

a=[]

'''a=[int(x) for x in input().split()]'''

for m in range (0,3):
    a.append(random.randint(0,100))

time_flag1=time.clock()
print(a)
n=len(a)
result1=0

for i in range (0, n):
    for j in range (i+1,n):
        if  a[i]*a[j]>result1:
            result1=a[i]*a[j]

print(result1)

print("time1 %f" % (time.clock()-time_flag1))
time_flag2=time.clock()
result2=fast_max(a)
print(result2)
print("time2 %f" % (time.clock()-time_flag2))

if result1!=result2:
    print("Resultados incorrectos")
