# Transpose of a matrix
# n,m = map(int,input().split())
# matrix = []
# print("Enter the matrix:")
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)
# print("Transpose of the matrix:")
# for j in range(matrix[0]):
#     for i in range(len(matrix)):
#         print(matrix[i][j], end=" ")
#     print()
#--------------------------------------------------
# Print each vowel in the string "education".
# for ch in 'education':
    # if ch in 'aeiou':
        # print()
#--------------------------------------------------
#print vowels in string with index value
# for i in range(len('education')):
    # if 'education'[i] in 'aeiou':
        # print(f"Vowel: { 'education'[i] }, Index: {i}")
# 
#-------------------------------------------------------------
#Count the number of vowels in the string "hello world".
# count=0
# for i, ch in enumerate('Akhil'):
    # if ch in 'aeiouAEIOU':
        # count+=1
        # print(f"Vowel: {ch.lower()}, Index: {i}")
    # 
#-------------------------------------------------------
#Reverse the string "python" using a for loop.
#for i in range(len('python')-1, -1, -1):
#    print('python'[i], end="")
#-------------------------------------------------------
#Find the frequency of each character in the string "apple".
# freq = {}
# s = "apple"
# freq = {}
# 
# for ch in s:
    # if ch in freq:
        # freq[ch] += 1
    # else:
        # freq[ch] = 1
# 
# print(freq)
#-------------------------------------------------------
#Write a program that computes the factorial of a given positive integer using a for loop.
# n=6
# fact = 1
# for i in range(n,0,-1):
    # fact*=i
# print(f"The factorial of {n} is: {fact}")
#-------------------------------------------------------
# n=6
# fact = 1
# for i in range(1,n+1):
    # fact*=i
# print(f"The factorial of {n} is : {fact}")
#---------------------------------------------------------
#String Reversal
# s= 'Levelupedu.com'
# res_s =''
# for i in range(len(s)-1,-1,-1):
    # res_s+=s[i]
# print(f"The reverse of the string {s} is: {res_s.upper()}")
# #---------------------------------------------------------
# print('eloHssa'[::-1])
#---------------------------------------------------------
#Multiplication Table Generator
# n=5
# print(f"Multiplication Table for {n}:")
# for i in range(1,11,1):
    # for j in range(1,n+1):
        # print(f"{j} x {i} = {j*i}", end="\t")
    # print()
#----------------------------------------------------------
# Print a pattern of alternating `0` and `1`:
    # ```
    # 0 1 0 1
    # 1 0 1 0
    # 0 1 0 1
    # 1 0 1 0
    # ```
    
# for i in range(3):
    # for j in range(4):
        # print((i+j)%2 , end=" ")
    # print()
    
#----------------------------------------------------------
# for i in range(4):
    # for j in range(4):
        # if i%2==0:
            # if j%2==0:
                # print(0,end= " ")
            # else:
                # print(1,end=" ")
        # else:
            # if j%2==0:
                # print(1,end=" ")
            # else:
                # print(0,end=" ")
    # print()
# -----------------------------------------------------------
# lst = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[1,2,3,4]]
# for i in range(len(lst)):
    # for j in range(len(lst)):
        # print(lst[i][j], end=" ")
    # print()
