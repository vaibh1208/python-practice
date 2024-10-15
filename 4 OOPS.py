# a  = 10
# print(a)
# print(type(a))
# print(dir(a))
# print(a.__add__(10))
# print(a.__divmod__(5))

# import pyttsx3
# engine = pyttsx3.init()
# text = 'What is my name , My name is Vaibhav'
# print(text)
# engine.say(text)
# engine.runAndWait()


# arr = {0,3,1,2,2,3}
# for num in arr:
#
# arr1 = set(arr)
# print(arr)
# arr.intersection(arr1)

# s = input()
# s1 = s[::-1]
# if s1 == s:
#     print('palindrome')
# else:
#     print('not palindrome')

#######################OOPS
#
# class EmployeeName():
#     pass
#
# e1 = EmployeeName()
# e1.empid = 101
# e1.name = 'Vaibhav'
# e1.salary = 70000.23
#
# e2 = EmployeeName()
# e2.empid = 102
# e2.name = 'Aarush'
# e2.dev_type = 'Python Dev'
# e2.classes = ['C' , 'DS' , 'CPP']
#
# e3 = EmployeeName()
# e3.empid = 103
# e3.name = 'Kunal'
# e3.dev_type = 'C Dev'
#
#
# print('Display Employee 1')
# print(f'Emp Id :  {e1.empid} , Name : {e1.name} , Salary : {e1.salary}')
#
# print('Display Employee 2')
# print(f'Emp Id :  {e2.empid} , Name : {e2.name} , Dev_Type : {e2.dev_type}')
# print(f'Classes : {e2.classes}')
#
# print('Display Employee 3')
# print(f'Emp Id :  {e3.empid} , Name : {e3.name} , Dev_Type : {e3.dev_type}')
#
# print('Using object . __dict__ => Dictinary')
# print(e1.__dict__)
# print(e2.__dict__)
# print(e3.__dict__)
#
# d = e1.__dict__
# print(type(d))
# print(d['empid'])
# print(d['name'])
# print(d['salary'])
#
# print('Using vars(object)') #return dict
# print(vars(e1))
# print(vars(e2))
#
# d = vars(e1)
# print(type(d))
# print(d['empid'])
# print(d['name'])
# print(d['salary'])
# #
# # Display Employee 1
# # Emp Id :  101 , Name : Vaibhav , Salary : 70000.23
# # Display Employee 2
# # Emp Id :  102 , Name : Aarush , Dev_Type : Python Dev
# # Classes : ['C', 'DS', 'CPP']
# # Display Employee 3
# # # Emp Id :  103 , Name : Kunal , Dev_Type : C Dev
# {'empid': 101, 'name': 'Vaibhav', 'salary': 70000.23}
# {'empid': 102, 'name': 'Aarush', 'dev_type': 'Python Dev', 'classes': ['C', 'DS', 'CPP']}
# {'empid': 103, 'name': 'Kunal', 'dev_type': 'C Dev'}
# <class 'dict'>
# 101
# Vaibhav
# 70000.23



#########################################
# class employee():
#     def vowtech(self):
#         print(f'In fuction self means :{self}')
#
# e1 = employee()
# e2 = employee()
#
# print(f'E1 address:{e1}')
# print(f'E2 address : {e2}')
#
# e1.vowtech()
# e2.vowtech()

#################################
# class employee():
#     def set_value(self,empid,name,salary):
#         self.empid = empid
#         self.name = name
#         self.salary = salary
#
# e1 = employee()
# print(e1.__dict__)
# e1.set_value(101,'Vaibhav',10000)
# print(e1.__dict__)
#
# print(f'Employee Id : {e1.empid}')
# print(f'Name : {e1.name}')
# print(f'Salary : {e1.salary}')




# class employee():
#     def set_value(self,empid,name,salary):
#         self.empid = empid
#         self.name = name
#         self.salary = salary
#
#     def display(self,):
#         print(f'Employee ID : {self.empid}',end = ' ')
#         print(f'Employee Name : {self.name}',end = ' ')
#         print(f'Employee Salary : {self.salary}')
#
# e1 = employee()
# e1.set_value(101,'Vaibhav',10000)
#
#
# e2 = employee()
# e2.set_value(101,'Vaibhav',10000)
#
# print('Display Employee 1')
# e1.display()
#
# print('Display Employee 2')
# e2.display()


#
# class employee():
#     def set_value(self):
#         self.empid = int(input('Enter Employee ID: '))
#         self.name = input('Enter Employee Name: ')
#         self.salary = int(input('Enter Employee Salary: '))
#
#     def display(self):
#         print(f'Employee ID : {self.empid}',end = ' ')
#         print(f'Employee Name : {self.name}',end = ' ')
#         print(f'Employee Salary : {self.salary}')
#
# e1 = employee()
# e1.set_value()
#
# e2 = employee()
# e2.set_value()
#
# print('Display Employee 1')
# e1.display()
#
# print('Display Employee 2')
# e2.display()
#
# print(e1.__dict__)
# print(e2.__dict__)

##################################
# class student():
#     def info(self):
#      self.name = input('Enter Student Name: ')
#      self.rollno = int(input('Enter the Roll no:'))
#      self.per = int(input('Enter the Percentage'))
#
#     def display(self):
#         print(f'Student Name :{self.name}')
#         print(f'Student Rollno : {self.rollno}')
#         print(f'Student Percentage : {self.per}')
#
# s1 = student()
# s1.info()
#
# s2 = student()
# s2.info()
#
# print('STUDENT DATA')
# s1.display()
# s2.display()



#####################################
# class student():
#     def set_values(self,rollno,name,per):
#         self.rollno = rollno
#         self.name = name
#         self.per = per
#         self.tution = 'Vowtech'
#
#     def display(self):
#         print(f'Rollno : {self.rollno}',end = ' ')
#         print(f'Name : {self.name}', end=' ')
#         print(f'Percentage : {self.per}', end=' ')
#         print(f'Tution : {self.tution}', end=' ')
#
#
# print('############# BEFORE #############')
# s1 = student()
# s1.set_values(101,'Vaibav',98.32)
#
# s2 = student()
# s2.set_values(102,'Aarush',98.43)
#
# print("display student 1")
# s1.display()
#
# print("display student 2")
# s2.display()
#
# print(s1.__dict__)
# print(s2.__dict__)
#
#
# s1.tution = 'Vowtech IT TC'
# s2.tution = 'Vowtech IT'
#
# print('############# AFTER #############')
# s1.tution = 'Vowtech IT TC'
# s2.tution = 'Vowtech IT'
#
# print("display student 1")
# s1.display()
#
# print("display student 2")
# s2.display()
#
# print(s1.__dict__)
# print(s2.__dict__)



# class student():
#     tution = 'Vowtech'
#     def set_values(self,rollno,name,per):
#         self.rollno = rollno
#         self.name = name
#         self.per = per
#
#     def display(self):
#         print(f'Rollno : {self.rollno}',end = ' ')
#         print(f'Name : {self.name}', end=' ')
#         print(f'Percentage : {self.per}', end=' ')
#         print(f'Tution : {self.tution}', end=' ')
#
#
# # print('############# BEFORE #############')
# s1 = student()
# s1.set_values(101,'Vaibav',98.32)
#
# s2 = student()
# s2.set_values(102,'Aarush',98.43)
#
# print("display student 1")
# s1.display()
#
# print("display student 2")
# s2.display()
#
# print(s1.__dict__)
# print(s2.__dict__)


################################################
# class Number():
#     @classmethod
#     def square(cls,number):
#         return number*number
#
#     @classmethod
#     def cube(cls,number):
#         return number*number*number
#
# number =  int(input('Enter ANY Key : '))
# sq = Number.square(number)
# cb = Number.cube(number)
# print(f'{number} square is {sq}')
# print(f'{number} cube is {cb}')

#####################################
# class Employee():
#     INCREMENT = 1000
#     def __init__(self,id,name,salary,increment):
#         self.id = id
#         self.name = name
#         self.salary = salary
#         self.increment = increment
#
#     def display(self):
#         print(f'id : {self.id}',end = ' ')
#         print(f'Name : {self.name}', end=' ')
#         print(f'salary : {self.salary}', end=' ')
#         print(f'Increment : {self.increment}', end=' ')
#
# e1 = Employee(101,'Vaibhav',55000.55,100)
# e2 = Employee(102,'Vaishnav',66000.66,200)
#
# e1.display()
# e2.display()
#
# print(f'Common Increment is RS{Employee.INCREMENT}')
# print(e1.__dict__)
# print(e2.__dict__)
#
# del e1
# del e2
#
# print(e1.__dict__) #error
# print(e2.__dict__) #error


######################## CV = to count number of objects
# class Employee():
#     NO_OF_EMPLOYEES = 0
#     def __init__(self,id,name,salary,increment):
#         self.id = id
#         self.name = name
#         self.salary = salary
#         self.increment = increment
#         Employee.NO_OF_EMPLOYEES += 1
#     def display(self):
#         print(f'id : {self.id}',end = ' ')
#         print(f'Name : {self.name}', end=' ')
#         print(f'salary : {self.salary}', end=' ')
#         print(f'Increment : {self.increment}', end=' ')
#
# e1 = Employee(101,'Vaibhav',55000.55,100)
# e2 = Employee(102,'Vaishnav',66000.66,200)
# e3 = Employee(103,'Arush',67000.88,300)
# e4 = Employee(104,'Varun',88000.66,300)
#
# print(f'Number of Employees are :{Employee.NO_OF_EMPLOYEES}')
# e1.display()
# print()
# e2.display()
# print()
# e3.display()
# print()
# e4.display()

#############################################
# string = '101-Vaibhav-75000.55'
# l = string.split('-')
# print(l)
# print(type(l))
#
# id = int(l[0])
# name = l[1]
# salary = float(l[2])
#
# print(id)
# print(type(id))
#
# print(name)
# print(type(name))
#
# print(salary)
# print(type(salary))

#########################################
# l = ['101', 'Vaibhav', '75000.55']
# l = [ str(value) for value in l]
# s = '-'.join(l)
# print(s)
# print(type(s))

########################################
# string = '103-Vaibhav-76000.55'
# id,name,salary = string.split('-')
# print(f'ID : {id}')
# print(f'NAME : {name}')
# print(f'SALARY : {salary}')

#########################################
# class Employee():
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#
#     def display(self):
#         print(f'ID :{self.id}', end = ' ')
#         print(f'NAME :{self.name}', end = ' ')
#         print(f'SALARY :{self.salary}', end = '')
#         print()
#
#     @classmethod
#     def createobject(cls,string):
#         id,name,salary = string.split()
#         return cls(int(id),name,float(salary))
#
# e1 = Employee(101,'Vaibhav',456)
# e2 = Employee(102,'Arun',322)
# e3 =Employee.createobject('103 Varun 56700')
#
# e1.display()
# e2.display()
# e3.display()


##########################################
# class Employee():
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#
#     def display(self):
#         print(f'ID :{self.id}')
#         print(f'NAME :{self.name}')
#         print(f'SALARY :{self.salary}')
#         print(f'CURRENT DAY IS {self.getday()}')
#         print(f'CURRENT DAY IS {Employee.getday()}')
#
#         print()
#
#     @classmethod
#     def createobject(cls,string):
#         id,name,salary = string.split()
#         return cls(int(id),name,float(salary))
#
#     @staticmethod
#     def getday():
#         from datetime import datetime
#         dt = datetime.now()
#         return dt.strftime('%A')
#
# e1 = Employee(101,'Vaibhav',456)
# e2 = Employee(102,'Arun',322)
# e3 =Employee.createobject('103 Varun 56700')
#
# e1.display()
# e2.display()
# e3.display()


################################## Inheritance
# class Pappa():
#     def set_page(self,age):
#         self.page = age
#
#     def p_job(self):
#         print('Pappa doing job in TCS')
#
# class Child1(Pappa):
#     def set_cage(self,age):
#         self.cage = age
#
#     def c_job(self):
#         print('Child is doing job in IBM')
#
# c1 = Child1()
# c1.set_page(50)
# print(f'Pappa Age : {c1.page}')
# c1.p_job()
#
# c1.set_cage(25)
# print(f'Child Age : {c1.cage}')
# c1.c_job()

##############################################
# class Pappa():
#     def job(self):
#         print(f'Pappa is doing job in TCS')
# class child1(Pappa):
#     def education(self):
#         print(f'Child1 is doing education ')
# class child2(Pappa):
#     def education(self):
#         print(f'Child2 is doing education ')
#
# c1 = child1()
# c1.job()
# c1.education()
#
# c2 = child2()
# c2.job()
# c2.education()

#######################################
# class Employee():
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#
#
#     def display(self):
#         print(f'ID:{self.id}')
#         print(f'NAME:{self.name}')
#         print(f'SALARY:{self.salary}')
#
# class Programmer(Employee):
#
#     def __init__(self,id,name,salary,prog_type,exp):
#         super().__init__(id,name,salary)
#         self.prog_type = prog_type
#         self.exp = exp
#
#     def display(self):
#         super().display()
#         print(f'PROG_TYPE:{self.prog_type}')
#         print(f'EXP:{self.exp}')
#
# p1 = Programmer(101,'Vaibhav',3456,'Python_dev',3)
#
# p2 = Programmer(102,'VaibhavI',34456,'Python_dev',4)
#
# p1.display()
# p2.display()
#
# # <class '__main__.Programmer'>
# # <class '__main__.Programmer'>
# print(type(p1))
# print(type(p2))


# #############################################
# class Employee():
#     pass
#
# e1 = Employee()
# e1.empid = '101'
# e1.name = 'Vaibhav'
# e1.salary = 15000
#
# e2 = Employee()
# e2.empid = '102'
# e2.name = 'Aarush'
# e2.dev_type = 10000
# e2.classes = ['C','DS','CPP']
#
# print('Display Employee 1')
# print(f'Emp Id :  {e1.empid} , Name : {e1.name} , Salary : {e1.salary}')
#
# print('Display Employee 2')
# print(f'Emp Id :  {e2.empid} , Name : {e2.name} , Dev_Type : {e2.dev_type}')
# print(f'Classes : {e2.classes}')


##################################################

# class employee():
#     def set_value(self,empid,name,salary):
#         self.empid = empid
#         self.name = name
#         self.salary = salary
#
# e1 = employee()
# # print(e1.__dict__)
# e1.set_value(102,'Vaibhav',10000)
# print(e1.__dict__)
#
# e2 = employee()
# e2.set_value(103,'Vaishnav',12000)
# print(e2.__dict__)
# print()
# print(f'Employee Id : {e1.empid}')
# print(f'Name : {e1.name}')
# print(f'Salary : {e1.salary}')
# print()
# print(f'Employee Id : {e2.empid}')
# print(f'Name : {e2.name}')
# print(f'Salary : {e2.salary}')




# class employee():
#     def set_value(self):
#         self.empid = input('Enter Employee ID: ')
#         self.name = input('Enter Employee Name: ')
#         self.salary = int(input('Enter Employee Salary: '))
#
#     def display(self):
#         print(f'Employee ID : {self.empid}',end = ' ')
#         print(f'Employee Name : {self.name}',end = ' ')
#         print(f'Employee Salary : {self.salary}')
#
# e1 = employee()
# e1.set_value()
#
# e2 = employee()
# e2.set_value()
#
# print('Display Employee 1')
# e1.display()
#
# print('Display Employee 2')
# e2.display()
# #
# print(e1.__dict__)
# print(e2.__dict__)


######################################## 3-5-24
# class employee():
#
#     course = 'Python'
#
#     def set_value(self):
#         self.empid = input('Enter Employee ID: ')
#         self.name = input('Enter Employee Name: ')
#         self.salary = int(input('Enter Employee Salary: '))
#
#     def display(self):
#         print(f'Employee ID : {self.empid}',end = ' ')
#         print(f'Employee Name : {self.name}',end = ' ')
#         print(f'Employee Salary : {self.salary}' ,end = ' ')
#         print(f'Course Applied: {employee.course}')
#
# e1 = employee()
# e1.set_value()
#
# e2 = employee()
# e2.set_value()
#
# print('Display Employee 1')
# e1.display()
#
# print('Display Employee 2')
# e2.display()
# #
# print(e1.__dict__)
# print(e2.__dict__)

# class examresults() :
#
#     examination = 'JUN-JUL-2023-24'
#
#     def student(self):
#
#         self.name = input('Enter the name of the candidate: ')
#         self.PRN = int(input('Enter the candidate PRN: '))
#         self.CGPA = float(input('Enter the CGPA: '))
#
#     def display(self):
#         print('Result is displayed as below')
#         print(f'Candidate Name:{self.name}')
#         print(f'Candidate PRN:{self.PRN}')
#         print(f'CGPA:{self.CGPA}')
#
#         d = examresults()
#         print(f'SEMESTER: {d.examination}')
#
#     @classmethod
#     def change(cls):
#         print('In class Function')
#         cls.examination = 'Final'
#         print(f'Result: {cls.examination}')
#
#
# s = examresults()
# s.student()
# s.display()
# examresults.change()

# class Number():
#
#     @classmethod
#     def square(cls,number):
#         return number*number
#
#     @classmethod
#     def cube(cls,number):
#         return number*number*number
#
# number = int(input('Enter the Number: '))
# s1 = Number.square(number)
# print(f'{number} square is {s1}')
# s2 = Number.cube(number)
# print(f'{number} cube is {s2}')


# Constructor

# class Employee():
#
#     Employee_Count = 0
#
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#         Employee.Employee_Count +=1
#
#     def display(self):
#         print(f'ID :{self.id}', end = ' ')
#         print(f'NAME :{self.name}', end = ' ')
#         print(f'SALARY :{self.salary}', end = '')
#         print()
#
#     # @classmethod
#     # def createobject(cls,string):
#     #     id,name,salary = string.split()
#     #     return cls(int(id),name,float(salary))
#
# print(f'Number of Employee:{Employee.Employee_Count}')
#
# e1 = Employee(101,'Vaibhav',456)
# e2 = Employee(102,'Arun',322)
# # e3 =Employee.createobject('103 Varun 56700')
#
# e1.display()
# e2.display()
# # e3.display()
#
# print(f'Number of Employee:{Employee.Employee_Count}')
# string = input('Enter the Data: ')
# l = string.split()
# # print(l)
# id = int(l[0])
# name = l[1]
# salary = float(l[2])
# print(f'Employee id is:{id}')
# # print(type(id))
# print(name)
# # print(type(name))
# print(salary)
# # print(type(salary))

############# 7-5-24

# l = list(map(int,input().split()))
# print(l)
# print(type(l))
# l = [str(value) for value in l]
# print(l)
# print(type(l))
# s = ' '.join(l)
# print(s)
# print(type(s))

############################ inheritance
# class pappa():
#     def set_page(self,age):
#         self.page = age
#
#     def p_job(self):
#         print('Pappa is doing job in tcs')
#
#         #2 IF and IV
#
# class child(pappa):
#     def set_cage(self,age):
#         self.cage = age
#
#     def c_job(self):
#         print('Child is not doing job')
#
# c1 = child()
# c1.set_page(50)
# print(f'Pappa age:{c1.page}')
# c1.p_job()
#
# c1.set_cage(25)
# print(f'Child age: {c1.cage}')
# c1.c_job()


# ##########################################
# class Employee():
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#
#     def display(self):
#         print(f'ID:{self.id}',end=',')
#         print(f'Name:{self.name}',end=',')
#         print(f'Salary:{self.salary}')
#
# class Programmer(Employee):
#     def __init__(self,id,name,salary,prog_type,exp):
#         self.id = id
#         self.name = name
#         self.salary = salary
#         self.prog_type = prog_type
#         self.exp = exp
#
#     def display(self):
#         print(f'ID:{self.id}',end=',')
#         print(f'Name:{self.name}',end=',')
#         print(f'Salary:{self.salary}',end=',')
#         print(f'Programmer Type:{self.prog_type}', end=',')
#         print(f'Name:{self.exp}')
#
# p1 = Programmer(101,'vaibhav',30000,'Python_dev',3)
# p1.display()

##drawback
#solution


# class Employee():
#     def __init__(self, id, name, salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#
#     def display(self):
#         print(f'ID:{self.id}', end=',')
#         print(f'Name:{self.name}', end=',')
#         print(f'Salary:{self.salary}')
#
#
# class Programmer(Employee):
#     def __init__(self, id, name, salary, prog_type, exp):
#         super().__init__(id,name,salary)
#         self.prog_type = prog_type
#         self.exp = exp
#
#     def display(self):
#         super().display()
#         print(f'Programmer Type:{self.prog_type}', end=',')
#         print(f'Name:{self.exp}')
#
#
# p1 = Programmer(101, 'vaibhav', 30000, 'Python_dev', 3)
# p2 = Programmer(102,'Vaibhav',35000,'C_Dev',4)
# p2.display()
# p1.display()

########################################
# a = 10
# print(type(a))
# print(dir(a))
#
# a = 10
# s = a.__add__(20)
# print(s)
#
# a = 10
# print(type(a))
# print('After conversion')
# s = a.__str__()
# print(s)

#######################################
# class Employee():
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print(f'ID:{self.id}', end=',')
#         print(f'Name:{self.name}',end=',')
#         print(f'Salary:{self.salary}')
#
#     def __add__(self,e):
#         return self.salary + e.salary
#
#     def __sub__(self,e):
#         return self.salary - e.salary
#
# e1 = Employee(101,'Vaibhav',35000)
# e2 = Employee(102,'Sayali',45000)
# e1.display()
# e2.display()
#
# salary = e1.__add__(e2)
# print(salary)
#
# s1 = e2 - e1
# print(s1)
#
# salary = e2.__sub__(e1)
# print(salary)
#
#
# s1 = e1 - e2
# print(s1)
#
# salary = e1.__sub__(e2)
# print(salary)
#
# s = e1 + e2
# print(s)

########################

# class Employee():
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print(f'ID:{self.id}', end=',')
#         print(f'Name:{self.name}',end=',')
#         print(f'Salary:{self.salary}')
#
#     def __add__(self,e2,e3,e4):
#         return self.salary + e2.salary + e3.salary + e4.salary
#
#
#
# e1 = Employee(101,'Vaibhav',35000)
# e2 = Employee(102,'Sayali',45000)
# e3 = Employee(103,'Rohit',45000)
# e4 = Employee(104,'Aarush',43567)
# e1.display()
# e2.display()
# e3.display()
# e4.display()
#
# s = e1.__add__(e2,e3,e4)
# print(salary)


# class Employee():
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print(f'ID:{self.id}', end=',')
#         print(f'Name:{self.name}',end=',')
#         print(f'Salary:{self.salary}')
#
#     def __str__(self):
#         return f'{self.id}-{self.name}-{self.salary}'
#
#     def __repr__(self):
#         return f'{self.id},{self.name},{self.salary}'
#
# e1 = Employee(101,'Vaibhav',35000)
# e2 = Employee(102,'Sayali',45000)
# e3 = Employee(103,'Rohit',45000)
# e4 = Employee(104,'Aarush',43567)
#
# print(e1.__str__())
# print(type(e1.__str__()))
# print(str(e1))
#
# print(e2.__str__())
# print(str(e2))
#
# print(e1.__repr__())
# print(str(e1))
#
# print(e2.__repr__())
# print(str(e2))

#
#
# class Employee():
#     def __init__(self,id,fname,lname,salary):
#         self.id = id
#         self.fname = fname
#         self.lname = lname
#         self.salary = salary
#         self.email = fname +'.'+lname+'@gmail.com'
#     def display(self):
#         print(f'ID:{self.id}')
#         print(f'First Name:{self.fname}')
#         print(f'Last Name:{self.lname}')
#         print(f'Salary:{self.salary}')
#         print(f'Email:{self.email}')  #Vaibhav.Dhotre@gmail.com
#
# e1 = Employee(101,'Vaibhav','Dhotre',450000)
# e1.display()
#
# e1.fname = 'Vaishnav'
#
# e1.display() #no change in email


##############################################################


# class Employee():
#     def __init__(self,id,fname,lname,salary):
#         self.id = id
#         self.fname = fname
#         self.lname = lname
#         self.salary = salary
#     def display(self):
#         print(f'ID:{self.id}')
#         print(f'First Name:{self.fname}')
#         print(f'Last Name:{self.lname}')
#         print(f'Salary:{self.salary}')
#
#     def email(self):
#         return self.fname+'.'+self.lname+'@pccoepune.org'
#
# e1 = Employee(101,'Vaibhavaa','Dhotre',45000)
# e1.display()
# print(e1.email())
#
# e1.fname = 'Rohit'
# e1.display()
# print(e1.email())

########################################################3

#
# class Employee():
#     def __init__(self,id,fname,lname,salary):
#         self.id = id
#         self.fname = fname
#         self.lname = lname
#         self.salary = salary
#     def display(self):
#         print(f'ID:{self.id}')
#         print(f'First Name:{self.fname}')
#         print(f'Last Name:{self.lname}')
#         print(f'Salary:{self.salary}')
#
#     @property
#     def email(self):
#         return self.fname+'.'+self.lname+'@pccoepune.org'
#
#     @email.setter
#     def email(self,string):
#         self.fname , self.lname = string.split('@')[0].split('.')
#
#
# e1 = Employee(101,'Vaibhavaa','Dhotre',45000)
# e1.display()
# print(e1.email )
#
# e1.fname = 'Rohit'
# e1.display()
# print(e1.email)
#
# e1.email = 'Dengu.dhotre@pccoepune.org'
# e1.display()
# print(e1.email)

################################################## OOPS 8

#
# class Employee():
#     def __init__(self,id,fname,lname,salary):
#         self.id = id
#         self.fname = fname
#         self.lname = lname
#         self.salary = salary
#     def display(self):
#         if self.id != None:
#             print(f'ID:{self.id}')
#             print(f'First Name:{self.fname}')
#             print(f'Last Name:{self.lname}')
#             print(f'Salary:{self.salary}')
#         else:
#             print('Employee Data Not found')
#     @property
#     def email(self):
#         if self.id != None:
#             return self.fname+'.'+self.lname+'@pccoepune.org'
#         else:
#             return 'Employee data not found'
#     @email.setter
#     def email(self,string):
#         self.fname , self.lname = string.split('@')[0].split('.')
#
#     @email.deleter
#     def email(self):
#         self.id = None
#         self.fname = None
#         self.lname = None
#         self.salary = None
#
#
# e1 = Employee(101,'Vaibhavaa','Dhotre',45000)
#
# e1.display()
# print(e1.email )
#
# print('==============================')
#
# e1.email = 'Vaibhavdhotre0806@gmail.com'
# e1.display()
# print(e1.email)
#
# print('==============================')
# print(e1.__dict__)
# del e1.email
#
# print('==============================')
# print(e1.__dict__)



# class Employee():
#     '''E1 ans e2 are the bjects'''
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print(f'ID:{self.id}', end=',')
#         print(f'Name:{self.name}',end=',')
#         print(f'Salary:{self.salary}')
#
#     def __add__(self,e2,e3,e4,number):
#         return self.salary + e2.salary + e3.salary + e4.salary + number
#
# e1 = Employee(101,'Vaibhav',35000)
# e2 = Employee(102,'Sayali',45000)
# e3 = Employee(103,'Rohit',45000)
# e4 = Employee(104,'Aarush',43567)
# e1.display()
# e2.display()
# e3.display()
# e4.display()
#
# print(e1.__doc__)  #E1 ans e2 are the bjects
#
# s = e1.__add__(e2,e3,e4,23453)
# print(s)

# #################################session 09
# class one():
#     def sub(self,a,b):
#         return a-b
#
# class two():
#     def mul(self,a,b):
#         return a*b
#
# class result(one,two):
#     def addition(self,a,b):
#         return a+b
#
# d = result()
#
# print(d.addition(20,34))
# print(d.)
# print(issubclass(result,one)) #true
# print(issubclass(result,two)) #true
# print(issubclass(two,one)) #false


# print(isinheritance())


#
# class class1:
#     def m(self):
#         print('CLASS 1')
#
# class class2:
#     def m(self):
#         print('CLASS 2')
#
# class class3(class1,class2):
#     def m(self):
#         print('CLASS 3')
#
# c = class3()
# c.m()
# class1.m(c)
# class2.m(c)



# class class1:
#     def m(self):
#         print('CLASS 1')
#
# class class2:
#     def m(self):
#         print('CLASS 2')
#
# class class3(class1,class2):
#     def m(self):
#         print('CLASS 3')
#         class1.m(self)
#         class2.m(self)
#
# c = class3()
# c.m()
# print('OUTSIDE CALL FOR CLASS1 AND CLASS2')
# class1.m(c)
# class2.m(c)



# class class1:
#     def m(self):
#         print('CLASS 1')
#
# class class2:
#     def m(self):
#         print('CLASS 2')
#
# class class3(class1,class2):
#     def m(self):
#         print('CLASS 3')
#         super().m()

# c = class3()
# c.m()

#
# class class1:
#     def m(self):
#         print('CLASS 1')
#
# class class2:
#     def m(self):
#         print('CLASS 2')
#
# class class3(class1,class2):
#     def m(self):
#         print('CLASS 3')
#
#
# c = class3()
# c.m()



class class1:
    def m(self):
        print('CLASS 1')

class class2:
    def m(self):
        print('CLASS 2')

class class3(class1,class2):
    pass

c = class3()
c.m()  #always class1
class1.m(c)
class2.m(c)

#
#
# class class1:
#     pass
#
# class class2:
#     def m(self):
#         print('CLASS 2')
#
# class class3(class1,class2):
#     pass
#
# c = class3()
# c.m()  #now will select class 2



