numbers=[1,2,3,2,0,65,21,4,2,10]
new=[]
srch=int(input("enter the search element"))
for i,value in enumerate(numbers):
	if value is 2:
		new.append(i)

print(new)
