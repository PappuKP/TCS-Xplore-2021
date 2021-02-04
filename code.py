if __name__ == "__main__":

	t1=[]
	t2=[]
	t3=[]
	l1=[]

	for i in range(3):
		x=input()
		t1.append(x)
		l1.append(x)

	for i in range(3):
		x=input()
		t2.append(x)
		l1.append(x)

	for i in range(3):
		x=input()
		t3.append(x)
		l1.append(x)

	result1=list(set(l1))
	result1.sort()
	
	t1=set(t1)
	t2=set(t2)
	t3=set(t3)
	if(t1 & t2 & t3):
		result2=t1 & t2 & t3

	for i in result1:
		print(i)
	for j in result2:
		print(j)