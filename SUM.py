# Python Program to Find Sum of Array

from array import *
a=array('i',[1,2,3,4,5])
sum=0
for i in a:
    sum=sum+i
print("sum of array is",sum)

#  2nd approach

from array import *
def sumarr(a):
    sum=0
    for i in a:
        sum=sum+i
a=array('i',[1,2,3,4,5])
print("sum of array is",sum)
