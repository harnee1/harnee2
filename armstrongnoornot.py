n=int(input())
sum=0
num=n
while n>0:
	r=n%10
	sum=sum+(r**3)
	n=n//10
if sum==num:
 print("yes it is an armstrong no")
else:
 print("no it is not an armstrong no")
