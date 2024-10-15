print("=========== Chapter 9:Advance modules and Topics ==========")
#
# import collections
# print(dir(collections))

# ['ChainMap', 'Counter', 'OrderedDict', 'UserDict', 'UserList', 'UserString', '_Link', '_OrderedDictItemsView', '_OrderedDictKeysView', '_OrderedDictValuesView', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_chain', '_collections_abc', '_count_elements', '_deque_iterator', '_eq', '_iskeyword', '_itemgetter', '_proxy', '_recursive_repr', '_repeat', '_starmap', '_sys', '_tuplegetter', 'defaultdict', 'deque', 'namedtuple']
#

##Namedtuple() =>

# import collections
# Student = collections.namedtuple('student',['name','age','dob'])
# s = Student('Shivam','19','2002-12-3')
# print(s._asdict())
# print(s.name,s[0],getattr(s,'name'))
# print(s.age,s[1],getattr(s,'age'))
# print(s.dob,s[2],getattr(s,'dob'))

# #Output =>
# {'name': 'Shivam', 'age': '19', 'dob': '2002-12-3'}
# Shivam Shivam Shivam
# 19 19 19
# 2002-12-3 2002-12-3 2002-12-3

# import collections
# Data = collections.namedtuple('Data',['Organization_name','SDE_Role','Management_Role'])
# a = input('Enter the company name:')
# b = input('Enter the core profile:')
# c = input('Any other profile:')
# t = Data(f'{a}',f'{b}',f'{c}')
# print(t._asdict())
# print(t.Organization_name)

##Output :
# Enter the company name: Infosys
# Enter the core profile:Python intern
# Any other profile:None
# {'name': ' Infosys', 'SDE_Role': 'Python intern', 'Management_Role': 'None'}


## OrderedDict()

# import collections
# d1 = collections.OrderedDict()
# d1['A'] = 10
# d1['B'] = 11
# d1['C'] = 12
# d1['D'] = 13
#
# for k,v in d1.items():
#     print(k,v)
#     print(f'Key:{k} Values:{v}')



