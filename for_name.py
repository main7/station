# -*- unicode:utf-8 -*-
names=['Tom','Tim','Bob']
for name in names:
    print(name)

#list
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)

#range(i)生成一个小于i的整数序列
sum=0
for x in list(range(101)):
    sum+=x
print(sum)



sum=0
n=99
while n>0:
    sum+=n
    n-=2
print(sum)

n=1
while n<=100:
    print(n)
    n+=1
print('END')


n=1
while n<=100:
    if n>10:
        break
    print(n)
    n+=1
print('END')


n=1
while n<=100:
    if n>10:
        continue
    print(n)
    n+=1
print('END')
