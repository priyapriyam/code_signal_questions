list = [50,60,60,45,70]
a=0
sum=0
sum1=0
new_list=[]
while a < len(list):
    if a % 2 == 0:
        sum=sum+list[a]
    elif a %2!= 0:
        sum1=sum1+list[a]
    a=a+1
new_list.append(sum)
new_list.append (sum1)
print new_list
     