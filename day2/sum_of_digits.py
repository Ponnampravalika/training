num=int(input())
count=0
while num!=0:
    n=num%10
    count+=n
    num=num//10
print(count)
