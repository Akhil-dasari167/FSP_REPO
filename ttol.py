#list to tuple
a=[1,2,3,4]
print(tuple(a))
#tup=list(map(int,input('Enter tuple list').split()))
# lis =list(map(int,input("Enter list Data").split()))
listt = ((1,2),3,4)
#print(f"list to tuple {tuple(tuple(i) for i in listt)}")

#nested list to nested tuple
a= [[1,2],[3,4]]
b=tuple(tuple(row) for row in a)
c = (*a,)

print(b)
print(c)