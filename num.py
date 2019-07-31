def maxi(x):
	sum=0
	for i in range(n):
		k=max(x)
		sum=sum*10 + k
		x.remove(k)
	return sum
n=int(input())
l=list(map(int,input().split()))
print(maxi(l))
