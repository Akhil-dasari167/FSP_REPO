# my_list = [1,2,3,4,5]
# list1= ['a','k','h','i','l']
# list2 = [1, 'a', 3.14, True]
# list3 = list([1,2,3,4,5,6,7])
# print(list3)
# list4 = list(range(1,11))
# print(list4)
# print(list(range(10,1,-1)))
#l1 = ['akhilsai.com']
#l2 = ['akhil']
# l3 =l1+l2
# l1 = [' akhilsai.com ']
# l2 = [' akhil ']
# 
# l3 = [x.strip() for x in l1 + l2]
# 
# print(l3)
# 
# l3 =[x.strip() for x in l1+l2]
# print(l3)
# l4 = [x.strip() for x in l3 +l1+l3]
# print(f"l4 = {l4}")
# print(l4[:3])
# print(l3*3)
# z= [x for x in range(1000, 1500, 1)]
# ls=[]
# for i in z:
    # if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        # ls.append(i)
# print(ls)
# 
# membership (in and not in)
# a=[1,2,3,4,5]
# print(3 in a)

# names= ['akhil', 'sai',' akki']
# names.remove(' akki')
# print(names)
# names.append('akki')
# names.insert(1,' bunty')
# names[0]='akhilsai'
# names.pop()
# names.pop(len(names)-1)
# print(len(names))


alpha = [chr(i) for i in range(97, 123)]

st='akhil'
for i in st:
    if i in alpha:
        print(alpha.index(i))
        
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
second_fruit = fruits.copy()
print(second_fruit)
del fruits[0]
print(fruits)   master 