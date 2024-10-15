#TO ENTER THE DATA INTO A LIST
#1
# l = []
# n = int(input('Enter the number of element:'))
# for i in range(n):
#     l.append(int(input('Enter the data:')))
# print(l)

#2
# n = int(input()) #5
# l = list(map(int,input().split()))[:n]  #11 12 13 14 15 16
# print(n)  #5
# print(l)  # [11, 12, 13, 14, 15]

#3
# n = int(input()) #5
# l = list(map(int,input().split('$')))[:n]  #11$12$13$14$15$16
# print(n)  #5
# print(l)  # [11, 12, 13, 14, 15]

#4
# s = 'Vowtech'
# l = list(s)
# print(l) #['V', 'o', 'w', 't', 'e', 'c', 'h']

#5
# s = 'Vowch'
# l = []
# for v in s:
#     l.append(v)
# print(l) #['V', 'o', 'w', 'c', 'h']

#6
# s = 'Vowtech'
# l = [ v for v in s]
# print(l)  #['V', 'o', 'w', 't', 'e', 'c', 'h']

#7
# s = 'Vow1T3e7ch'
# l = [ v for v in s if (ord(v)>=65 and ord(v)<=90) or (ord(v)>=97 and ord(v)<=122)]
# print(l)

#8
#if there any special chr in string
# s = 'Vow1T3e7ch$%&'
# let = [chr(v) for v in range(65,91)]  # A to Z
# let.extend([chr(v) for v in range(97,123)]) # A to Z and a to z
# print(let)
# l = [v for v in s if v in let ]
# print(l) #['V', 'o', 'w', 'T', 'e', 'c', 'h']

# letters = [v for v in range(10)]
# print(letters) #0  t0 9 in list

# letters = [v for v in range(10) if v%2 == 0]
# print(letters) #[0, 2, 4, 6, 8]

#to get squares for
# letters = [x**2 for x in range(11)]
# print(letters) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# obj = ['Even' if v%2 == 0 else 'Odd' for v in range(10)]
# print(obj) #['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']


#### Transpose of matrix #########
# transposed= []
# matrix = [[1,2,3,4],[5,6,7,8]]
# l1 = []
# for v in matrix:
#     for i in v:
#         l1.append(i)
# print(l1)
#
# o1 =[]
# k = 0
# for i in range(4):
#     o = []
#     for j  in range(2):
#         o.append(l1[k])
#         k+=1
#     o1.append(o)
# print(o1)


# transposed= []
# matrix = [[1,2,3,4],[5,6,7,8]]
#
# for i in range(len(matrix[0])):
#     trans = []
#     # i =0 1 2 3
#     for mat in matrix:
#         trans.append(mat[i])
#     transposed.append(trans)
# print(transposed)


# matrix = [[1,2,3,4],[5,6,7,8]]
# transposed= [[mat[i] for mat in matrix ] for i in range(len(matrix[0]))]
# print(transposed)
#
#
# m = [[1,2,3,4],[5,6,7,8]]
# t = [[j[i] for j in m] for i in range(4)]
# print(t)

# f =open('log.txt')
# l = []
# for line in f:
#     if line.split()[3] != 'NA':
#         l.append(int(line.split()[3]))
# print(l)
# print(sum(l))
#
# f = open('log.txt')
# price = [ int(line.split()[3]) for line in f if line.split()[3] != 'NA']
# print(price)
# print(sum(price))




# l = []
# n = int(input('Enter the element:'))
# for i in range(n):
#     l.append(int(input('Enter the data:')))
# print(l)

# n = int(input())
# l = list(map(int,input().split()))[:n]
# print(l)

# s = 'Vowtech'
# l = [v for v in s]
# print(l)

# s = 'Vowte1c3h'
# l = [v for v in s if (ord(v)> 65 and ord(v)<90) or (ord(v)> 97 and ord(v)< 122)  ]
# print(l)

# s = 'Vow1T3e7ch$%&'
# let = [chr(v) for v in range(65,91)]  # A to Z
# let.extend([chr(v) for v in range(97,123)]) # A to Z and a to z
# print(let)
# l = [v for v in s if v in let]
# print(l)

# letters = [x for x in range(1,21) if x%2==0]
# print(letters)

# l = [ 'even' if x%2 == 0 else 'odd' for x in range(1,21)]
# print(l)

# transposed = []
# matrix =[[1,2,3,4],[5,6,7,8]]
# #
# for i in range(len(matrix[0])):
#     trans=[]
#     for mat in matrix:
#         trans.append(mat[i])
#     transposed.append(trans)
# print(transposed)
#
# transposed = [ [mat[i] for mat in matrix] for i in range(len(matrix[0]))]
# print(transposed)


# f = open('log.txt','r')
# price = []
# for line in f:
#     print(line.split()[3])
#     if line.split()[3] != 'NA':
#         price.append(int(line.split()[3]))
# print(f'Total bill amount : {sum(price)}')
#
# f = open('log.txt','r')
# price = [int(line.split()[3]) for line in f if line.split()[3] != 'NA']
# print(f'Total bill amount : {sum(price)}')
