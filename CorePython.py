# t = (101,'ritu',56,5.3,'dy patil','be','comp',(45,'div',12.2))
# print(t)
# print( len(t) )
# print( t[0],type(t[0]) )
# print( t[1],type(t[1]) )
# print( t[2],type(t[2]) )
# print( t[3],type(t[3]) )
# print( t[4],type(t[4]) )
# print( t[7],type(t[7]) )

# t = (101,'ritu',56,5.3,'dy patil','be','comp',(45,'div',12.2))
# for i in range(len(t)):
#     print(t[i])

# t = (101,'Ritu',56,5.3,'Dy Patil','BE','Comp',(45,'Div-A',12.2))
# for value in t:
#     print(value)

#shortcut to get above
# t = ((0,101),(1,'ritu'),(2,56),(3,5.3),(4,'dy patil'),(5,'be'),(6,'comp'),(7,(45,'div',12.2)))
#
# for i in range(0,8):
#     print(t[i],type(t[i]))

# t = ((0,101),(1,'ritu'),(2,56),(3,5.3),(4,'dy patil'),(5,'be'),(6,'comp'),(7,(45,'div',12.2)))
# for value in t:# (0,101)
#     print(value,type(t))

# t = ((0,101),(1,'ritu'),(2,56),(3,5.3),(4,'dy patil'),(5,'be'),(6,'comp'),(7,(45,'div',12.2)))
# for key,value in t:
#     print(key,value)

# for key,value in t:
#     # print(f'key = {key},value = {value}')
#     print('{},{}' .format(value,key))


# #alternate to key,value seperate is enumerate the original tuple
# t = (101,'ritu',56,5.3,'dy patil','be','comp',(45,'div',12.2))
#
# # enumerate(t) convert tuple to tuple in tuple index & value pair
# # t = ((0,101),(1,'ritu'),(2,56),(4,5.3),(5,'dy patil'),(6,'be'),(7,'comp'),(8,(45,'div',12.2)))
#
# for value in enumerate(t): # (0,101)
#     print(value,type(t))

# for key,value in enumerate(t):
#     print(f'key = {key} , value = {value}')
#     print('{}_{}' .format(key,value))




######################################################
#list
# any data type hold
# collection of element stored
# []
# , seperate
# value change or deleted


 #  0      1     2  3    4  5     6      7         8    9    starting index
# L = [101,'Ritu',56,5.3,'C','DS','CPP','Dy Patil','BE','Comp']
#  #  1      2     3  4   5   6     7      8         9    10   Ending index
#  #  -10    -9   -8  -7  -6  -5   -4     -3        -2    -1    negativeindex
#
# print(type(L))
# for key,value in enumerate(L):
#     print(f'key={key} value={value}')

#  #  0      1     2  3    4  5     6      7         8    9    starting index
# l = [101,'Ritu',56,5.3,'C','DS','CPP','Dy Patil','BE','Comp']
#  #  1      2     3  4   5   6     7      8         9    10   Ending index
#  #  -10    -9   -8  -7  -6  -5   -4     -3        -2    -1    negativeindex

#Syntax => Listname[startingindex:endingindex:step]

#print(l[0:10][::-1]) #REVERSE
# l[3] = 5.5  #list is changeble
# print(l)
# del l[3]
# print(l)
# del l
# print(l)

# l2 = l*3
# print(l2) #list can be multiplied
# l =(101)
# print(l,type(l))
# l2 =[101]
# print(l2,type(l2))
# l3=(101,)
# print(l3,type(l3))

# l = [101,'Ritu',56,5.3,'C','DS','CPP','Dy Patil','BE','Comp']

# print(l)
# print( len(l) )
# print( l[0],type(l[0]) )
# print( l[1],type(l[1]) )
# print( l[2],type(l[2]) )
# print( l[3],type(l[3]) )
# print( l[4],type(l[4]) )
# print( l[7],type(l[7]) )

# for value in enumerate(l):
#     print(value,type(value))
# l = [(0,101),(1,'Ritu'),(2,56),(3,5.3),(4,'C'),(5,'DS'),(6,'CPP'),(7,'Dy Patil'),(8,'BE'),(9,'Comp')]
# for key,value in enumerate(l):
#     print(f'key = {key} value = {value }')



###########################################
#string
# collection of characters
# collection of element stored
# ''  " "   ''' '''  """ """
# , seperate
# NO value change or deleted
#can't delete inner data  , can delete whole string
#Data can be modify
#
#     0   1   2   3   4   5   6  7  8  9   #startingindex
#     V   o   w   T   e   c   h     I  T
#     1   2   3   4   5   6   7  8  9  10  #endingindex
#     -12 -11 -10 -9 -8   -7  -6 -5 -4 -3  #negativeindex

# s = 'VowTech IT'
# print(type(s))
# print(s)

# print(s[0],type(s[0]))
# print(s[1],type(s[1]))
# print(s[2],type(s[2]))
# print(s[3],type(s[3]))
# print(s[4],type(s[4]))
# print(s[5],type(s[5]))
# print(s[6],type(s[6]))
# print(s[7],type(s[7]))
# print(s[8],type(s[8]))
# print(s[9],type(s[9]))

# s = 'VowTech IT'
# print(type(s))
# # s[3] = 'f' #error
# # del s[3] #error
# # del s  #deletetion can be done
# print(s)

#     0   1   2   3   4   5   6  7  8  9   #startingindex
#     V   o   w   T   e   c   h     I  T
#     1   2   3   4   5   6   7  8  9  10  #endingindex
#     -12 -11 -10 -9 -8   -7  -6 -5 -4 -3  #negativeindex

# s1 = 'Vowtech'
# s2 = ' IT'
# s3 = s1 + s2 #concate
# s4 = s1*4
# print(s3)
# print( s4)

# s1 = 'VowTech '
# s2 = s1*3
# s2 = s2[:len(s2)-1]
# print(s1)
# print(s2)

# s = 'Vowtech'
# print(s)
# s1 = s[0:3]
# print(s1)
# s2 = 'T'
# print(s2)
# s3 = s[4:7]
# print(s3)
# s4 = s1+s2+s3
# print(s4)

# s = 'Vowtech'
# print(s)
# print(s[0:3]+' T'+s[4:7])

# s = 'Vowtech'
# print(s)
# print( len(s) )
# print( s[0],type(s[0]) )
# print( s[1],type(s[1]) )
# print( s[2],type(s[2]) )
# print( s[3],type(s[3]) )
# print( s[4],type(s[4]) )
# print( s[5],type(s[5]) )
# print( s[6],type(s[6]) )


# s = 'Vowtech'
# print(s)

# s = ((0,'V'),(1,'O'),(5,'W'),(6,'T'),(7,'E'),(8,'C'),(45,'H'))

# for i in range(len(s)):
#     print(s)

# for key,value in enumerate(s):
#     print(f'key = {key} value = {value}')

# s = 'Vowtech'
# for i in range(0,len(s)):
#     print(s[i],type(s[i]))


# s = ((0,'V'),(1,'O'),(5,'W'),(6,'T'),(7,'E'),(8,'C'),(45,'H'))
# for i in range(0,len(s)):
#     print(s[i],type(s[i]))

# s = 'vowtech'
# for value in enumerate(s):
#     print(value)

# s = ((0,'V'),(1,'O'),(5,'W'),(6,'T'),(7,'E'),(8,'C'),(45,'H'))
# for key,value in s:
#     print(f'key={key} value={value}')


# a = 'Vaibhav Anil Dhotr'
# print(a[0:len(a)]+'eeeeeee')



#############################################
#conversions
#tuple - string = same  = no  change
#list change

# t = (101,'ritu',56,5.3,'dy patil','be','comp')
# print(type(t))
# print(t)
# l = list(t)
# print(type(l))
# print(l)
# l[3]= 5.5
# del(l[3])
# print(l,type(l))
# t = tuple(l)
# print(t,type(t))

# t = (101,'ritu',56,5.3,'dy patil','be','comp')
# s =str(t)
# print(type(s))
# print(s)

# l = [101,'ritu',56,5.3,'dy patil','be','comp']
# s =str(l)
# print(type(s))
# print(s)

# s = 'vowtech'
# print(type(s))
# t = tuple(s)
# print(t,type(t))

# s = 'vowtech'
# print(type(s))
# l = list(s)
# print(l,type(l))


##############
# Dictionary
# key -Any Data Type _ int,float,string,tuple,list
# Value -Any Data Type_ int,float,string,tuple,list
# Syntax
# {}
#{ key : value , key:value..........Key:ValueN.. }
#key means user defines value
#key is unique.


# d = {}
# print(type(d))
# print(d)


# d = dict()   #will print empty dict
# print(type(d))
# print(d)


# d = {'ID':101,'Name':'Ritu',5.6:'Height','Classes':('C','DS','CPP'),'CollegeInfo':['DY','BE','2ndYEAR']}
# print(d['ID'])
# print(type(d))
# print(d)

# TO get single value
# d['keyname']  #to get the key value
# print(d['Name'])
# print(d[5.6])
# print('Classes')
# print('CollegeInfo')

#we can not get the slice

#
# d = {'ID':101,'Name':'Ritu',5.6:'Height','Classes':('C','DS','CPP'),'CollegeInfo':['DY','BE','2ndYEAR']}
# print(d)
# print(d.keys())  #to get the keys (list of kays ayga)

# for key in d.keys():    #to get the keys individually
#     print(key,d[key])
#     print(f'key : {key} , value : {d[key]}')

# for key in d:    #to get the keys individually
#     print(key,d[key])
#     print(f'key : {key} , value : {d[key]}')




# d = {'ID':101,'Name':'Ritu',5.6:'Height','Classes':('C','DS','CPP'),'CollegeInfo':['DY','BE','2ndYEAR']}

# print(d.values())  #to get list of value
# print(d.keys()) #to get the list of values

# for value in d.values():
#     print(value)

#enumerate ke jaise chahiye to 'd.items()' can be used
#
# d = {'ID':101,'Name':'Ritu',5.6:'Height','Classes':('C','DS','CPP'),'CollegeInfo':['DY','BE','2ndYEAR']}
# # print(d.items()) #list of tuple
#
# # for value in d.items():
# #     print(value) #('Name', 'Ritu')
#
# for key,value in d.items():
#     print(f'key : {key} value : {value}') #key : Name value : Ritu

# d = { 'order-1' : {'Item1': ['Roti',10,20],'Item2':['Butter Chicken',2,570],'Item3':['plater',2,2750],'status':'pending'} ,
#      'order-2'   : {'Item1': ['Roti',5,20],'Item2':['Chicken Masala',1,270],'status':'Sucess'} }
# k = d.keys()
# for key in k:
    # print(key,' - ', d[key]) #key Nd values milega of both order
    # print(key,d[key]['Item1']) #item1
    # print(key,d[key]['status']) #to get status
    # print(f'status : {d[key]["status"]} ')
    # print(f'status : {d[key]["Item1"]}') #status
    # print(f'order1 : {d[key]["Item1"]} ') #print item1
    # print(f'order1 : {d[key]["Item1"][0]}') #roti
    # print(f'order1 : {d[key]["Item1"][1]}')  #10 and 5
    # print(f'order1 : {d[key]["Item1"][2]}') #20 and 20
#
# d = { 'order-1' : {'Item1': ['Roti',10,20],'Item2':['Butter Chicken',2,570],'Item3':['plater',2,2750],'status':'pending'} ,
#      'order-2'   : {'Item1': ['Roti',5,20],'Item2':['Chicken Masala',1,270],'status':'Sucess'} }
#
# k = d.keys()
# for key in k:
#     print(f'order number = {key} \n order details= {d[key]} ')




# k = d.keys()
# for key in k:
#     print(f'order number : {key}')
#     data = d[key]
#     print(data)
#     for datakey in data.keys():
#         if datakey != 'status':
#             print(datakey)


# d = { 'order-1' : {'Item1': ['Roti',10,20],'Item2':['Butter Chicken',2,570],'Item3':['plater',2,2750],'status':'pending'} ,
#      'order-2'   : {'Item1': ['Roti',5,20],'Item2':['Chicken Masala',1,270],'status':'Sucess'} }
# d = d.keys()
# for key in d:
#      print(f'order number - {key}  order details - ')




# for key in d:#['order-1','order-2']
#      print(f'Order Id is - {key}')
#      order = d[key]
#      for k in order:
#           if k == 'status'


#############################################
# c1 = complex()
# print(type(c1))
#
# c1 = complex(10,15)
# print(type(c1))
# print(c1)

############################################ VIDEO 10
# d = {'ID':101,'Name':'Ritu',5.6:'Height','Classes':('C','DS','CPP'),'CollegeInfo':['DY','BE','2ndYEAR']}
# print(d)
#
# d1 ={'ID':101,'Name':'Ritu',5.6:'Height',('C','DS','CPP'):'Classes','CollegeInfo':['DY','BE','2ndYEAR']}
# print(d1)
#
# d2 = {'ID':101,'Name':'Ritu',5.6:'Height',('C','DS','CPP'):'Classes',['DY','BE','2ndYEAR']:'CollegeInfo'}
# print(d2)  #unhashable type : 'list'

# a =10 ; b = 20 ; print(a,b,f'sum = {a+b}' )

# a =3 ; b = 4 ; print(a,b)

#this is also a data type.
# c1 = complex()
# print(type(c1))
# print(c1)
# c1 = complex(11)
# print(type(c1))
# print(c1)
# c1 = complex(11,22)
# print(type(c1))
# print(c1)
# c1 = complex(11,-22)
# print(type(c1))
# print(c1)

# str1 = 'hello vowtech'
# str2 = 'how are you'
# print(str1[4])
# print(str1[4:])
# print(str1[5])
# print(str1[6:9])
# print(str1[0:len(str1)][::-1])
# print(str1[0:len(str1)])

####### Keywords #######
#These keywords are commonly used in conditional statements, loops, and other constructs where boolean values are required.
# a = None
# print(a)
# a = 56>34
# print(a)
# a = 10<1
# print(a)

# 10 int literal
# 10.23  float literal
# ''   string literal
#[] , ()  list and tuple literal

#kabhi bhi value dekha s usko operator kahenge

# import math
# import statistics

# a = 10%3 #1
# print(a)
#
# a = 3%5 #3
# print(a)
#
# a = 5%3 #2
# print(a)
#
# q,r = divmod(10,3 # 3 1
# print(q,r)

# ()
#* / %
# =


#comparison operator (< > = >= <= == !=)

# if else elif.......
#syntax
#if (condition)   or  if condition
#if ()

# if (condition):
#       statement-1
#       statement-2
#       statement-3
#       statement-4

#non-zero -true
#zero - false

# if 10>1:
#     print('yes1')
# print('R1')    #THIS IDENTATION SHOW IT IS OUTOFF LOOP
# print('R2')
# print('R3')

# if 10<1:
#     print('yes1')
# print('R1')    #THIS IDENTATION SHOW IT IS OUTOFF LOOP
# print('R2')
# print('R3')

# if 10<1:
#     print('yes1')  #Nothing will print

#######################  Q-1  ###################################
# user se quantity & price leneka
# QTY>1000 then dis= 10%  OW 0%
#ex/ qty = 1000 price 2 rupees   dis=0%  total = 2000  dis = 2000*0/100 =  0rs tp = 2000-0 = 2000

#ex/ qty = 2000 price 2 rupees   dis=10%  total = 4000  disr = 2000*10/100 = 400rs tp = 4000-400 = 3600

# qty = int(input('enter the quantity: '))
# price = float(input('enter the quantity: '))
# dis=0
# if qty>1000:
#     dis= 10  #condition true hai if  ke andar jaygaand print karega varna bahar ayga
# print(f'Discount = {dis}%')
#
# total = qty*price  #totalamount
# disr = total * dis/100  #discountrupees
# tp = total - disr #totalpayableamount
# print(f'discount in percent is {dis}%')
# print(f'Total in Rs: {total}')
# print(f'Discounted in Rs: {disr}')
# print(f'Total payable amount: {tp}')


#######################  Q-2  ###################################
# cy & jy current year and joining year
# yos = cy-jy
#if yos>3 then bonus = 2500 OW Nothing print!!!

# cy,jy = int(input('enter the current year: ')),int(input('enter the joining year: '))
# yos = cy -jy
# if yos>3:
#     bonus = 2500
#     print(f'YOU  ARE ELLIGIBLE FOR BONUS Rs: {bonus}')


# if 10>1:  #will print yes1 along with r1r2r3
#     print('yes1')
# else:
#     print('no1')
# print('R1')    #THIS IDENTATION SHOW IT IS OUTOFF LOOP
# print('R2')
# print('R3')

# if 10<1:  #when condn is  false will print no1 along with r1r2r3
#     print('yes1')
# else:
#     print('no1')
# print('R1')    #THIS IDENTATION SHOW IT IS OUTOFF LOOP
# print('R2')
# print('R3')


#######################  Q-3  ###################################
# Basic salary user se leneka
# bs <1500 hra=10 and da = 90
# ex bs= 1000  hra = 1000*10/100 100  da = 1000*90/100 = 900
# gs = bs+hra+da
# bs>=1500 hra = 500 da = 98%
# bs = 2000 hra = 500 da = 2000*0.98 = 1960
#
# bs = int(input('enter the basic salary: '))
# if bs<1500:
#     hra = bs*0.1
#     da = bs*0.9
# else:
#     hra = 500
#     da = bs * 0.98
#
# gs = hra + bs + da
# print(f'Basic Salary Rs. {bs}')
# print(f'HRA Rs. {hra}')
# print(f'DA Rs. {da}')  #ALLOWANCE
# print(f'Gross Salary Rs. {gs}') #totalsalary


################################ VIDEO 11 ###############################
# nested if-else


# i = 3
# if i ==1:
#     print('YES1')
# else:
#     if i == 2:
#         print('YES2')
#     else:
#         print('NO2')
#     print('P1')
# print('P2')
#
# i = 12
# if i ==1:
#
#     if i == 2:
#         print('YES12')
#     else:
#         print('NO12')
#     print('R1')
#
# else:
#     print('YES2')
#
# print('R2')

# i = 12
# if i == 1:
#
#     if i == 2:
#         print('YES12')
#     else:
#         print('NO12')
#     print('R1')
#
# else:
#     if i == 2:
#         print('YES22')
#     else:
#         print('NO22')
#     print('R2')
#
# print('R3')

#######################  Q-4  ###################################

# PERCENTAGE QUESTION
# 60>= FC first class
#50-59 SC
#40-49 PC
#Below 40 Fail

# per = int(input('Enter Percentage :'))
# if per >= 60 :
#     print('Pass with First class')
# else:
#     if per >=50:
#         print('Pass with Second class')
#     else:
#         if per >= 40:
#             print('pass with pc')
#         else:
#             print('you are failed')
#         print('R1')
#     print('R2')
# print('R3')

#Drawbacks
# 1] 1000 condition - 1000 nested 'if -else' statements
# Complexity increses for large condition
# care which 'if-else' is with which 'if-else'
# misplaced 'if'
# misplaced 'else'
#Space problem - improper indentation can cause problem

# per = int(input('Enter Percentage :'))
# if per >= 60 :
#     print('Pass with First class')
# else:
#     if per >=50:
#         print('Pass with Second class')
#     else:
#         if per >= 40:
#             print('pass with pc')
#         else:
#             print('you are failed')
#         print('R1')
#     print('R2')
# print('R3')

#to overcome use logical operator - and or not
# per = int(input('Enter Percentage :'))
#
# if per >= 60:
#     print('FC')
# if per>=50 and per <60:
#     print('SC')
# if per>=40 and per <50:
#     print('PC')
# if per<40:
#     print('FAILED')
#
# print(f'YOU GOT {per}%!!!!')
#
# #Drawback - as it will check every condtion so it will degrade the performance
# #slow performance

#solutin -  if => elif
# per = int(input('Enter Percentage :'))
# if per >= 60:
#     print('FC')
# elif per>=50 and per <60:
#     print('SC')
# elif per>=40 and per <50:
#     print('PC')
# else:
#     print('FAILED')
#
# print(f'YOU GOT {per}%!!!!')

#without LO solved!!!!
#problem - order up down can give wrong answer
# per = int(input('Enter Percentage :'))
# if per >= 60:
#     print('FC')
# elif per>=50 :
#     print('SC')
# elif per>=40:
#     print('PC')
# else :
#     print('FAILED')

#using operator won't affected by order but it will check every condn
#best => elif plus logical operator
# per = int(input('Enter Percentage :'))
# if per >= 60:
#     print('FC')
# elif per>=50 and per <60:
#     print('SC')
# elif per>=40 and per <50:
#     print('PC')
# else:
#     print('FAILED')
#
# print(f'YOU GOT {per}%!!!!')

# Bank
# 1 lac policy hai
#Policy Add - toh if-elif is best as we can put it everywhere as it won't affect the results

# Nested if else - NO use LO

########################## Q-5 #################
# MS - M => IP
# MS - U GEN-M AGE>30 => IP
# MS - U GEN-F AGE>25 => IP
# OW INP

# ms = str(input('Enter you maritial status M or U :'))
# age = int(input('Enter your age :'))
# gen = str(input('Enter you gender [M/F] :'))
#
# if ms =='M':
#     print('IP')
# else:
#     if gen=='M':
#         if age>30:
#             print('Male-IP')
#         else:
#             print('Male-INP')
#         print('R1')
#     else:
#         if age > 25:
#             print('FeMale-IP')
#         else:
#             print('FeMale-INP')
#         print('R2')
# print('R3')

#Using 'Elif"
# ms = str(input('Enter you maritial status M or U :'))
# age = int(input('Enter your age :'))
# gen = str(input('Enter you gender [M/F] :'))
#
# if ms =='M':
#     print('IP')
#
# elif gen=='M':
#     if age>30:
#         print('Male-IP')
#     else:
#         print('Male-INP')
#     print('R1')
# else:
#     if age > 25:
#         print('FeMale-IP')
#     else:
#         print('FeMale-INP')
#     print('R2')
# print('R3')

#
# ms = str(input('Enter you maritial status M or U :'))
# age = int(input('Enter your age :'))
# gen = str(input('Enter you gender [M/F] :'))
#
# if ms =='M':
#     print('IP')
# elif gen=='M' and age>30:
#     print('Male-IP')
# elif gen == 'F' and age > 25:
#     print('FeMale-IP')
# else:
#     print('FeMale-INP')

# ms = str(input('Enter you maritial status M or U :'))
# age = int(input('Enter your age :'))
# gen = str(input('Enter you gender [M/F] :'))
#
# if (ms =='M') or (gen=='M' and age>30) or (gen == 'F' and age > 25) :
#     print('IP')
# else:
#     print('INP')
# print('R1')


################# Q-6
# gen = input('Enter you gender [M/F] :')
# yos = int(input('Enter YOS: '))
# qual =input('Enter your qualification [G/PG]: ')
#
# salary =  None
# if gen == 'M' and yos>=10 and qual == 'P':
#     salary = 15000
# elif gen == 'F' and yos>=10 and qual == 'P':
#     salary = 12000
# elif (gen == 'M' and yos>=10 and qual == 'G') or (yos<10 and qual == 'P'):
#     salary = 10000
# elif gen == 'F' and yos>=10 and qual == 'G':
#     salary = 9000
# elif gen == 'M' and yos<10 and qual == 'G':
#     salary = 7000
# elif gen == 'F' and yos<10 and qual == 'G':
#     salary = 6000
#
# print(f'Salary Provided Rs. {salary}')


################ Company Question Mindtree
'''
Input - 1
78
90
84
92
95
Output - 1
87.8
Medical

Input - 2
92
94
97
99
90
Output - 2
94.4
JEE,Medical

Input - 3
92
27
65
57
80
Output - 1
64.2
Fail


Input - 4
92
75
80
98
95
Output - 1
88.0
JEE

Input - 5
80
55
99
98
97
Output - 1
85.8
Fail
'''

# maths = int(input('enter the marks for math'))
# biology = int(input())
# english = int(input())
# hindi = int(input())
# social_studies = int(input())
#
# per = ((maths+biology+english+hindi+social_studies)/500)*100
# print('%.1f' %per)
# if (maths < 30 or biology < 30 or english < 30 or hindi < 30 or social_studies < 30):
#     print('Fail')
# elif (maths >=90 and biology >=70 and per >80) and (biology >=90 and per >= 60):
#     print('JEE and Medical')
# elif maths >=90 and biology >=70 and per >80 :
#     print('JEE')
# elif biology >=90 and per >= 60:
#     print('Medical')
# else:
#     print('fail')


'''
Input - 1
78 90 84 92 95
Output - 1
87.8
Medical

Input - 2
92 94 97 99 90
Output - 2
94.4
JEE,Medical

Input - 3
92 27 65 57 80
Output - 1
64.2
JEE,Medical

Input - 4
92 75 80 98 95
Output - 1
88.0
JEE

Input - 5
80 55 99 98 97
Output - 1
85.8
Fail

'''

# maths , biology , english , hindi , social_studies = list(map(int,input('Enter the marks:').split()))
# per = ((maths+biology+english+hindi+social_studies)/500)*100
# print('%.1f' %per)
# if (maths < 30 or biology < 30 or english < 30 or hindi < 30 or social_studies < 30):
#     print('Fail')
# elif (maths >=90 and biology >=70 and per >80) and (biology >=90 and per >= 60):
#     print('JEE and Medical')
# elif maths >=90 and biology >=70 and per >80 :
#     print('JEE')
# elif biology >=90 and per >= 60:
#     print('Medical')
# else:
#     print('fail')


####################### Video 13
# if 10:
#     print('yes1')
# else:
#     print('no1')
# print('r1')
# print('r2')
# print('r13')

# if 0:
#     print('yes1')
# else:
#     print('no1')
# print('r1')
# print('r2')
# print('r13')

# if 'vowtech':
#     print('yes1')
# else:
#     print('no1')
# print('r1')
# print('r2')
# print('r13')

# if '':
#     print('yes1')
# else:
#     print('no1')
# print('r1')
# print('r2')
# print('r13')

# if []:
#     print('yes1')
# else:
#     print('no1')
# print('r1')
# print('r2')
# print('r13')

# if 12.34:
#     print('yes1')
# else:
#     print('no1')
# print('r1')
# print('r2')
# print('r13')


#loop
#for while

# for i in range(10,0,-1):
#     print(i)

# while (condition):
#   statement..
#   statement..
# R1
# R2

#infinite 1 print hoga
# i = 1
# while i <= 10:
#     print(i)
# print(f'R i :{i}' )

#using operator
# i = 1
# while i <= 10:
#     print(i)
#     i=i+1
# print(f'R i :{i}' )

# i = 1
# while i <= 10:
#     print(i)
#     i += 1  # i = i + 1  += -= *= /= // %=  Compound Assignment operator
# # print(f'R i :{i}' )

# i = 1
# while i <= 10:
#     print(i,end = ' ')
#     i += 2  # i = i + 1  += -= *= /= // %=  Compound Assignment operator
# print(f'R i :{i}' )

# i = 10
# while i >= 1:
#     print(i,end = '\t')
#     i -= 2  # i = i + 1  += -= *= /= // %=  Compound Assignment operator
# print(f'\nR i : {i}' )

# i = 10
# while i >= 1 :
#     print(i,end='\t')
#     i -= 2  # i = i + 1  += -= *= /= // %=  Compound Assignment operator
# print(f'\nR i :{i}' )

#logic development!!!

# 11 12 13 14
# 21 22 23 24
# 31 32 33 34

# for i in range(1,4):
#     for j in range(1,5):
#         print(f'{i}{j}',end = '\t')
#     print()

# for i in range(1,4): #rows
#     #i = 1      for every i 'j' starting from 1
#     for j in range(1,5): #column 5 aya ki condn false
#         print(f'{i}{j}',end=' ') #11 12 13 14
#     print()

#lets convert into while
# for i in range(1,4):
#     j =1
#     while j<=4:
#         print(f'{i}{j}',end=' ') #11 12 13 14
#         j = j+1
#     print()


# for i in  range (1,4):
#     # i = 1
#     j = 1
#     while j <=4:
#         print(f'{i}{j}',end='\t') #11 12 13 14 15
#         j = j+1
#     print()
#
# i = 1
# while i <4:
#     j = 1
#     while j < 5:
#         print(f'{i}{j}',end='\t') #11 12 13 14 15
#         j = j+1
#     print()
#     i = i+1  #ye nnhi diya toh 11 12 13 14 infinite print karega

# i = 1
# while i <4:
#     for j in range(1,5):
#         print(f'{i}{j}', end='\t')
#     print()
#     i = i+1



# 31 32 33 34 35
# 41 42 43 44 44
# 51 52 53 54 55
# 61 62 63 64 65

# for i in range(3,7):
#     #i=3 4 5 6
#     for j in range(1,6):
#         print(f'{i}{j}', end = ' ')
#     print()

#lets convert into while
#1]
# 1
# 12
# 123
# 1234
# 12345
#each row value cjanges => J
# for i in range(1,6):
#
#     for j in range(1,i+1):
#         print(f'{j}',end='')
#     print()

#2]
# 1
# 22
# 333
# 4444
# 55555

# each row same value  => i
# for i in range(1,6):
#
#     for j in range(1,i+1):
#         print(f'{i}',end='')
#     print()


#3]
# 12345
# 1234
# 123
# 12
# 1

# for i in range (5,0,-1):
#     #i 1 2 3 4 5
#     for j in range(1,i+1):
#         print(f'{j}',end = '')
#     print()
#
# #alternate solution
# for i in range (6,1,-1):
#     #i 1 2 3 4 5
#     for j in range(1,i):
#         print(f'{j}',end = '')
#     print()

#4]
# 4567
# 456
# 45
# 4

# for i in range(8,4,-1):
#     for j in range(4,i):
#         print(f'{j}', end='')
#     print()


#5]
# 1
# 12
# 123
# 1234
# 12345
# 123456

# for i in range(1,7):
#     for j in range(1,i+1):
#         print(f'{j}',end = '')
#         j=j+1
#     print()

# 1
# 22
# 333
# 4444
# 55555
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(f'{i}',end='')
#     print()


# 4567
# 456
# 45
# 4

# for i in range(8,4,-1):
#     for j in range(4,i):
#         print(f'{j}',end='')
#     print()

# 12345
# 1234
# 123
# 12
# 1

# for i in range(6,1,-1):
#     for j in range(1,i):
#         print(f'{j}',end = '')
#     print()


########################### session 14

# 12345  16
# 2345   26
# 345    36
# 45     46
# 5      56

# for i in  range(1,6):
#     for j in range(i,6):
#         print(f'{j}',end = '')
#     print()


# 54321
# 4321
# 321
# 21
# 1

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(f'{j}',end = '')
#     print()



# 54321
# 5432
# 543
# 54
# 5

# for i in range(0,5):
#     for j in range(5,i,-1):
#         print(f'{j}',end='')
#     print()

#alternative logic
# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(f'{j}',end='')
#     print()


# 5        56
# 45       46
# 345      36
# 2345     26
# 12345    16

# for i in range(5,0,-1):
#     for j in range(i, 6):
#         print(f'{j}', end='')
#     print()

#Alternative logic
# for i in range(1,6):
#     for j in range(6-i, 6):
#         print(f'{j}', end='')
#     print()

#
# 1           10
# 21          20
# 321         30
# 4321        40
# 54321       50

# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(f'{j}',end = '')
#     print()
#
# #alternative logic
# for i in range(5,0,-1):
#     for j in range(6-i,0,-1):
#         print(f'{j}',end = '')
#     print()


# 5         54
# 54        53
# 543       52
# 5432      51
# 54321     50

# for i in range(4,-1,-1):
#     for j in range(5,i,-1):
#         print(f'{j}', end='')
#     print()
#
# #alternative solution
# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(f'{j}', end='')
#     print()
#

# 1        12  21
# 22       13  31
# 333      14  41
# 4444     15  51
# 55555    16  61

# for i in range(1,6):
#     for j in range(0,i):
#         print(f'{i}', end='')
#     print()
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(f'{i}', end='')
#     print()


# 5          56   65
# 44         46   64
# 333        36   63
# 2222       26   62
# 11111      16   62

# for i in range (5,0,-1):
#     for j in range(i,6):
#         print(f'{i}', end='')
#     print()

#alternative solution
# for i in range (5,0,-1):
#     for j in range(6,i,-1):
#         print(f'{i}', end='')
#     print()


# 55555   50      61      16
# 4444    40      51      15
# 333     30      41      14
# 22      20      31      13
# 1       10      21      12

# for i in range(5,0,-1):
#     for j  in range(i,0,-1):
#         print(f'{i}', end='')
#     print()
#
# for i in range(5,0,-1):
#     for j  in range(i+1,1,-1):
#         print(f'{i}', end='')
#     print()

####################### session 15

# 11111    16 61
# 2222     26 62
# 333      36 63
# 44       46 64
# 5        56 65

# for i in range(1,6):
#     for j in range(i,6):
#         print(f'{i}', end='')
#     print()

#alternative logic
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print(f'{i}', end='')
#     print()


# 12345    odd 16
# 4321     even 40
# 123      odd 14
# 21       even 20
# 1        odd 12

# for i in range(5,0,-1):
#     #i = 5
#     if i%2==0:    #even  4 2
#         for j in range(i,0,-1):
#             print(f'{j}', end='')
#     else:           #odd
#         for j in range(1,i+1):
#             print(f'{j}', end='')
#     print()



# 1234567      18
# 12345        16
# 123          14
# 1            12

# for i in range(10,1,-2):
#     for j in range(1,i-2):
#         print(f'{j}',end='')
#     print()
#
# for i in range(8,1,-2):
#     for j in range(1,i):
#         print(f'{j}',end='')
#     print()


# 1        odd
# 01       even
# 101      odd
# 0101     even
# 10101    odd
#
# for i in range(1,6):
#     #i = 4
#     if i%2==0:     #even
#         for j in range(1,i+1):
#             if j%2==0:
#                 print(f'{1}',end='')
#             else:
#                 print(f'{0}',end='')
#     else:           #odd
#         for j in range(1,i+1):
#             if j%2==0:
#                 print(f'{0}',end='')
#             else:
#                 print(f'{1}',end='')
#     print()

# 1
# 01       even
# 101      odd
# 0101     even
# 10101    odd


# for i in range(1,6):
#     #i = 4
#     if i%2==0:     #even
#         for j in range(0,i):  #0 4
#             print(f'{j%2}',end='')    #0101
#     else:           #odd
#         for j in range(1,i+1):  #1,6
#             print(f'{j%2}',end='')
#     print()


# 1
# 01
# 101
# 0101
# 10101

# alternative solution
# for i in range(1,6):
#     #i = 4
#       for j in range(1,i+1):  #1,6
#             print(f'{(i+j+1)%2}',end='')  #for i =4 j will move 4 times
#       print()
            #4+1+1=6  6%2=0  0
            #4+2+1=7  6%2=1  1
            #4+3+1=8  6%2=0  0
            #4+4+1=9  6%2=1  1

# 13579
# 3579
# 579
# 79
# 9

# for i in range(1,10,2):
#     for j in range(i,10,2):
#         print(f'{j}',end = '')
#     print()



# 1             odd   1 2       1+1
# 2 4           even  2 5
# 1 3 5         odd   1 6       3+3
# 2 4 6 8       even  2 9
# 1 3 5 7 9     odd   1 10      5+5

# for i in range(1,6):
#     #i=2
#     if i%2==0:   #2 4
#         for  j in range(2,i*2+1,2):
#             print(f'{j}',end = ' ')
#     else:  #1 3 5
#         for j in range(1,2*i,2):
#             print(f'{j}',end = ' ')
#     print()


#remove space from last
# 1             odd   1 2   =>    1+1
# 2 4           even  2 5
# 1 3 5         odd   1 6    =>   3+3
# 2 4 6 8       even  2 9
# 1 3 5 7 9     odd   1 10   =>   5+5
#
# for i in range(1,6):
#     #i=2
#     if i%2==0:   #2 4
#         for  j in range(2,i*2+1,2):
#             if j == 2*i :
#                 print(f'{j}',end = '')
#             else:
#                 print(f'{j}',end = ' ')
#
#
#     else:  #1 3 5
#         for j in range(1,2*i,2):
#             if j == i*2-1 :
#                 print(f'{j}',end = '')
#             else:
#                 print(f'{j}',end = ' ')
#
#     print()


############################# session 16
# 25]
# 55555     5          5555
# 45555     45         555
# 34555     345        55
# 23455     2345       5
# 12345     12345

# for i in range(5,0,-1):
#     for j in range(i,6):
#         print(f'{j}',end='')
#
#     for j in range(1,i):
#         print(f'{5}',end='')
#     print()

# 26]
# 1
# 23
# 456
# 78910

# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(f'{k}', end = '')
#         k += 1
#
#     print()



# 27]
# 1
# 23
# 456
# 78910


# for i in range(1,5):
#     k = i(i-1)//2 + 1         1 2 3 4  => 1 2 4 7
#     for j in range(1,i+1):
#         print(f'{k}', end = '')
#         k += 1
#
#     print()



# 28]
# 1            odd
# 10           even
# 101          odd
# 1010         even
# 10101        odd


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(f'{j%2}',end='')
#     print()

# 29]
#18lacs
# 1                     1 2
# 2 6                   2 6
# 3 7 10                3 11
# 4 8 11 13             4 14
# 5 9 12 14 15

# 30]
# for i in range(1,6):
#     k=i
#     l=4
#     for j in range(1,i+1):
#         print(f'{k}', end=' ')
#         k += l
#         l -= 1
#     print()

# for i in range(1,6):
#     k=i
#     l=4
#     for j in range(1,i+1):
#         if j==i:
#             print(f'{k}', end='')
#         else:
#             print(f'{k} ', end='')
#         k += l
#         l -= 1
#     print()

# Q-32
# N=5     input
# 1
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15

# n = int(input())
# for i in range(1,n+1):
#     k=i
#     l=4
#     for j in range(1,i+1):
#         if j==i:
#             print(f'{k}', end='')
#         else:
#             print(f'{k} ', end='')
#         k += l
#         l -= 1
#     print()

#Q32]
# Input: 8
# 	Output:
# 1
# 2 9
# 3 10 16
# 4 11 17 22
# 5 12 18 23 27
# 6 13 19 24 28 31
# 7 14 20 25 29 32 34
# 8 15 21 26 30 33 35 36

# n=int(input())
# for i in range(1,n+1):
#     #i=1,2,3,4,5
#     k=i # k=5
#     l=n-1
#     for j in range(1,i+1):# 1,6
#         if j==i:# 1 2 3 4 5== 5
#             print(k, end='')  # 5-9-12-14-15-
#         else:
#             print(k, end=' ')  # 5-9-12-14-15-
#         k += l #k=k+l k =14+1=15
#         l-=1 # l=0
#     print()


# Q-33]
# 1             12
# 123           14
# 12345         16
# 1234567       18

# for i in range(1,5):
#     #i=1 2 3 4 5
#     for j in range(1,i*2):
#         print(f'{j}', end='')
#     print()
#
# #without last space
#
# for i in range(1,5):
#     #i=1 2 3 4 5
#     for j in range(1,i*2):
#         if j==i*2:
#             print(f'{j} ', end='')
#         else:
#             print(f'{j}', end='')
#     print()


# Q-34]
# 12344321       15   0*  40
# 123**321       14   2*  30
# 12****21       13   4*  20
# 1******1       12   6*  10
#
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print(f'{j}', end='')
#
#     for j in range(i,4):
#         print(f'**', end='')
#
#     for j in range(i,0,-1):
#         print(f'{j}', end='')
#
#
#     print()

# 12344321
# 123  321
# 12    21
# 1      1

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print(f'{j}', end='')
#
#     for j in range(i,4):
#         print(f'  ', end='')
#
#     for j in range(i,0,-1):
#         print(f'{j}', end='')
#     print()

# Q35]
# ____*
# ___*_*
# __*_*_*
# _*_*_*_*
# *_*_*_*_*

#mylogic
# for i in range(5,0,-1):
#     #forspace
#
#     for j in range(i,1,-1):
#         print(f' ', end='')
#
#     for j in range(i,6):
#         print(f'* ', end='')
#
#     print()
#
#
#
#sir logic
# for i in range(1,6):
#     #forspace
#
#     for j in range(i,5):
#         print(f' ', end='')
#
#     for j in range(1,i+1):
#         print(f'* ', end='')
#
#     print()

#withoutspace
# for i in range(1,6):
#     #forspace
#
#     for j in range(i,5):
#         print(f' ', end='')
#
#     for j in range(1,i+1):
#         if j == i:
#             print(f'*', end='')
#         else:
#             print(f'* ', end='')
#
#     print()


#36]
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#
# for i in range(1,6):
#     for j in range(i,5):
#         print(f' ', end='')
#
#     for j in range(1,i+1):
#         if j == i:
#             print(f'*', end='')
#         else:
#             print(f'* ', end='')
#
#     print()
#
# for i in range(4,0,-1):
#     for j in range(i,5):
#         print(f' ', end='')
#
#     for j in range(1,i+1):
#         if j == i:
#             print(f'*', end='')
#         else:
#             print(f'* ', end='')
#
#     print()


#37]
#     *
#   * * *
# * * * * *

# for i in range(1,6):
#     #forspace
#
#     for j in range(i,5):
#         print(f' ', end='')
#
#     for j in range(1,i+1):
#         if j == i:
#             print(f'*', end='')
#         else:
#             print(f'* ', end='')
#
#     print()

#38] same as star logic
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
# for i in range(1,6):
#     #forspace
#
#     for j in range(i,5):
#         print(f' ', end='')
#
#     for j in range(1,i+1):
#         if j == i:
#             print(f'*', end='')
#         else:
#             print(f'* ', end='')
#
#     print()

# 39]
#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5

# for i in range(1,6):
#     #forspace
#
#     for j in range(i,5):
#         print(f' ', end='')
#
#     for j in range(1,i+1):
#         if j == i:
#             print(f'{i}', end='')
#         else:
#             print(f'{i} ', end='')
#
#     print()


# Q39]
#     1
#    2 3
#   4 5 6
#  7 8 9 10

# k=1
# for i in range(1,5):
#     #forspace
#
#     for j in range(i,5):
#         print(f' ', end='')
#
#     for j in range(1,i+1):
#         if j == i:
#             print(f'{k}', end='')
#         else:
#             print(f'{k} ', end='')
#         k+=1
#
#     print()



# 40]
#     A
#    B C
#   A B C
#  A B C E
# A B C D E

# for i in range(1,6):
#     #forspace
#
#     for j in range(i,5):
#         print(f' ', end='')
#     k=65
#     for j in range(1,i+1):
#         if j == i:
#             print(f'{chr(k)}', end='')
#         else:
#             print(f'{chr(k)} ', end='')
#         k+=1
#     print()



# 41]
#     A
#    B B
#   C C C
#  D D D D
# E E E E E
#
# k=65
# for i in range(1,6):
#     #forspace
#
#     for j in range(i,5):
#         print(f' ', end='')
#
#     for j in range(1,i+1):
#         if j == i:
#             print(f'{chr(k)}', end='')
#         else:
#             print(f'{chr(k)} ', end='')
#
#     print()
#     k+=1

#========================session 17
# Q42]
#     1
#   2 3 4
# 5 6 7 8 9

# k=1
# for i in range(1,5):
#     #forspace
#
#     for j in range(i,5):
#         print(f' ', end='')
#
#     for j in range(1,i+1):
#         if j == i:
#             print(f'{k}', end='')
#         else:
#             print(f'{k} ', end='')
#         k+=1
#
#     print()


# Q43]
# 5432*
# 543*1
# 54*21
# 5*321

# for i in range(1,6):
#     #for first logic
#     for j in range(5,0,-1) :
#         if j==i:
#             print(f'*',end = '')
#         else:
#             print(f'{j}',end = '')
#
#     print()

# Q44]
# 1            12     00
# 121          13     10
# 12321        14     20
# 1234321      15     30

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(f'{j}', end='')
#
#     for j in range(i-1,0,-1):
#         print(f'{j}', end='')
#
#     print()

# Q45]
# 0                         10-10   0   9-9
# 909                       9-10    0  9-8
# 89098                     8-10    0  9-7
# 7890987                   7-10    0  9-6
# 678909876                 6-10    0  9-5
# 56789098765               5-10    0  9-4
# 4567890987654             4-10    0  9-3
# 345678909876543           3-10    0   9-2
# 23456789098765432         2-10    0   9-1
# # 1234567890987654321       1-10    0   9-0
#
# for i in range(10,0,-1):
#     for j in range(i,10):
#         print(f'{j}',end='')
#
#     print(f'0',end='')
#
#     for j in range(9,i-1,-1):
#         print(f'{j}', end='')
#
#     print()

# Q46]
# 1        1    12 4 10
# 12      21    13 3 20
# 123    321    14 2 30
# 1234  4321    15 1 40
# 1234554321    16 0 50
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(f'{j}',end='')
#
#     for j in range(i,5):
#         print(f'  ',end='')
#
#     for j in range(i,0,-1):
#         print(f'{j}', end='')
#     print()

# Q46]
# 1        1    12 4 10
# 12      21    13 3 20
# 123    321    14 2 30
# 1234  4321    15 1 40
# 1234554321    16 0 50
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(f'{j}',end='')
#
#     for j in range(i,5):
#         print(f'  ',end='')
#
#     for j in range(i,0,-1):
#         print(f'{j}', end='')
#     print()


# Q-48
#     1     4s 10
#    21     3s 20
#   321
#  4321
# 54321

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(f' ',end='')
#
#     for j in range(i,0,-1):
#         print(f'{j}',end='')
#
#     print()

# Q-49
# 1
# 232
# 45654
# 78910987
# k=1
# for i in range(1,5):
#
#     for j in range(1,i+1):
#         print(f'{k}',end='')
#         k+=1
#
#     l = k-2
#     for j in range(1,i):
#         print(f'{l}',end='')
#         l-=1

    # print()


# Q-50
# 1              1  12
# 2*2            3  14
# 3*3*3          5  16
# 4*4*4*4        7  18
# 4*4*4*4
# 3*3*3
# 2*2
# 1

# for i in range(1,5):
#     #i=1 2 3 4
#     for j in range(1,i+1):
#         if j==i:
#             print(f'{i}', end='')
#         else:
#             print(f'{i}*',end='')
#     print()
#
# for i in range(5,0,-1):
#     #i=1 2 3 4
#     for j in range(1,i+1):
#         if j==i:
#             print(f'{i}', end='')
#         else:
#             print(f'{i}*',end='')
#     print()

# Q-51
# 11
# 12 13
# 13 14 15
# 14 15 16 17

# for i in range(1,5):
#     k=10+i
#     for j in range(1,i+1):
#         print(f'{k}',end=' ')
#         k+=1
#     print()
#


# ============================session 18
# Q-52
#              1        13spaces
#            2 3        11Spaces
#          4 5 6        9Spaces
#       7 8 9 10        6Spaces
# 11 12 13 14 15        0Spaces

# Q-53
#     5  15   54
#    54  14   53
#   543  13   52
#  5432  12   51
# 54321  11   50

# for i in range(5,0,-1):
#     for j in range(1,i):
#         print(f' ',end='')
#
#     for j in range(5,i-1,-1):
#         print(f'{j}',end='')
#     print()

# Q-54
# 1         10 22
# 212       20 23
# 32123     30 24
# 4321234   40 25

#
# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(f'{j}',end='')
#
#     for j in range(2,i+1):
#         print(f'{j}',end='')
#     print()

# Q-55
# 1           12
# 23          24
# 345         36
# 4567        48
# 56789       510

# for i in range(1,6):
#     k=i
#     for j in range(1,i+1):
#         print(f'{k}',end='')
#         k+=1
#     print()

# for i in range(1,6):
#
#     for j in range(i,2*i):
#         print(f'{j}',end='')
#
#     print()

#57]
#  1  2  3  4  5           1  6
#  6  7  8  9              6  10
# 10 11 12                10 13
# 13 14                   13 15
# 15                      15 16

#mylogic
# k=1
# for i in range(1,6):
#     for j in range(i,6):
#         if k>=10:
#             if k==10 or k==13 or k==15:
#                 print(f'{k}',end='')
#             else:
#                 print(f' {k}',end='')
#
#         else:
#             if k==6 or k==1:
#                 print(f' {k}',end='')
#             else:
#                 print(f'  {k}',end='')
#         k+=1
#     print()

# Q-56
# 1234  15  00
# 2341  25  10
# 3421  35  20
# 4321  45  30

#mylogic
# for i in range(1,6):
#     for j in range(i,5):
#         print(f'{j}',end='')
#
#     for j in range(i-1,0,-1):
#         if i-1==4:
#             print(f'',end='')
#         else:
#             print(f'{j}',end='')
#
#     print()


# alternate logic
# for i in range(1,5):
#     for j in range(i,5):
#         print(f'{j}',end='')
#
#     for j in range(i-1,0,-1):
#         print(f'{j}',end='')
#
#     print()


# Q-57
# 11111      odd
# 0000       even
# 111        odd
# 00        even
# 1         odd

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(f'{i%2}',end='')
#     print()


# mylogic
# for i in range(6,0,-1):
#     for j in range(1,i):
#         if i%2==0:
#             print(f'{1}',end='')
#         else:
#             print(f'{0}',end='')
#     print()


# Q58]
#     1             12
#    123            14
#   12345           16
#  1234567          18
# 123456789         1 10
#  1234567         1 8
#   12345          1 6
#    123
#     1
#
# for i in range(1,6):
#     for j in range(4,i-1,-1):
#         print(f' ',end='')
#
#     for j in range(1,2*i):
#         print(f'{j}',end='')
#
#     print()
#
# for i in range(4,0,-1):
#     for j in range(4,i-1,-1):
#         print(f' ',end='')
#
#     for j in range(1,2*i):
#         print(f'{j}',end='')
#
#     print()


# 61]
#         1                   00
#       2 3 2                 21
#     3 4 5 4 3               42
#   4 5 6 7 6 5 4             63
# 5 6 7 8 9 8 7 6 5           84
#
# for i in range(1,6):
#     for j in range(4,i-1,-1):
#         print(f'  ',end='')
#
#     for j in range(i,i*2):
#         print(f'{j} ',end='')
#
#     for j in range(i*2-2,i-1,-1):
#         if j == 0 or j == 1 or j == 2 or j == 3  :
#             print(f'{j}', end='')
#         else:
#             print(f'{j} ',end='')
#
#
#     print()

# 62]
#inverted full pyrmid of *
# * * * * * * * * *      0        9
#   * * * * * * *        1        7
#     * * * * *          2        5
#       * * *            3        3
#         *              4        1
#
# for i in range(5,0,-1):
#     for j in range(i,5):
#         print(f'  ',end='')
#
#     for j in range(i*2-1,0,-1):     #90 70 50 30 10
#         if j==1:
#             print(f'*',end='')
#         else:
#             print(f'* ',end='')
#
#     print()


# 63]
# *000* 000*             *000 * 000*
# 0*00* 00*0    =>       0*00 * 00*0
# 00*0* 0*00             00*0 * 0*00
# 000** *000             000* * *000

# for i in range(1,5):
#
#     #first
#     for j in range(1,5):
#         if j == i:
#             print(f'*',end='')
#         else:
#             print(f'{0}',end='')
#     #second
#     print('*',end='')
#
#     #third
#     for j in range(4,0,-1):
#         if j == i:
#             print(f'*',end='')
#         else:
#             print(f'{0}',end='')
#     print()

# Q-63
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

#to get space
# num=14641
# s=str(num)
# for v in s:
#     print(f'{v} ',end='')

#with space
# for i in range(5):
#     num = 11 ** i
#     s = str(num)
#     for v in s:
#         print(f'{v} ', end='')
#     print()

#without space

# for i in range(5):
#     num = 11 ** i
#     s = str(num)
#     for j in range(len(s)):
#         if i==j:
#             print(f'{s[j]}', end='')
#         else:
#             print(f'{s[j]} ', end='')
#
#     print()

# Q-64
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
# 6 12 18 24 30 36
# 7 14 21 28 35 42 49
# 8 16 24 32 40 48 56 64
# 9 18 27 36 45 54 63 72 81
# 10 20 30 40 50 60 70 80 90 100

# for i in range(1,11):
#     for j in range(1,i+1): #i=3
#         print(f'{i*j}',end=' ')
#
#     print()


# pn    1   1   2   3   5
# nn    1   2   3   5   8
# sum   2   3   5   8   13

# Q-65
# 1
# 1 2
# 3 5 8
# 13 21 34 55
# 89 144 233 377 610

# pn,nn =1,1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(f'{pn}',end=' ')
#         sum = pn + nn
#         pn = nn
#         nn = sum
#
#     print()



# Q-66
# 1 2 3 4 5    11 16
# 2 1 2 3 4    21 15
# 3 2 1 2 3    31 14
# 4 3 2 1 2    41 13
# 5 4 3 2 1    51 12

# for i  in range(1,6):
#     for j in range(i,1,-1):
#         print(f'{j} ',end='')
#
#     for j in range(1,7-i):
#         print(f'{j} ',end='')
#
#     print()

# Q-66
# 1                            odd
# 3 2                          even
# 4 5 6                       odd
# 10 9 8 7                    even
# 11 12 13 14 15             odd
#
# k=1
# for i in range(1,6):
#     if i%2==0:       #even 2 4
#         l= k+i-1
#         k=l+1
#         for j in range(1,i+1):
#             print(f'{l} ',end='')
#             l-=1
#
#     else:           #odd
#         for j in range(1,i+1):
#             print(f'{k} ',end='')
#             k+=1
#
#     print()
#

##################################session 21

# 1
# 2 3
# 4 5 6
# 7 8 9 10

# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         if k == 1 or k==3 or k==6 or k==10:
#             print(f'{k}', end='')
#         else:
#             print(f'{k} ',end='')
#         k+=1
#     print()



# ch = ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(f'{chr(ch)}',end='')
#         ch += 1
#     print()






# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1



#              1    13S
#            2 3    11S
#          4 5 6    9S
#       7 8 9 10    6S
# 11 12 13 14 15    0S
#
# k , l = 1 , 1
# for i in range(1,6):
#     #i=1,2,3,4,5
#     space=13
#     for j in range(1,i+1):# 1,6
#         if j==i: # 1 2 3 4 5== 5
#             if k>=10: # 10>=10
#                 space-=1
#         else:
#             if k>=10:# 9>=10
#                 space-=3
#             else:
#                 space-=2 # space=7
#         k+=1 # k=11
#
#     for j in range(1,space+1):
#         print(f'-',end='')
#
#     for j in range(1,i+1):
#         if j==i:
#             print(f'{l}', end='')
#         else:
#             print(f'{l}-', end='')
#         l+=1
#
#

    # print()

#       1           6s  1 0s
#     2   2         4s  2 3s 2
#   3       3       2s  3 7s 3
# 4           4     0s  4 11s 4
#   3       3
#     2   2
#       1

# for i in range(1,5):
#     for j in range(i,4):
#         print(f'  ',end='')
#
#
#     print(f'{i}',end='')
#
#     for j in range(1,(i-1)*4):
#         print(' ',end='')
#
#     if i!=1:
#         print(f'{i}', end='')
#
#     print()
#
# for i in range(3,0,-1):
#     for j in range(i,4):
#         print(f'  ',end='')
#
#
#     print(f'{i}',end='')
#
#     for j in range(1,(i-1)*4):
#         print(' ',end='')
#
#     if i!=1:
#         print(f'{i}', end='')
#
#     print()

# Q-68
# 1     1       0S  1   5S  1
#  2   2        1S  2   3S  2
#   3 3         2s  3   1S  3
#    4          3S  4   0S  4
#   3 3
#  2   2
# 1     1
#
# for i in range(1,5):
#     for j in range(1,i):
#         print(f' ',end='')
#
#     print(f'{i}',end='')
#
#     for j in range(i*2,7):#4*2,7
#         print(' ',end='')# -
#
#     if i!=4:
#         print(f'{i}',end='')
#
#     print()
#
# for i in range(3,0,-1):
#     for j in range(1,i):
#         print(f' ',end='')
#
#     print(f'{i}',end='')
#
#     for j in range(i*2,7):#4*2,7
#         print(' ',end='')# -
#
#     if i!=4:
#         print(f'{i}',end='')
#
#     print()

# Q-69
# 1  2  3  4  5
# 16          6     16 16-10=6
# 15          7     15 15-8 =7
# 14          8     14 14-6 =8
# 13 12 11 10 9

# k = 16
# l = 10
# for i in range(1,6):
#     # i = 1 or
#     if i==1:
#         for j in range(1,6):
#             print(f'{j}  ',end='') # 1 2 3 4 5
#     elif i==5:
#         for j in range(1,6):
#             print(f'{k} ',end='')
#             k-=1
#     else: # 2,3,4
#         for j in range(1,6):
#             if j==1: # 1==1
#                 print(f'{k} ',end='') # 15-
#             elif j==5:
#                 print(f'{k-l}', end='')# 15-8=7
#             else: # 2 3 4
#                 print(f'   ', end='')# 9-
#         k-=1 # k=15
#         l-=2 # l=8
#     print()

# Q-72
# AAAAA
# BBBB
# CCC
# DD
# E

# ch = 65
# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(f'{chr(ch)}',end='')
#     ch+=1
#     print()

# Q-73
# A
# BB
# CCC
# DDDD
# EEEEE
#
# k = ord('A')
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(f'{chr(k)}',end='')
#     k+=1
#     print()

# Q-74
# A
# AB
# ABC
# ABCD
# ABCDE

# k = ord('A')
# for i in range(1,6):
#     k = ord('A')
#     for j in range(1,i+1):
#         print(f'{chr(k)}',end='')
#         k+=1
#     print()

# Q-74
# EDCBA
# EDCB
# EDC
# ED
# E

# for i in range(5,0,-1):
#     k = ord('E')
#     for j in range(1,i+1):
#         print(f'{chr(k)}',end='')
#         k-=1
#     print()

# Q76
# 99999999999
#  9999999999
#   999999999
#    99999999
#     9999999
#      999999
#       99999
#        9999
#         999
#          99
#           9

# n  = int(input())
# ch = input()
# for i in range(n,0,-1):
#     for j in range(n,i,-1):
#         print(' ',end='')
#
#     for j in range(1,i+1):
#         print(f'{ch}',end='')
#
#     if(i!=1):
#         print()

#78]
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# num = 14641
# s=str(num)
# s = ' '.join(s)
# print(s)

# for i in range(5):
#     num = 11 ** i
#     s = str(num)
#     print(' '.join(s))


# Q-79
# 11111
# 10001
# 10001
# 10001
# 11111

# for i in range(1,6):
#     if i == 5 or i == 1:
#         for j in range(1,6):
#             print(f'{1}',end='')
#     else:
#         for j in range(1,6):
#             if j ==1 or j == 5:
#                 print(f'{1}',end='')
#             else:
#                 print(f'{0}',end='')
#
#     print()
#

# @80

# 1                       12    00
# 232                     24    21
# 34543                   36    42
# 4567654                       63
# 567898765                     84


# for  i in range(1,6):
#     k=i
#     for j in range(1,i+1):
#         print(f'{k}',end='')
#         k+=1
#
#     k-=2
#     for j in range(1,i):
#         print(f'{k}',end='')
#         k-=1




    # print()

# num = 1231
# s = str(num)
# s = ' '.join(s)
# print(s)


# Q81]
# 1     1       0S  1   5S  1
#  2   2        1S  2   3S  2
#   3 3         2s  3   1S  3
#    4          3S  4   0S  4
#   3 3
#  2   2
# 1     1
#
# for i in range(1,5):
#     for j in range(1,i):
#         print(f' ',end='')
#
#     print(f'{i}',end='')
#
#     for j in  range(i*2,7):
#         print(f' ',end='')
#
#     if i!=4:
#         print(f'{i}',end='')
#
#     print()
#
# for i in range(3,0,-1):
#     for j in range(1,i):
#         print(f' ',end='')
#
#     print(f'{i}',end='')
#
#     for j in  range(i*2,7):
#         print(f' ',end='')
#
#     if i!=4:
#         print(f'{i}',end='')
#
#
#
#     print()

#
# for i in range(1,5):
#     for j in range(1,5):
#         if j == i:
#             print(f'{i}',end='')
#         else:
#             print(f' ',end='')
#
#     for j in range(3,0,-1):
#         if j == i:
#             print(f'{i}',end='')
#         else:
#             print(f' ',end='')
#     print()
#
#
# for i in range(3,0,-1):
#     for j in range(1,5):
#         if j == i:
#             print(f'{i}',end='')
#         else:
#             print(f' ',end='')
#
#     for j in range(3,0,-1):
#         if j == i:
#             print(f'{i}',end='')
#         else:
#             print(f' ',end='')
#     print()


# Q82]
# 1
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15

# rows = 5
# for i in range(rows):
#     k = i + 1
#     for j in range(i + 1):
#         print(f'{k}', end=" ")
#         k += rows - j - 1
#     print()

# Q-83
#         1             8s      1*2,10
#       1 2 1           6s      2*2,10
#     1 2 3 2 1         4s      2*3,10
#   1 2 3 4 3 2 1       2s      2*4,10
# 1 2 3 4 5 4 3 2 1     0s      2*5,10
#
# for i in range(1,6):
#     for j in range(i,5):
#         print(f'  ',end='')
#
#     for j in range(1,i+1):
#         if i == 1:
#             print(f'{j}', end='')
#         else:
#             print(f'{j} ', end='')
#
#     for j in range(i - 1, 0, -1):
#         if j == 1:
#             print(f'{j}', end='')
#         else:
#             print(f'{j} ', end='')
#
#
#     print()


# Q-84
#       1           6s  1 0s
#     2   2         4s  2 3s 2
#   3       3       2s  3 7s 3
# 4           4     0s  4 11s 4
#   3       3
#     2   2
#       1
#
# for i in range(1,5):
#     for j in range(i,4):
#         print(f'  ',end='')
#     print(f'{i}',end='')
#
#     for j in range(1,(i-1)*4):
#         print(f' ',end='')
#
#     if i!=1:
#         print(f'{i}',end='')
#
#     print()
#
# for i in range(3,0,-1):
#     for j in range(i,4):
#         print(f'  ',end='')
#     print(f'{i}',end='')
#
#     for j in range(1,(i-1)*4):
#         print(f' ',end='')
#
#     if i!=1:
#         print(f'{i}',end='')
#
#     print()



# Q-85
# 99999999999
#  9999999999
#   999999999
#    99999999
#     9999999
#      999999
#       99999
#        9999
#         999
#          99
#           9


# n = int(input('Enter the value of n:'))
# ch = int(input('Enter the value of ch:'))
# for i in range(n,0,-1):
#     for j in range(i,n):
#         print(f' ',end='')
#
#     for j in range(1,i+1):
#         print(f'{ch}',end='')
#
#     if i!=1:
#
#         print()

# Q-86
# *****
# *   *
# *****
#   *
#   *


# for i in range(5,0,-1):
#     for j in range(5,0,-1):
#         if i == 4 or i == 2 or i == 1:
#             if i == 4:
#                 if j == 1 or j == 5:
#                     print(f'*', end='')
#                 else:
#                     print(f' ', end='')
#
#             elif i == 2 or i == 1:
#                 if j != 3:
#                     print(f' ',end='')
#                 else:
#                     print(f'*', end='')
#
#         else :
#             print(f'*',end='')
#
#     print()


# Q-87
# n=5
# *****
# *   *
# *****
#   *
#   *

# n=7
# *******
# *     *
# *     *
# *******
#    *
#    *
#    *

# n = int(input())
# for i in range(0,n):
#     if i == 0 or i==n//2:
#         for j in range(1,n+1):
#             print(f'*', end='')
#
#     elif i>0 and i<n//2:
#         for j in range(1, n + 1):
#             if j == 1 or j == n:
#                 print(f'*', end='')
#             else:
#                 print(f' ', end='')
#
#     else :
#         for j in range(0,n//2+1):
#             if j == n//2:
#                 print(f'*', end='')
#             else:
#                 print(f' ', end='')
#
#     print()


# Q-88
# n=5
#   *
#   *
# *****
# *   *
# *****


# n=7
#    *
#    *
#    *
# *******
# *     *
# *     *
# *******


# n = int(input())
# for i in range(0,n):
#     if i == n//2 or i==n-1:
#         for j in range(1,n+1):
#             print(f'*', end='')
#
#     elif i>n//2 and i<n:
#         for j in range(1, n + 1):
#             if j == 1 or j == n:
#                 print(f'*', end='')
#             else:
#                 print(f' ', end='')
#
#     else :
#         for j in range(0,n//2+1):
#             if j == n//2:
#                 print(f'*', end='')
#             else:
#                 print(f' ', end='')
#
#     print()

# Q-89
# n=5
# ***
# * *
# * ***
# * *
# ***

# n=7
# ****                  0
# *  *                  1
# *  *                  2
# *  ****               3
# *  *                  4
# *  *                  5
# ****                  6
#
# n = int(input())
# for i in range(0,n):
#     if i == 0 or i == n-1:
#         for j in range(0,n//2+1):
#             print(f'*',end='')
#
#     else:
#         for j in range(0,n//2+1):
#             if j == 0 or j == n//2:
#                  print(f'*',end='')
#             else:
#                 print(f' ', end='')
#
#
#         if i == n//2:
#             for j in range(0,n//2+1):
#                 print(f'*', end='')
#
#     print()


# Q90]

# * * * * *
# * * 1 * *        3
# * 1 2 3 *       234
# 1 2 3 4 5      12345
# * * * * *

# for i in range(0,5):
#     if i == 0 or i == 4:
#         for j in range(0,5):
#             if j == 4:
#                 print(f'*', end='')
#             else:
#                 print(f'* ',end='')
#
#     else:
#         # i = 1  2s
#         # i = 2  1s
#         # i = 3  0s
#         for j in range(i,3):
#             print(f'* ',end='')
#
#         for j in range(1,i*2):
#             if j == 5:
#                 print(f'{j}',end='')
#             else:
#                 print(f'{j} ',end='')
#
#
#         for j in range(i,3):
#             if j == 2:
#                 print(f'*', end='')
#             else:
#                 print(f'* ',end='')
#
#     print()

############################# Pattern end
# if else
# nested if else
# and or
# loops
# break continue
# company  level

############################# session 23
#operators
# Arithmatic  (* / % + -)
# comparison (< > <= >= == !=)
# assignment (=)
# logical  (and or not)
# bitwise (& | ^ <<  >>)
# membership
# indentity (is is not)


# membership operation - konsa bhi data search karne ka ' 1] in 2]not in'

# t = (101,'Manish','Kumar',5.6,55,'ASM','C','DS','CPP')
# print(t)
# print('Kumar' in t)  #true
# print('Kumar' not in t)  #false
# print('KUmar' in t)  #False
# print('KumAr' not in t)  #false

# L = [101,'Manish','Kumar',5.6,55,'ASM','C','DS','CPP']
# print(L)
# print('Kumar' not in L)
# print('Kumar'  in L)
# print('KuMar' not in L)
# print('KuMar'  in L)
#
# d = { 'name':'Manish' , 'age':20 , 5.6:'height' , 'college':'ASM' , 'classes1' : ['C','DS','CPP'] , 'classes2' : ('Java','Python','DB')}
# print(d)
# print('name' in d)# T
# print('age' in d)# T
# print(5.6 in d)# T
# print('name' not in d)# F
# print('Manish' in d) # Only Check Key F
# print(d['name']) # Manish
# print(d['age'])  #20
# print(d['Name']) # Error throw = exception throw


# if 'name' in d:
#     print(d['name'])
# else:
#     print('Key is not found!!!')

#
# s = 'VowTech IT TC'
# print('TC' in s)          #true
# print('Tc' in s)          #false

# a1 = 10
# b1 = 10
# print(a1  is b1)       #true
# print(a1  is not b1)  #false

# Same for float and string
# String tuple is immutable whose  value cannot be change
# mutable = changeble

# a1=10
# b1=10
# print(a1 is b1)
# print(a1 is not b1)
#
# a1=10.23
# b1=10.23
# print(a1 is b1)
# print(a1 is not b1)
#
# a1='VowTech'
# b1='VowTech'
# print(a1 is b1)
# print(a1 is not b1)
#
# a1=(10,20)
# b1=(10,20)
# print(a1 is b1)
# print(a1 is not b1)
#
# a1=[10,20]
# b1=[10,20]
# print(a1 is b1) # False
# print(a1 is not b1)# True

# list is changeble

# a1 = {1:'ONE',2:'TWO'}
# print(a1)
# a1[3]='THREE'
# print(a1)
# a1[2]='two'
# print(a1)
# del a1[2]
# print(a1)

# dictionary is changeble

# d = { 'name':'Manish' , 'age':20 , 5.6:'height' , 'college':'ASM' , 'classes1' : ['C','DS','CPP'] , 'classes2' : ('Java','Python','DB')}
# print(d)
# d[5.6] = 'weight'
# print(d)
# d['classes2'] = ('Java','SQL','CPP')
# print(d)
# d['Surname'] = 'Dhotre'
# print(d)
# del d['Surname']
# print(d)

# dictionary is changeble mutable
# you can add further like surname

# a1 = {1:'ONE',2:'TWO'}
# b1 = {1:'ONE',2:'TWO'}
# print(a1 is b1) # False
# print(a1 is not b1)# True

# Summary : tuple and string are non-mutable and dict and list are mmutable



#ternary operator
# Python
# Ternary operator:
# [on_true] if [expression] else [on_false]
# [True] if Condition else [False]

# a,b = 101 ,20
# max = a if a>b else b
# print(max)

# a,b = 10,20
# if a>b:
#     max = a
# else:
#     max = b
# print(max)


# a,b,c = 2945 , 2011 , 2034
#
# if a > b:
#     if a>c:
#         max = a
#     else:
#         max = c
# else:
#     if b>c:
#         max = b
#     else:
#         max = c
#
# print(max)

# a,b,c = 2945 , 3811 , 203
# if a>b and a>c:
#     max =a
# elif b>a and b>c:
#     max = b
# elif c>a and c>b:
#     max = c
# print(max)
#
# a,b,c = 2945 , 3811 , 203
# if a>b and a>c:
#     max =a
# else:
#     if b>c:
#         max = b
#     else:
#         max = c
# print(max)

# a,b,c = 2945 , 3811 , 203
# max = a if a>b else b
# max = max if max>c else c
# print(max)

# a , b , c = 100 , 20 , 30
# max = (a if a>c else c)  if a>b  else (b if b>c else c)
# print(max)

# a , b , c = 100 , 20 , 30
# max =a if a>b and a>c else (b if b>c else c)
# print(max)


# a , b , c = 100 , 20 , 30
# m = max(a,b,c)
# print(m)
# m = min(a,b,c)
# print(m)

# l  = [23,43,31,23,45,43]
# m = min(l)
# print(m)
#
# l = [43,31,23,45,43]
# m = max(l)
# print(m)

#literable objects
# l  = [23,43,31,23,45,43]
# for a in l:
#     print(a)


# l  = [23,43,31,23,45,43]
# s = sum(l)
# print(s)
# s = sum(l,55)
# print(s)
# s = sum(l,55.55)
# print(s)
# s = sum(l,55 , 55) #TypeError: sum() takes at most 2 arguments (3 given)
# print(s)


# a,b = 100,200
# print( (b,a) [a>b])  #max nikal ne ka feature
#     #(false,true)
# print({True: a, False: b} [a>b])  #sequence matter nnhi karega
# print({False: b, True: a} [a>b])  #sequence matter nnhi karega
# print((lambda:b, lambda:a)[a>b]())


# a,b = 1000,1000
# print("Both a and b are equal" if a==b else "a is greater then b" if a>b else "b is greater than a")
#
# print(f"Both {a} and {b} are equal" if a==b else f"{a} is greater then {b}" if a>b else f"{b} is greater than {a}")


# a,b = 100,110
# if a!=b:
#     if a>b:
#         print(f'{a} is greater then {b}')
#     else:
#         print(f'{b} is greater then {a}')
# else:
#         print(f'{a} is equal to {b}')

# summary
# string and tuple are non mutable
# dictinary and list are mutable



############################# session 24
#aptitude - New
# m=1
# a = [2,1,2,1]
# for j in range(1,4): # j=1,2,3
#     # if (( 2 & a[3-1] & 1)>3):
#     # if (( 2 & a[2] & 1)>3):
#     # if (( 2 & 2 & 1)>3):
#     # 10
#     # 10
#     # 01
#     # --
#     # 00 0
#     # if (0 > 2 ):
#     if (( 2 & a[j-1] & 1)>j):
#         m=m+a[j]
#     m=m+1 #m=4
# print(m) #4


#break statement
#rules - only and only loop


# if 1:
#     break

# i = 1
# # while i<=10:
#     print(i,end='\t')
#     i+=1
# print(f'\nR {i}')


# i=1
# while i<=10:      # 1 2 5<=10
#     if i==6:      # 1 2 3 4 5==5
#         break
#     print(i,end='\t')   # 1 2 3 4
#     i+=1# i=5
#
# print('\nOut Of Loop')
# print(f'R {i}')    # 5


#
# for i in range(1,11):      # 1 2 5<=10
#     if i==9:      # 1 2 3 4 5==5
#         break
#     print(i,end='\t')   # 1 2 3 4
# print('\nOut Of Loop')
# print(f'R {i}')    # 5



# i=1
# while i<=10:      # 1 2 5<=10
#     if i==15:      # 1 2 3 4 5==5
#         break
#     print(i,end='\t')   # 1 2 3 4
#     i+=1# i=5
# else:
#     print()
#     print('ALL STATEMENT ARE EXECUTED')
# print('\nOut Of Loop')



#prime number
# n = int(input('Enter the number:'))
# i = 2
# while i < n:
#     if n%i == 0:
#         break
#     i+=1
#
# if n==i:
#     print('it is pn')
# else:
#     print('it is not npn')




# n = int(input('Enter the Number:'))
# i = 2
# while i<n:
#     print(f'{n}%{i} = {n%i}')
#     if n%i == 0 :
#         break
#     i+=1
#
# if n == i :
#     print(f'{n} is Prime Number')
# else:
#     print(f'{n} is not Prime Number')




# n = int(input('Enter the Number:'))
# i = 2
# flag = True
# while i<=n//2:
#     print(f'{n}%{i} = {n%i}')
#     if n%i == 0 :
#         flag = False
#         break
#     i+=1
#
# if flag :
#     print(f'{n} is Prime Number')
# else:
#     print(f'{n} is not Prime Number')


# n = int(input('Enter the Number:'))
# i = 2
# flag = True
# while i<=n//2:
#     print(f'{n}%{i} = {n%i}')
#     if n%i == 0 :
#         flag = False
#         break
#     i+=1
#
# if flag and n > 1 :
#     print(f'{n} is Prime Number')
# else:
#     print(f'{n} is not Prime Number')



# num = int(input('Enter Number : '))
#
# if num<=1:
#     print(f'{num} is NPN')
# else:
#
#     for i in range(2 , num//2+1 ):# 2,3,
#         if num%i==0: # 7%3 1==0
#             print(f'{num} is NPN')
#             break
#     else:
#         print(f'{num} is PN')



# n = int(input())
# i = 2
# flag = True
# while i<n//2:
#     print(f'{n}%{i}={n%2}')
#     if n%i == 0:
#         flag = False
#         break
#     i+=1
#
# if flag and n>1 :
#     print(f'{n} is the prime number')
# else:
#     print(f'{n} is the not prime number')



#
# n = int(input('Enter the number:'))
# if n<=1:
#     print(f'{n} is not a Prime number')
#
# else:
#     for i in range(2,n//2+1):
#         if n%i == 0:
#             print(f'{n} is not a Prime Number')
#             break
#
#     else:
#         print(f'{n} is a Prime number')




# #1.....10 PN NPN
# for n in range(1,11):
#     i = 2
#     flag = True
#     while i<=n//2:
#         # print(f'{n}%{i}={n%2}')
#         if n%i == 0:
#             flag = False
#             break
#         i+=1
#
#     if flag and n>1 :
#         print(f'{n} is the prime number')
#     else:
#         print(f'{n} is the not prime number')




# n  = int(input('Enter the Range: '))
# for n in range(1,n+1):
#     i = 2
#     flag = True
#     while i<=n//2:
#         # print(f'{n}%{i}={n%2}')
#         if n%i == 0:
#             flag = False
#             break
#         i+=1
#
#     if flag and n>1 :
#         print(f'{n} is the prime number')
#     else:
#         print(f'{n} is the not prime number')
#


#
# sumpn , sumnpn = 0 , 0
# for num in range(1,11):
#     i=2
#     flag = True
#     while i <= num//2 :
#         if num%i==0:
#             flag = False
#             break
#         i+=1
#
#     if flag and num>1:
#         sumpn+=num
#     else:
#         sumnpn+=num
#
# print(sumpn)
# print(sumnpn)
#
# if sumpn>sumnpn:
#     print(sumpn-sumnpn)
#
# else:
#     print(sumnpn-sumpn)


#
# x=0
# while x<3:#0 1 2 3 <3
#     x+=1# x=3
#     print(x,end=' ')# 1 2 3
# else:
#     print('Else Block')

# t=(11,22,33,44)
# for v in t:
#     print(v)

# t= 11,22,33,44
# print(type(t))
# for v in t:
#     print(v)


# p,q = 2,3
# for r in range(3,7):
#     p = p + (p&q)
#     if (q^p > r&q):
#         break
#     q = q + (q^p)
# print(p+q)


# s,k=0,0
# a = [ [9,2],[3,6]]
# for j in range(4):
#     s = s + a[j][k]
#     k+=1
#     if j == 1:
#         break
# print(s)


# a,b,c,d=1,0,6,7
# for i in range(4):
#     #i=0,1,2,3
#     if a or b or (c and d): # 5 or
#         print(a) #
#         a = a + 1 #6
#     if a == 2:# 6==2
#         print(a)
#         a = a + 1 #3
#     if a ==1: # 6==1
#         break
# print('journey')



# a,b,c=0,8,10
# for c in range(3,8):
#     b=11+a
#     if ((c+5)>(a-c)):
#         break
#     else:
#         c=(a+6)+b
# print(a+b)


# if 1:
#     print('Yess')
# else:
#     pass
#
# print('R1')
# print('R2')
# print('R3')


# while 1:
#     pass
#     break
# print('R1')
# print('R2')
# print('R3')

#Break = exit
#Continue = Loop cintinue

# i=0
# while i<10: # 0 1 2 3 4 <10
#     i+=1 #i=5
#     if i==5:# 1 2 3 4  5== 5
#         break
#     print(i,end='\t')# 1 2 3 4

#
# i=0
# while i<10: # 0 1 2 3 4 <10
#     i+=1 #i=5
#     if i==5:# 1 2 3 4  5== 5
#         # print(f'{i} SKIPP')
#         continue
#     print(i,end='\t')# 1 2 3 4

#
# i=1
# while i<=10: # 1 2 3 4 5 5 <=10
#     if i==5:#1 2 3 4 5== 5
#         print('VowTech')
#         continue
#     print(i,end='\t')# 1 2 3 4 VowTech VowTech.....
#     i+=1 # i=5


# i=1
# while i<=10: # 1 2 3 4 5 5 <=10
#     if i==5:#1 2 3 4 5== 5
#         print('VowTech')
#         i+=1
#         continue
#     print(i,end='\t')# 1 2 3 4 VowTech VowTech.....
#     i+=1

# for i in range(1,5):
#     if  i == 3:
#         continue
#     print(i)


#SET
# set
# Automatically Remove Duplicates Elements!!!
# Set- Remove Duplicates { Value1,Value2 ,... ,ValueN }
# Order -  unOrder
# No Index


# s = { 11,11,22,11,22,10 , 20,10,20,10,10,10,20,20 }
# print(s)
# print(type(s))

# s = {"Sayali","Tanishka","Sayali","Sayali","Tanishka","Tanishka","Tanishka","Archana"}
# print(s)
# print(type(s))
# # print(s[0]) #error
# # print(value) #error
# for value in s:
#     print(value)  #Sayali Tanishka Archana


# s = 'Vaibhav'
# print(s)
# print(type(s))
# print(s.ljust(15))
# print(s.ljust(15,'*'))
# print(s.rjust(15,'-'))

# s = '        Vaibhav       '
# print(s)
# print(type(s))
# print(len(s))
# s = s.lstrip()
# print(s)
# print(len(s))
#
# s = '        Vaibhav       '
# print(s)
# print(type(s))
# print(len(s))
# s = s.rstrip()
# print(s)
# print(len(s))
#
# s = '        Vaibhav       '
# print(s)
# print(type(s))
# print(len(s))
# s = s.strip()
# print(s)
# print(len(s))


# s = 'Vaibhav Anil Dhotre'
# print(type(s))
# print('##############Before Partition##############')
# print(s)
# print('##############after Partition################')
# print(s.partition('Anil'))

# s = 'Vowtech IT TC'
# print(s.replace('IT','it'))
# print(s.replace('IT','ITOC'))
# print(s.replace('IT',''))

# s = 'Vowtech\nIT\nTC'
# print(s.splitlines())

# s = 'Vowtech IT TC'
# print(s.swapcase())

# s = 'Vowtech'
# print(s.zfill(15))


# s = 'Vowtech'
# print(s.partition('w'))
# print(len(s))


# Input =
# test_str = 'VowtechItVowtech-is-best-for-Vowtech'
# Output =
# test_str = 'VowtechItVowtech-is-best-for-'

# s = 'VowtechItVowtech-is-best-for-Vow-te-ch'
# i = s.rindex('-')
# print(i)
# print(s[ :i+1])

# input =>
# s = 'Google.com'
# Output =>
# each letter with index

# s1 = 'Google.com'
# s2 = set(s1)
# print(s2)
#
# s= 'Vaibhav'
# print(s.ljust(15))
# print(s.rjust(15))

# s= '       Vaibhav         '
#
# print(s.lstrip())
# print(s.rstrip())
# print(s.strip())

# s = 'Vowtech IT TC'
# print(s.partition('IT')) #TUPLE
# print(s.replace('IT','it')) #TUPLE

# s = 'Vowtech\nIT\nTC'
# print(s.splitlines()) #list dega

# s = 'Vowtech IT TC'
# print(s.swapcase())

# s = 'Vowtech'
# print(s.zfill(15))

#Write a python progrmme to find lenght of a string
# s = 'Vaibhav'
# print(len(s))

# s = 'Vowtech'
# len = 0
# for i in s:
#     len+=1
# print(len)


#Input =
# test_str = 'VowtechItVowtech-is-best-for-Vowtech'
#Output =
# test_str = 'VowtechItVowtech-is-best-for-'

# s = 'VowtechItVowtech-is-best-for-Vowtech'
# i = s.rindex('-')  #last index degs '-' ka and index will give index of 1st occurance
# print(i)
# print(s[:i+1])
#
# i = 0
# for ch in s:
#     i+=1
#     if ch == '-':
#         k = i
# print(s[:k])
#
# i = 0
# for ch in s:
#     i+=1
#     if ch == '-':
#         break
# k = i
# print(s[:k])




# input =>
# s = 'Google.com'
# Output =>
# each letter with index

#1st logic
# s = 'Google.com'
# s1 = set(s)
# print(s1)
# d = {}
# for ch in s1:
#     cnt = s.count(ch)
#     d[ch] = cnt
#
# print(d)


# 2nd logic
# s1 = 'google.com'
# d = {}
# for ch in s1:
#     if ch in d:
#         d[ch]+=1
#     else:
#         d[ch] = 1
#
# print(d)


# n = input('Enter the string: ')
# print(f' "{n}" is your Entered String')
#
# if len(n) >1:
#     print(n[:2]+n[-2:])
# else:
#     print('SORRY')


# s = 'restartre'
# output = s[0]
# for ch in s[1:]:
#     if ch == s[0]:
#         output += '$'
#     else:
#         output+=ch
#
# print(output)


# s = 'restartre'
# # print(s[0] + s[1:].replace('r','$'))
# s = s[0]+s[1:].replace('r','$')
# print(s)


# s1,s2 = 'abc', 'xyz'
# output = s2[:2]+s1[2:] + ' ' +s1[:2]+s2[2:]
# print(output)


# s = input('Enter the string')
#
# if len(s) >=3:
#     if 'ing' not in s :
#         print(s+'ing')
#     else:
#         print(s+'ly')
# else:
#     print(s)


# s = 'The lyrics is not that poor!'
# if 'not that poor' not in s:
#     print(s)
# else:
#     print(s.replace('not that poor','good'))


# s = 'vowtech'
# a = '123'
# print(s.isnumeric())
# print(a.isnumeric())

# s = " "
# print(s.isspace())
# s = 'a'
# print(s.isspace())


# s = 'Vowtech IT TC'
# print(s)
# print(s.title())
# print(s.istitle()) #false

# s = 'Vowtech It Tc'
# print(s.istitle())  #true

# join vvvvimp

# l = ['11','12','14','15','16']
# s = ' '.join(l)
# print(s)
# print(type(s))

# l = ['11','12','14','15','16']
# s = '$'.join(l)  #11$12$14$15$16
# print(s)
# print(type(s))

# l1 = []
# l = [11,12,13,14,15]
# for value in l:
#     l1.append(str(value))
# print(l1)
# s = ' '.join(l1)
# print(s)

# s = 'vaibhav Diksha'
# l = s.split( )
# print(l)

# s = 'vaibhav Diksha'
# l = s.split('$')
# print(l)


#
# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

# l = ['Vowtech', 'Php' , 'Vaibhav' , 'Cpp']
# max = len(l[0])
# output = l[0]
# for value in l[1:]:
#     m = len(value)
#     if m>max:
#         max = m
#         output = value
#
# print(f'Longest word : {output}')
# print(f'Lenght of the longest word : {max}')

#2nd logic
# l = ['Vowtech', 'Php' , 'Vaibhav' , 'Cpp']
# output = max(l)
# print(f'Longest word : {output}')
# print(f'Lenght of the longest word : {len(output)}')



#9. Write a Python program to remove the nth index character from a nonempty string.

# n = input('Enter the string: ')
# x = int(input('Enter the nth index to remove: '))
# print(n[0:x]+n[x+1:])


# 10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

# s = 'abcd'        #dbca
# s1 = s.replace('a','d')  #dbcd
# s2 = s.replace('d','a')  #abca
# print(s1[:2]+s2[2:])


# 11. Write a Python program to remove characters that have odd index values in a given string.
# s = 'String'
# #s t r i n g
# #0 1 2 3 4 5
# print(s[::2])  #even index
# print(s[1::2]) #odd index

# #even
# s = 'Vowtech It TC'
# for i in range(len(s)):
#     if i%2==0:
#         print(s[i],end='')

# #ODD
# s = 'Vowtech It TC'
# for i in range(len(s)):
#     if i%2!=0 :
#         print(s[i],end='')


# 12. Write a Python program to count the occurrences of each word in a given sentence.

# s = 'Python is object oriented language and java is also object oriented language vowtech it tc is object '


# l = s.split()
# print(l)
# d={}
# for word in l:
#     if word not in d:
#         d[word] = s.count(word)
#         print(f'{word}:{d[word]}')


# s = 'Python is object oriented language and java is also object oriented language vowtech it tc is object '
#
# l = s.split()
# d = {}
# for word in l :
#     if word in d:
#         d[word]+=1
#     else:
#         d[word] =1
#
# print(d)


#13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
#
# n = input('Enter the string: ')
# print(f'Uppercase = {n.upper()}')
# print(f'Lowercase =  {n.lower()}')


# 14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

# s = 'red, white, black, red, green, black'
# l = s.split(', ')
# print(l)
# s1 = set(l)
# print(s1)


# s = 'red, white, black, red, green, black'
# l =set(s.split(', '))
# print(l)


#string = list => split() function
#list = string => join() function
#sorted hame list dega

# s = 'red, white, black, red, green, black'
# l = ', '.join(sorted(set(s.split(', '))))
# print(l)


# s = 'red, white, black, red, green, black'
# l = set(s.split(', '))
# print(l)



# 15. Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>

# n = input('Enter the string: ')
# tag = input('Enter the tag: ')
# print(f'<{tag}>{n}</{tag}>')


# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

# p = '<<>>'
# n = input('Enter the string: ')
# print(p[:2],f'{n}',p[2:])


# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

#
# s = input('Enter the string: ')
# if len(s) >= 2:
#     print(len(s))
#     print( (s[len(s)-2:])*4 )
# else:
#     print('Quection bagh jara yekda')


# 18. Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt

# s = input('Enter the  string: ')
# if len(s) >= 3:
#     print(f'{s} => {s[:3]}')
# else:
#     print('Sorry')


# 19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python


# s = 'https://www.w3resource.com/py-thon-exercises'
# i = s.rindex('-')
# print(i)
# print(s[:i])


# 20. Write a Python function to reverse a string if its length is a multiple of 4.

# s = input('Enter the string: ')
# if len(s)%4==0:
#     print(s[::-1])
# else:
#     print()


# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

# s = 'VAibhav'
# cnt = 0
# for ch in s[:4]:
#     if ch.isupper():
#         cnt+=1
#
# if cnt>=2:
#     print(s.upper())
# else:
#     print(s)


# 22.Write a Python program to sort a string lexicographically.
# s = 'w3resource'
# l = sorted(s)
# print(l)
# s = ''.join(l)
# print(s)


# 23. Write a Python program to remove a newline in Python

# s = 'Vowtch IT\n PCMC\n 411044'
# l = s.splitlines()
# print(l)
# for value in l:
#     print(value,end='')


# 24. Write a Python program to check whether a string starts with specified characters.

# s = 'Vaibhav'
# ch = s[:1]
# print(s.startswith(ch))   #True


################################################# Function
# def funchtionName():
#     statement1
#     statement1
#     statement1
#     .
#     .
#     statementn

# def manish(): #define funtion
#     print('work1')
#     print('work2')
#     print('work3')
#
# print('Main-1')
# manish()  #call function
# print('Main-2')
# manish()
# print('Main-3')
# manish()


# number 1 , number 2 = Parameters/Arguments
# def addition(number1 ,number2):
#     print(f'{number1}+{number2}={number1+number2}')

# addition(11,34)
# print('Complete!!!!!')

# def addition(num1,num2):
#     return num1+num2
#
# num1 = int(input('Enter Num1:'))
# num2 = int(input('Enter Num2:'))
# sum = addition(num1,num2)
# print(sum)
# print(f'{num1}+{num2}={addition(num1,num2)}')

#call by value
# def func(t):
#     print(f'In func : {t}')
#     t = t * 2
#     print(f'In func : {t}')
#
# if __name__ == '__main__':
#     t = ('Vaibhav', 'Anil', 'Dhotre')
#     print(f'In main : {t}')
#     func(t)
#     print(f'In main : {t}')


#string
# def func(s):
#     print(f'In func : {s}')
#     s = s * 2
#     print(f'In func : {s}')
#
# if __name__ == '__main__':
#     s = 'Vaibhav'
#     print(f'In main : {s}')
#     func(s)
#     print(f'In main : {s}')    #immutable aslya mule same yeil

# def func(l):
#     print(f'In func : {l}')
#     l.append('Manish')
#     print(f'In func : {l}')
#
# if __name__ == '__main__':
#     l = ['Vaibhav', 'Dhotre']
#     print(f'In main : {l}')
#     func(l)
#     print(f'In main : {l}')    #immutable aslya mule same yeil


#Required arguments

# def fullname(fn,mn,ln):
#     print(f'{fn} {mn} {ln}')
#
# # fullname('Vaibhav') #missing 2 required positional arguments: 'mn' and 'ln'
# fullname('Vaibhav','Anil','Dhotre')


#Keywords arguments

# def fullname(fn,mn,ln):
#     print(f'{fn} {mn} {ln}')
#
# if __name__ == '__main__':
#     firstname = 'Vaibhav'
#     middlename = 'Anil'
#     lastname = 'Dhotre'
#     # fullname(firstname,middlename,lastname)
#     # fullname(middlename,lastname,firstname)  #call but output wrong
#     # fullname(mn=middlename, ln= lastname, fn = firstname) #Vaibhav Anil Dhotre
#     fullname(firstname, ln=lastname, mn=middlename) #correct
#     fullname(mn=middlename, ln=lastname, firstname) #correct


# def simple_interest(p,t,r):
#     return (p*t*r)/100
#
# print('Simple Interest', simple_interest(10,10,1900))
# print('Simple Interest', simple_interest(t=10.2,r=10.3,p=10))
# print('Simple Interest', simple_interest(time = 10, rate = 10.2, p = 1900))
#keywords do not matches



#default arguments
# def fullname(fn,mn = 'Anil',ln ='Dhotre'):
#     print(f'{fn} {mn} {ln}')
#
# fullname('Vaibhav',mn='Anilkumar',ln='Dhotre')
# fullname(mn='Anilkumar',ln='Dhotre','Vaibhav') #error



#vaiable lenght argument

# def func(*args):
#     print(f'Call Ok : {args}')
#
# func()
# func(10,29)
# func(23,32,12)

# def func(cn, *args):
#     print(f'Company name = {cn} Call Ok : {args}')
#
# # func() #error
# func('Vowtech',10,29)
# func('Vowtech',23,32,12)


# def func(*args,cn):   #wrong
#     print(f'Company name = {cn} Call Ok : {args}')
#
# # func() #error
# func(10,29,'Vowtech')
# func('Vowtech',23,32,12)


# def func(*num):
#     return sum(num)
#
# print(func(10,20,30)) #60
# print(func()) #0


# i = 20 #global variable
# def func():
#     i = 10      #local variable
#     print(f'In func:{i}')
#
# if __name__ == '__main__':
#     print(f'In main:{i}')
#     func()



# i = 10  #globsl variable
# def func():
#     print(f'In function:{i}')
#     i+=20
#
# if __name__ == '__main__':
#     print(f'In main:{i}')
#     func()

#To change the global var in funtion
# i = 10  #globsl variable
# def func():
#     global i
#     print(f'In function:{i}')
#     i+=20
#     print(f'In function:{i}')
#
# if __name__ == '__main__':
#     print(f'In main:{i}')
#     func()


# x = 1000
# def vowtech():
#
#     x = 20
#     def rohan():
#         global x  #1000
#         print(f'In rohan()',x)
#         x = 88
#         print(f'In rohan()',x)
#
#     print(f'Before calling rohan()',x)
#     rohan()
#     print(f'after calling rohan()',x)
#
# print(f'In main ',x) #1000
# vowtech()
# print(f'In main',x) #88

#
# def func(*args,**kwargs):
#     print(f'First argument:{args}',{type(args)})
#     print(f'Second argument:{kwargs}',{type(kwargs)})
#
# l = [10,20,34,43]
# d = {'1':20,'2':30,'3':40,'4':50,}
# func()
# func(*l)
# func(**d)


# def func(cv,*args,**kwargs):
#     print(f'First argument:{cv}',{type(cv)})
#     print(f'Second argument:{args}',{type(args)})
#     print(f'Third argument:{kwargs}',{type(kwargs)})
#
# cv = 'Vowtech'
# l = [10,20,34,43]
# d = {'1':20,'2':30,'3':40,'4':50,}
#
# func(cv,*l, **d)


# def func(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact *= i
#     return fact
#
#
# if __name__ == '__main__':
#     num = int(input('Enter the number: '))
#     fact = func(num)
#     print(f'Factrial of {num} is {fact}')


# #Recursion function
# if __name__ == '__main__':
#     num = int(input('Enter the number: '))
#     rev = 0
#     temp = num
#     while temp > 0:
#         r = temp % 10
#         rev = rev * 10 + r
#         temp //= 10
#     print(f'{num},{rev}')
#     if num == rev:
#         print(f'{num} is palindrme')
#     else:
#         print(f'{num} is not palindrome')



#####################session 32
# Palindrome logic:
#
# num = int(input('Enter the number :'))
# temp = num
# rev =0
# while temp>0:
#     r = temp % 10
#     rev = rev*10+r
#     temp = temp//10
#
# if rev == num:
#     print(f'{num} is a palindrme')
# else :
#     print(f'{num} is not palindrome')


#Palindrome using function
# def ispalindrome(num):
#     temp = num
#     rev = 0
#     while temp > 0:
#         r = temp % 10
#         rev = rev * 10 + r
#         temp = temp // 10
#
#     if rev == num:
#         print(f'{num} is a palindrme')
#     else:
#         print(f'{num} is not palindrome')
#
#     print(f'Reverse of {num} is {rev}')
#
#
# if __name__ == '__main__':
#     num = int(input('Enter any key: '))
#     ispalindrome(num)




# Palindrome using recursion function
# def ispalindrome(rev, temp,num):
#     if temp > 0:
#         r = temp % 10
#         rev = rev * 10 + r
#         temp = temp // 10
#         return ispalindrome(rev, temp, num)
#
#
#     if rev == num:
#         return True
#     return False
#
#
# if __name__ == '__main__':
#     num = int(input('Enter any key: '))
#     if ispalindrome(0,num,num):
#         print(f'{num} is palindrome')
#     else:
#         print(f'{num} is not palindrome')

'''
def ispalindrome(rev, temp,num):
    if temp > 0:
        r = temp % 10
        return ispalindrome(rev * 10 + r, temp // 10, num)
    if rev == num:
        return True
    return False


if __name__ == '__main__':
    num = int(input('Enter any key: '))
    if ispalindrome(0,num,num):
        print(f'{num} is palindrome')
    else:
        print(f'{num} is not palindrome')
'''

#Armstrong number

# if __name__ == '__main__' :
#     num = int(input('Enter any key: '))
#     temp = num
#     sum = 0
#     power =len(str(num))
#     while temp>0:
#         r = temp % 10
#         sum = sum + r**power
#         temp //= 10
#
#     if sum == num:
#         print(f'{num} is an armstrong number')
#     else:
#         print(f'{num} is not armstrong number')


#Using function

# def isarmstrong(num):
#     temp = num
#     sum = 0
#     power = len(str(num))
#     while temp > 0:
#         r = temp % 10
#         sum = sum + r ** power
#         temp //= 10
#
#     if num == sum:
#         return True
#     return False
#
# if __name__ == '__main__':
#     num = int(input('Enter any key: '))
#     if isarmstrong(num):
#         print(f'{num} is armstrong number')
#     else:
#         print(f'{num} is not armstrong number')


#using recursion
# def isarmstrong(sum,temp,num):
#     power = len(str(num))
#     if temp > 0:
#         r = temp % 10
#         sum = sum + r ** power
#         temp //= 10
#         return isarmstrong(sum,temp,num)
#
#     if num == sum:
#         return True
#     return False
#
# if __name__ == '__main__':
#     num = int(input('Enter any key: '))
#     if isarmstrong(0,num,num):
#         print(f'{num} is armstrong number')
#     else:
#         print(f'{num} is not armstrong number')


##############Built  in function

# # a = -10
# # print(abs(a))  #10
#
# a = [10,23,32,21]
# print(all(a))   #true
#
# a = [0,True,12]
# print(all(a)) #false
#
# a = [1,23,21,False]
# print(all(a))  #false
#
# a = [1,23,21,True]
# print(all(a))   #true
#
# k = [0,False,1]
# print(any(k))    #true
#
# k = [False,0]
# print(any(k))   #false
#
# a = 14
# k = bin(14)
# print(k[2:])
# print(type(k))

# a = 14
# k = bin(14).replace('0b',"")
# print(k)
# print(type(k))
#
# a = []  false
# print(bool(a))


# def vowtech():
#     return 5
#
# x = vowtech
# print(x)
# print(callable(x)) #false
# print(callable(vowtech))  #true
# print(callable(bin))

# l = [1,3,2,3,4]
# for value  in l:
#     print(value)

# l = [1,3,2,3,4]
# it = iter(l)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) #error


# l = list(map(int , input().split()))
# print(l)
#output
# 1 2 3 4 5 6
# [1, 2, 3, 4, 5, 6]

# l = list(map(str , input().split()))
# print(l)
# output
# 1 2 4
# ['1', '2', '4']

# l = list(map(int,input().split()))
# print(l)
#
#
# #Python Filter()
# def filterdata(x):
#     if x > 5:
#         return x
#
# result = filter(filterdata,(7,1,2,6))
# print(list(result))   #[7, 6]
#
# #using map()
# def filterdata(x):
#     if x > 5:
#         return x
#
# result = map(filterdata,(7,1,2,6))
# print(list(result))  #[7, None, None, 6]
#
#
# def filterinput(x):
#     if x > 5:
#         return x
#
# result = filter(filterinput,(4,3,6,7,5,7,1))
# print(list(set(result)))  #[6, 7]

# def filterages(x):
#     if x > 15:
#         return x
#     else:
#         return None
#
# output = filter(filterages,[12,23,23,12,34,54,21])
# print(list(output))


# result = hex(132)
# result1 = oct(132)
# print(result)
# print(result1)


# s = "vvaiibbhhaav"
# s = sorted(s)
# print(s)
# l = ''.join(s)
# print(l)
# a = set(l)
# print(a)

# print(pow(4,2))

# print(list(range(0,12)))

#reversed function()
# s = 'Vaibav'
# print(list(reversed(s)))

# t = (12,21,22,34,21,17)
# print(list(reversed(t)))

# #Plaindrome
# def is_palindrome(num):
#     # Convert the number to a string
#     num_str = str(num)
#     reversed_num_str = ''.join(reversed(num_str))
#     if num_str == reversed_num_str:
#         return True
#     else:
#         return False
#
# num = int(input('Enter any key: '))
# if is_palindrome(num):
#     print(num, "is a palindrome.")
# else:
#     print(num, "is not a palindrome.")


# def Table(x):
#     return lambda i : num*i
#
# num = 10
# t = Table(num)
#
# for i in range(1,11):
#     print(f'{num} X {i} = {t(i)}')

# l = [12,13,14,15,16,17,18,19]
#
# output = list(filter(lambda x : (x%3==0),l))
# print(output)

# l = int(input('Enter the key:'))




################################# File handling

# fr = open('python.txt','r')
# print('ok')    #to locate the file and directory

# fr = open('python.txt','r')
# content = fr.read()
# print(content)
# fr.close()

#TO READ LINE BY LINE
# fr = open('python.txt','r')
# content = fr.read()
# # print(content)
# l = content.splitlines()
# print(l)
# fr.close()

#
# fr = open('python.txt','r')
# i = int(input('Enter the key: 34'))
# content = fr.read(i)
# print(content)

# fr = open('python.txt','r')
# content = fr.readline()  #read and print first line
# print(content)

# fr = open('python.txt','r')
# content = fr.readlines()  #read line to line and print in form of list
# print(content)

#to read letter by letter

# fr = open('python.txt','r')
# content = fr.read()
# for ch in content:
#     print(ch,end='')
# fr.close()

# fr = open('python.txt','r')
# for ch in fr.read():
#     print(ch,end='')
# fr.close()


# file = open('log.txt','r')
# sum = 0
# for line in file:
#     print(line)
#     l = line.split()
#     if l[3] != 'NA':
#         sum += int(l[3])
#
#
# print(f'Sum is :{sum}')

# fr = open('Python1.txt','w')
# fr.write('''Your Bill
# Name = Vaibhav Anil Dhotre''')
# fr.close()
#
# fr = open('python1.txt','a')
# fr.write('''\nAmount = 2345/-''')
# fr.close

# fr = open('Vaibhav.txt1','x')
# print(fr)
# if fr:
#     print('File Created !!!!!!!!')

# fr = open('Python1.txt','r')
# if fr:
#     print('File found')


# with open('python1.txt','a') as file:
#     file.write('''
#     Your order details are:
#     Paneer Tikka Masala
#     Aloo Tikki Masala
#     Aloo Paratha
#     Masala Chaas''')
# print('ok')


# fr = open('Python1.txt','r')
# print(fr.tell())
# c = fr.read(5)
# print(c)
# print(fr.tell())
# c = fr.read(10)
# print(c)
# print(fr.tell())
# c = fr.seek(5)
# print(fr.tell())


# fr = open('Python1.txt','r')
# print(fr.tell())
# c = fr.read(5)
# print(c)
# print(fr.tell())
# c = fr.read(17)
# print(c)
# print(fr.tell())
# fr.seek(0)
# print(fr.tell())
# c = fr.read(2)
# print(c)

# import os
# os.rename('Python1.txt','Python23.txt')
# print('Rename success')

# os.remove('log.txt')
# print('Remove success')

# fr = open('arith.py','x')

################# session 35
# Chapter - Modules and packages

# import arith
# print(arith.add(10,20))
# print(arith.pow(10,20))
# print(arith.mul(10,20))
# print(arith.sub(10,20))
# print(arith.div(10,20))
# print(arith.floor(10.25))
# print(arith.ceil(10.25))

# import os
# os.rename('vaibhav.py','arith.py')

# import maths as ar
# print(ar.mul(10,23))


# from arith import *
# print(add(10,23))

# fr = open('secondarith.py','x')
# import secondarith, maths
# print(maths.add(10,12))
# secondarith.add(10,12)

# import os
# os.rename('arith.py','maths.py')
# print('Renamed succesfully')

# from secondarith import add   #will not work
# print(add(19,34))       #53
# from maths import add
# print(add(19,34))       #53

# # open('IT Employeer.py','x')
# import os
# os.rename('IT','IT.py')

# import IT
# print(f'IT Employes are : {IT.itemployees()}')


############################# Exception Handling

# print('SE1')
# print('SE1')
# print('SE1')
# print('SE1')
# A = 10/0 #ZeroDivisionError: division by zero(code close)
# print('A')
# print('SE1')
# print('SE1')
# print('SE1')



# print('SE1')
# print('SE1')
# print('SE1')
# print('SE1')
# try:
#     a = 10/0
#     print(a)
# except ZeroDivisionError as i :
#     print(f'Exception Handle : {i}')
# print('SE1')
# print('SE1')
# print('SE1')

# print('''############################
# #########################''')

# print('SE1')
# print('SE1')
# print('SE1')
# print('SE1')
# try:
#     a = 10/0
#     print(a)
# except IOerror as i :
#     print(f'Exception Handle : {i}')
# print('SE1')
# print('SE1')
# print('SE1')


# print('SE1')
# print('SE1')
# print('SE1')
# print('SE1')
# try:
#     a = 10/0
#     print(a)
# except IOError as i :
#     print(f'Exception Handle : {i}')
# except ZeroDivisionError as i :
#     print(f'Exception Handle : {i}')
# print('SE1')
# print('SE1')
# print('SE1')


# print('SE1')
# print('SE1')
# print('SE1')
# try:
#     a = 10/2
#     print(a)
#     fr = open(f'IT')
#     print('FO SUCCESS')
# except IOError as i :
#     print(f'Exception Handle : {i}')
# except ZeroDivisionError as i :
#     print(f'Exception Handle : {i}')
# print('SE1')
# print('SE1')
# print('SE1')


#
# print('SE1')
# print('SE1')
# print('SE1')
# try:
#     a = 10/0
#     print(a)
#     fr = open(f'vaibhav')
#     print('FO SUCCESS')
# except IOError as i :
#     print(f'Exception Handle : {i}')
# except Exception as i :
#     print(f'Exception Handle : {i}')
# print('SE1')
# print('SE1')
# print('SE1')


#######################################
# Wipro
# 5678923
# 5+7+9+3 = 24

# num = int(input())
# sum = 0
# while num > 0:
#     r = num % 10
#     if r%2 != 0:
#         sum += r
#     num = num//10
# print(sum)


# s = input()
# sum = 0
#
# for i in range(len(s)):
#     if int(s[i])%2 != 0:
#         sum += int(s[i])
#
# print(sum)

# def getAnswer(StrNum):
#     sum = 0
#     for i in range(len(StrNum)):
#         if int(StrNum[i]) % 2 != 0:
#             sum += int(StrNum[i])
#
#     return sum
# if __name__ == '__main__':
#     StrNum = input()
#     print(getAnswer(StrNum))


#######################################
#6
# 1 2 2 9 4 1   I/P
# 9 5

# n = int(input())
# l = list(map(int,input().split()))[:n]
#
# i = 1
# while 1<len(l)-1:
#     sum_l = sum(l[:i])
#     sum_r = sum(l[i+1:])
#     if sum_l == sum_r:
#         print(l[i],sum_l)
#         break
#     i+=1


###############################
# l = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# 1 2 3 4           # 00 01 02 03
# 5 6 7 8           # 10 11 12 13
# 9 10 11 12        # 20 21 22 23

# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(f'{i}{j}',end = ' ')
#     print()

###############################
#Q3]
# 4 2
# 11 12 13 14 15 16 17 18

#       0  1
#
# 0    11 12
# 1    13 14
# 2    15 16
# 3    17 18
#
# r,c = list(map(int,input().split()))[:2]
# l = list(map(int,input().split()))[:r*c]
# print(l)
#
# l1 = []
# k=0
# for i in range(r):
#     o = []
#     for j in range(c):
#         o.append(l[k])
#         k+=1
#     l1.append(o)
#
# # print(l1)
# #[[11, 12], [13, 14], [15, 16], [17, 18]]
#
# if r >c:
#     for i in range(r):
#         for j in range(c,r):
#             l1.append(1)
#
#     c = r
#
# else:
#     o = []
#     for i in range(0,c):
#         o.append(1)
#
#     for i in range(r,c):
#         l1.append(o)
#
#     r = c
#
# print(l1)
#
# #logic for uper daigonal and lower diagonal
# sum = 0
# for i in range(r):
#     v= l1[i][i]
#
#     flag = True
#     for i in range(0,r-1):
#         for j in range(i+1,c):
#
#             if l1[i][j] == v:
#                 flag = False
#                 break
#
#             if l1[j][i] == v:
#                 flag = False
#                 break
#
#         if not flag:
#             break
#
#     if flag:
#         sum +=v
# print(sum)


###############################################
# 3Q]
# s = 'sisi'
# c = 'o'
# n = 6
# sioooooosi


# s = 'abab'
# c = 'd'
# n = 4
# abddddab

# s = input('s:')
# c = input('c:')
# n = int(input('n:'))
#
# i = len(s)//2
# print(s[:i]+n*c+s[i:])


#########################################
# 5
# 3
# 3
#
# 5 15 45
#
# 2
# 4
# 3
#
# 2 4 32
#
# 2
# 6
# 5
#
# 2 12 72 432 2592

# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
#
# sum = n1*n2
# print(n1,sum,end = ' ')
#
# for i in range(n3-2):
#     sum = sum*n2
#     print(sum,end = ' ')


#########################################
# alphxxdida
# 4
#
# explain
# alphxxdida  - Reversed
# adidxxhpla

#
# s1 = input()
# s2 = s1[::-1]
# cnt = 0
# i = 0
# while i < len(s1):
#     if s1[i] == s2[i]:
#         cnt+=1
#     i+=1
#
# print(cnt)


# s1 = input()
# s2 = s1[::-1]
# cnt = 0
# i = 0
# for i in  range(len(s1)):
#     if s1[i] == s2[i]:
#         print(f'{s1[i]} == {s2[i]}')
#         cnt+=1
#     i+=1
#
# print(cnt)



############################################\
# Q5]
# 1
# 4
# output
# -1
#
# 2
# 1
# 2
# output
# -1
#
# 2
# 5
# 25
# output
# 1
#
# 3
# 5
# 25
# 625
# output
# 2
#
# 4
# 5
# 25
# 625
# 1234
# output
# 2

# n = int(input())
# l = []
#
# for _  in range(n):
#     l.append(int(input()))
#
# print(l)
#
# # 3
# # 5
# # 25
# # 625
# # output
# # 2
# cnt = 0
# i = 0
# while i < len(l)-1:
#     if l[i]*l[i] == l[i+1]:
#         cnt+=1
#     else:
#         break
#     i+=1
#
# if cnt == 0:
#     print(-1)
# else:
#      print(cnt)



###################################
# Input
# 4
# 8 3 1 2
# output
# 29

# 1

##################################
# cut    slice
# 0        1
# 1        2
# 2        4
# 3        7

# cut = int(input('Cut: '))
#
# if cut <= -2:
#     print(-1)
# else:
#     print(f'Slice: {(cut*(cut+1)//2)+1}')

# def max_pizz(cut):
#     if(cut<=-1):
#         return -1
#     return (cut*(cut+1)//2)+1
#
# if __name__ == '__main__':
#     cut = int(input())
#     print(max_pizz(cut))


#########################################
# # Zoho - 22 lac
# ([]) - True
# ([{}])  - False
# (([[]]))  - True
# ([)] - False
#  ] - False

# s = input()
# l = []
# flag = False
#
# if s[0] == ')' or s[0] == ']' or s[0] == '}':
#     flag = False
#
# else :
#     for v in s:
#         if v == '[' or v == '(' or v == '{' :
#             l.append(v)
#         elif v == ']' and l[-1] == '[':
#             flag = True
#             del l[-1]
#         elif v == ')' and l[-1] == '(':
#             flag = True
#             del l[-1]
#         elif v == '}' and l[-1] == '{':
#             flag = True
#             del l[-1]
#         else:
#             flag = False
#             break
#
# if flag and len(l) == 0:
#     print('True')
# else:
#     print('False')


###################################### session 39
# 5
# 2 1 5 4 3
# 25

# n = int(input())
# l = list(map(int,input().split()))[:n]
# m = max(l)
# print(m*m)

# 6
# 1 2 3 4 5 6
# 1 + 3 + 5 = 9

# n = int(input())
# l = list(map(int,input().split()))
# sum_even,sum_odd = 0,0
# for v in l:
#     if v%2 != 0:
#         sum_odd+=v  #odd
#     else:
#         sum_even +=v
#
# print(sum_odd,sum_even)
# print(abs(sum_odd - sum_even))


#input 1
# {4,3,5}
# PNP
# 3
# output
# 600
# explain
# 3-4*5 = 6*100 = 600

# {2,3}
# PN
# 2
# output
# 100
# explain
# 2-3 = |-1|*100 = 100

#
# l = list(map(int,input().split()))
# s = input()
# n = int(input())
# sum = 0
# i = 0
#
# while i<n:
#     if s[i] == 'P':
#         sum += l[i]
#     else :
#         sum -= l[i]
#     i+=1
#
# print(abs(sum)*100)


# #apcdapapapospaapap
# 3

# s  = input()
# c = s.count('ap')
# print(c)
#
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# n4 = int(input())
# n5 = int(input())
#
# print(n1)
# sum = n1 + n2
# print(sum)
# sum1 = sum + n3
# print(sum1)
# sum2 = sum1 + n4
# print(sum2)
# sum3 = sum2 + n5
# print(sum3,end ='')


########################## Apptitude
# 01]
# pp , qq , rr = 3,8,8
# if (qq>pp and (qq^rr) < (pp + qq)):
#     pp = 7 & rr
#
# print(pp+qq+rr)

########################### CCR
# Factorial
# num = int(input('Enter the number :'))
# fact = 1
# for i in range(1,num+1):
#     fact *= i
# print(fact)


# def fact_num(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact *= i
#     return fact
#
# if __name__ == '__main__':
#     num = int(input('Enter the number:'))
#     fact = fact_num(num)
#     print(fact)


# Wipro
# Sum of odd number
# 5974132
# 25

# num  = int(input('Enter the number: '))
# sum = 0
# while num > 0:
#     r = num % 10
#     if r%2 != 0:
#         sum += r
#     num = num // 10
#
# print(sum)

# 5974132
# num  = input('Enter the number: ')
# sum = 0
# for value in num:
#     num = int(value)
#     if num % 2 != 0:
#         sum += num
# print(sum)


# 6
# 1 2 2 9 4 1
# 9 5
# n = int(input())
# l = list(map(int,input().split()))[:n]
# print(l)
#
# i = 1
# while i<len(l)-1:
#     sum_left = sum(l[ :i])
#     sum_right = sum(l[i+1: ])
#     if sum_left == sum_right:
#         print(l[i],sum_left)
#         break
#     i+=1

# def getAns(n):
#     i = 1
#     while i < len(l)-1:
#         sum_left = sum(l[:i])
#         sum_right = sum(l[i+1: ])
#         if sum_left == sum_right:
#             print(l[i],sum_left)
#             break
#         i += 1
#
#
# if __name__ == '__main__':
#     n = int(input())
#     l = list(map(int,input().split()))
#     i = 1
#     getAns(n)


# l = [ [1,2,3,4] , [5,9,8,10] , [6,7,8,9] ]
#
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(f'{l[i][j]}',end = '\t')
#     print()


# r,c = list(map(int,input().split()))[:2]
# l = list(map(int,input().split()))[:r*c]
# # print(l)
# k = 0
# l1 = []
# for i in range(r):
#     o = []
#     for j in range(c):
#         o.append(l[k])
#         k+=1
#     l1.append(o)
#
# # print(l1)
#
# if r > c:
#     for i in range(r):
#         for j in range(c,r):
#             l1[i].append(1)
#     c = r
#
# else:
#     o = []
#     for i in range(0,c):
#         o.append(1)
#     for j in range(r,c):
#         l1.append(o)
# # print(l1)


##########
# 5
# 3
# 3
#
# 5 15 45

# n1 = int(input())
# n2 = int(input())
# n = int(input())
#
# print(n1,n1*n2)
#
# while i < n-1:
#     print()


#################3
# cut - slice
# 0     1
# 1     2
# 2     4
# 3     7

# def pizza(cut):
#     if cut <= -1:
#         return -1
#     else:
#         return (cut*(cut + 1)/2) + 1
#
# if __name__ == '__main__':
#     cut = int(input())
#     slice = pizza(cut)
#     print(slice)

###################
# Input -
# 3
# 22 36 48
#
# output -
# 12 #Max sum of digit

# def maximum_digit_sum(numbers):
#   max_digit_sum = 0
#   for number in numbers:
#     digit_sum = 0
#     for digit in str(number):
#       digit_sum += int(digit)
#     max_digit_sum = max(max_digit_sum, digit_sum)
#   return max_digit_sum
#
# numbers = [22, 36, 48]
# max_sum = maximum_digit_sum(numbers)
# print(max_sum)


# n = int(input())
# l = list(map(int,input().split()))
# max_digit_sum = 0
# for number in l:
#     digit_sum = 0
#     for digit in str(number):
#         digit_sum += int(digit)
#     print(digit_sum)
#     max_digit_sum = max(max_digit_sum,digit_sum)
#
# print(max_digit_sum)

# def getAns(l):
#     max_digit_sum = 0
#     for number in l:
#         digit_sum = 0
#         for digit in str(number):
#             digit_sum += int(digit)
#         # print(digit_sum)
#         max_digit_sum = max(max_digit_sum, digit_sum)
#
#     return max_digit_sum
#
# if __name__ == '__main__':
#     n = int(input())
#     l = list(map(int,input().split()))[:n]
#     max = getAns(l)
#     print(max)

##########################
# n = 5 , k = 2
# # Arr[] = [12,5,786,1,23]
# print first K max number from Arr

# n = int(input())
# k = int(input())
# s = sorted(set(list(map(int,input().split()))))
# new_set = s[::-1]
# print(new_set)
#
# for i in range(k):
#     print(new_set[i],end = ' ')


# def getAns(n,k):
#     s = sorted(set(l))
#     new_set = s[::-1]
#
#     for i in range(k):
#         print(new_set[i], end=' ')
#
#
# if __name__ == '__main__':
#     n = int(input())
#     k = int(input())
#     l = list(map(int,input().split()))
#     Output = getAns(n,k)
#     print(Output)

# def getAns(n, k, l):
#     s = sorted(set(l))
#     new_set = s[::-1]
#     return new_set[:k]
#
# if __name__ == '__main__':
#     n = int(input())
#     k = int(input())
#     l = list(map(int, input().split()))
#     result = getAns(n, k, l)  # Call the function and store the result
#     for element in result:
#         print(element, end=" ")



##############################
# 6
# 1 2 3 4 5 6
# 1 + 3 + 5 = 9
# 2 + 4 + 6 = 12
# 12-9 = 3

# n = int(input())
# l = list(map(int,input().split()))[:6]
# sum_odd , sum_even = 0 , 0
# for value in l:
#     if value % 2 == 0:
#         sum_even += value
#     else:
#         sum_odd += value
#
# print(abs(sum_odd - sum_even))

# if sum_odd > sum_even:
#     print(sum_odd - sum_even)
# else:
#     print(sum_even - sum_odd)


#####################################
# input :
# {4,3,5}
# PNP
# 3

# output -
# 600
#
# Explain-
# 4-3+5 = 6*100 = 600
#
# l = list(map(int,input().split()))
# s = input()
# n = int(input())
#
# sum = 0
# i = 0
# while i<n:
#     if s[i] == 'P':
#         sum += l[i]
#     else:
#         sum -= l[i]
#     i+=1
#
# sum = abs(sum)
# print(sum*100)


##################
# 5
# 55

# n = int(input())
# sum = 0
#
# for i in range(1,n+1):
#     sum = sum + i**2
# print(sum)


################
# TCS
# 5 INPUT1
# [2849,1620,705,1,30]  INPUT2
# 2387  OUTPUT

# n = int(input())
# l = list(map(int,input().split()))
# s = sum(l)
# lit = s//n
# sum = 0
# for v in l:
#     if v > lit:
#         sum = sum + (v-lit)
#
# print(sum)



#########################
# Input-1
# 1
# 2
# 3
# 4
# 5
# output-1
# 1
# 3
# 6
# 10
# 15


# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# n4 = int(input())
# n5 = int(input())
#
# print(n1)
# sum = n1+n2
# print(sum)
# sum1 = sum + n3
# print(sum1)
# sum2 = sum1 + n4
# print(sum2)
# sum3 = sum2 + n5
# print(sum3)



#####################################
# s = input()
# v = ['A','a','e','E','i','I','o','O','u','U']
# output = ''
# for ch in s:
#     if ch not in v:
#         output += ch
# print(output)


#
# n = int(input())
# m = int(input())
#
# for i in range(n+1,m):
#     b = bin(i)
#     if '11' not in b:
#         print(b[2:],end = ' ')



# def find_binary_without_consecutive_ones(n, m):
#   results = []
#   for num in range(n+1, m):
#     binary_str = bin(num)[2:]  # Remove '0b' prefix
#     if not ('11' in binary_str):
#       results.append(binary_str)
#   return results
#
# n,m = list(map(int,input().split()))[:2]
# results = find_binary_without_consecutive_ones(n, m)
# for num in results:
#     print(num,end='\n')

