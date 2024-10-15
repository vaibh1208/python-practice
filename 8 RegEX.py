#Findall function()

# import re
# print(dir(re))
# txt = "The rain in Spain"
# x = re.match("in Spain", txt)
# if x:
#     print("Yes Match is found")
# else:
#     print("No match is found")


# import re
# txt = 'How are you, How is your day going'
# matches = re.findall("How",txt)
# print(matches) #['How', 'How']

# import re
# text = 'How are you, How is everything'
# pattern = re.compile(r'How')
# matches = pattern.finditer(text)
# print(matches)
# for match in matches:
#     print(match)

# import re
# txt = 'Mumbai is the financial, commercial,[30] and entertainment capital of South Asia. Mumbai is often compared to New York,[31][32] and the city is home to the Bombay Stock Exchange, situated on Dalal Street. It is also one of the worlds top ten centres of commerce in terms of global financial flow,[33] generating 6.16% of Indias GDP,[34] and accounting for 25% of the nations industrial output, 70% of maritime trade in India (Mumbai Port Trust, Dharamtar Port and JNPT),[35] and 70% of capital transactions to Indias economy.[36][37] The city houses important financial institutions and the corporate headquarters of numerous Indian companies and multinational corporations. The city is also home to some of Indias premier scientific and nuclear institutes , the Hindi, Marathi film industries. Mumbais business opportunities attract migrants from all over India.'
# matches = re.findall('Mumbai',txt)
# print(matches)
# if matches:
#     print("Yess there are atleat one match")
# else:
#     print("ERROR")


# import re
# txt = 'Mumbai is the financial, commercial,[30] and entertainment capital of South Asia. Mumbai is often compared to New York,[31][32] and the city is home to the Bombay Stock Exchange, situated on Dalal Street. It is also one of the worlds top ten centres of commerce in terms of global financial flow,[33] generating 6.16% of Indias GDP,[34] and accounting for 25% of the nations industrial output, 70% of maritime trade in India (Mumbai Port Trust, Dharamtar Port and JNPT),[35] and 70% of capital transactions to Indias economy.[36][37] The city houses important financial institutions and the corporate headquarters of numerous Indian companies and multinational corporations. The city is also home to some of Indias premier scientific and nuclear institutes , the Hindi, Marathi film industries. Mumbais business opportunities attract migrants from all over India.'
# pattern = re.compile(r'Mumbai')
# matches = pattern.finditer(txt)
# print(matches)
#
# for match in matches:
#     print(match)
# if matches:
#     print("Yess there are atleat one match")
# else:
#     print("ERROR")


# import re
# txt = 'abvcs'
# match = re.findall('^a...s$',txt)
# print(match)
# if match:
#     print("Required Pattern Exists")
# else:
#     print("Required Pattern does not exists")

# import re
# txt = 'abvs'
# pattern = re.compile(txt)
# matches = pattern.finditer(txt)
# print(matches)
# for match in matches:
#     print(match)

# import re
# txt = 'abvs'
# pattern = re.compile(r'abvs')
# matches = pattern.finditer(txt)
# print(matches)
# for match in matches:
#     print(match)

# import re
# txt = 'The university ordered for the resolution in the india'
# pattern = re.compile(r'^The.*india$')
# matches = pattern.finditer(txt)
# print(matches)
# for match in matches:
#     print(match)


#Search Function()

# import re
# txt = 'The rain in spain'
# match = re.search('ain',txt) #Here we get only first match
# print(match)
# if match:
#     print("Required Pattern Exists")
# else:
#     print("Required Pattern does not exists")

#######################################

# import re
# txt = "The rain in spain"
# pattern = re.compile(r'ain')
# matches = pattern.finditer(txt)
# print(matches)
#
# if matches:
#     print('Match Found')
# else:
#     print("SORRY")
#
# for match in matches:
#     print(match)

###############################

# import re
# txt = 'The rain in spain'
# x = re.search('ain',txt) #Here we get only first match
# print(x)
# print(x.start())
# print(x.end())
# print(x.span())
# print(x.string)
# print(x.group())

#############################3

#split()

# import re
# txt = 'The rain in spain'
# l = txt.split()
# print(l)
# l = re.split('\s',txt)
# print(l)

# Output =
# ['The', 'rain', 'in', 'spain']
# ['The', 'rain', 'in', 'spain']

###################################

# import re
# txt = 'The$rain$in$spain'
# l = txt.split('$')
# print(l)
# l = re.split('\$',txt)
# print(l)

# Output =
# ['The', 'rain', 'in', 'spain']
# ['The', 'rain', 'in', 'spain']

#######################################
# import re
# txt = 'My name is vaibhav'
# x = re.findall('[a-z]',txt)
# print(x)

##############################
# import re
# str= " I have 59 ruppes"
# pattern = re.compile(r'\d')
# matches = pattern.findall(str)
# print(matches)
#
# for match in matches:
#     print(match)
################################
# import re
# str = 'I have 59 ruppes'
# matches = re.findall('\d',str)
# print(matches)

###############################
# import re
# str = 'I have 59 rupees'
# matches =  re.findall('\d\d',str)
# print(matches)

#output = ['59']

################################
# import re
# str = 'I have 59 rupees'
# pattern = re.compile(r'\d\d')
# matches = pattern.finditer(str)
# print(matches)

#output = ['59']

###############################

# import re
# str = 'I have 59 rupees 56 78'
# matches =  re.findall('\d{2}',str)
# print(matches)

#output = ['59', '56', '78']

################################
# import re
# str = 'I have 59 rupees 54 67 34'
# pattern = re.compile(r'\d{2}')
# matches = pattern.finditer(str)
# print(matches)


#output = ['59', '54', '67', '34']

#################################
# import re
# str = 'I have 59 rupees 54 67 34'
# pattern = re.compile(r'\d{2}')
# matches = pattern.finditer(str)
# print(matches)
# for match in matches:
#     print(match)

# output =
# <callable_iterator object at 0x0000022DB9216710>
# <re.Match object; span=(7, 9), match='59'>
# <re.Match object; span=(17, 19), match='54'>
# <re.Match object; span=(20, 22), match='67'>
# <re.Match object; span=(23, 25), match='34'>

##################################
# import re
# str = 'I have 59 rupees hello world'
# pattern = re.compile(r'he..o')
# matches = pattern.finditer(str)
# print(matches)
# for match in matches:
#     print(match)

# import re
# str = 'I have 59 rupees hello world'
# x = re.findall('he..o',str)
# print(x)
# print(str[17:22])

##############################
# import re
# str = 'In Python, a tuple is an ordered and immutable collection of elements. Tuples are similar to lists, but unlike lists, once a tuple is created, its elements cannot be changed or modified. Tuples are defined using parentheses ( ). Heres an example program that illustrates the concept of a tuple'
# pattern = re.compile(r'tup*')
# x = pattern.finditer(str)
# print(x)
# for match in x:
#     print(match)
#
# import re
# str = 'In Python, a tuple is an ordered and immutable collection of elements. Tuples are similar to lists, but unlike lists, once a tuple is created, its elements cannot be changed or modified. Tuples are defined using parentheses ( ). Heres an example program that illustrates the concept of a tuple'
# x = re.findall('tup*',str)
# print(x)
# if x:
#     print('Match Found')
# else:
#     print('No Match Found')

######################################
# import re
# str = 'All the best, all will be pass in the all exaam'
# pattern = re.compile(r'al{2}')
# x = pattern.finditer(str)
# print(x)
# for match in x:
#     print(match)
#
# import re
# str = 'All the best, all will be pass in the all exaam'
# x = re.findall('al{2}',str)
# print(x)
# if x:
#     print('Match Found')
# else:
#     print('No Match Found')

################################
# import re
# str = 'All the best, all will stays be pass in the all exaam'
# pattern = re.compile(r'all|stays')
# x = pattern.finditer(str)
# print(x)
# for match in x:
#     print(match)
#
# import re
# str = 'All the best, all will be pass stays in the all exaam'
# x = re.findall('all|stays',str)
# print(x)
# if x:
#     print('Match Found')
# else:
#     print('No Match Found')

#output =
# <callable_iterator object at 0x000001E93FA37520>
# <re.Match object; span=(14, 17), match='all'>
# <re.Match object; span=(23, 28), match='stays'>
# <re.Match object; span=(44, 47), match='all'>
# ['all', 'stays', 'all']
# Match Found

#################################
#SPECIAL SEQUENCES#

# \A => Start of the string

# import re
# str = 'All the best, all will be pass stays in the all exaam'
# x = re.findall('\AAll',str)
# print(x)
# if x:
#     print('Match Found')
# else:
#     print('No Match Found')
#
# import re
# str = 'All the best, all will be pass stays in the all exaam'
# x = re.findall('^All',str)
# print(x)
# if x:
#     print('Match Found')
# else:
#     print('No Match Found')


###############################

#\b => Each word of beginning

# import re
# str = 'All the best, ainall will be ainpass stays in the all exaam'
# x = re.findall(r'\bain',str)
# print(x)
# if x:
#     print('Match Found')
# else:
#     print('No Match Found')
#
# import re as m
# str = 'All the best, ainallain will be ainpassain stays in the all exaam'
# x = m.findall(r'ain\b',str)
# print(x)
# if x:
#     print('Match Found')
# else:
#     print('No Match Found')

######################################
#\B => ending and betwen chalel but not starting
# import re
# str = 'All the best, ainall will be ainpainassain stays in the all exaam'
# x = re.findall(r'\Bain',str)
# print(x)
# if x:
#     print('Match Found')
# else:
#     print('No Match Found')
#
# #\B => Starting and inbetween but not ending
# import re
# str = 'All the best, ainall will be pass stays in the all exaam'
# x = re.findall(r'ain\B',str)
# print(x)
# if x:
#     print('Match Found')
# else:
#     print('No Match Found')


####################################
# import re
# txt = 'There is ainrrain in spaink for money gain'
# pattern = re.compile(r'ain\B')
# x = pattern.finditer(txt)
# print(x)
# if x:
#     print("Match Found")
# else:
#     print("Match don't Found")
#
# for match in x:
#     print(match)
# print(txt[23:27])
# print(txt[9:13])

#Output =>
# <callable_iterator object at 0x000001F8A4CD6890>
# Match Found
# <re.Match object; span=(9, 12), match='ain'>
# <re.Match object; span=(23, 26), match='ain'>
# aink
# ainr

#################################################
# import re
# str = 'It does what it says on the tin, and it does it really well. The book starts out with a walkthrough of the basic Python elements and data structures, working through variables, strings, numbers, lists, and tuples, outlining how you work with each of them.'
# pattern = re.compile(r'\Bin') #inbetween and ending
# x = pattern.finditer(str)
# print(x)
# for match in x:
#     print(match)
# print(str[29:32])
# print(str[154:157])
# print(str[180:183])
# print(str[218:222])
# print(str[220:223])

#######################################
# import re
# str = 'It does what it says on the tin, and it does it really well. The book starts out with a walkthrough of the basic Python elements and data structures, working through variables, strings, numbers, lists, and tuples, outlining how you work with each of them.'
# pattern = re.compile(r'in\B') #STARTING AND inbetweeN
# x = pattern.finditer(str)
# print(x)
# for match in x:
#     print(match)

###########################################
# \d => only digit
# import re
# str = 'I am a boy , my age is 56'
# pattern = re.compile(r'\d')
# x = pattern.finditer(str)
# if x:
#     print("++++++Match Found++++++")
# else:
#     print("Match Not Found")
# print(x)
# for math in x:
#     print(math)

###########################################
# \D => Return everthing without digit

# import re
# str = 'I am a boy ,65 23 11 22 431 my age is 56'
# pattern = re.compile(r'\D')
# x = pattern.finditer(str)
# if x:
#     print("++++++Processing++++++")
# else:
#     print("Loading")
# print(x)
# for math in x:
#     print(math)

# import re
# str = 'I am a boy ,65 23 11 22 431 my age is 56'
# x = re.findall('\D',str)
# print(x)
# if x:
#     print("Match Found")
# else:
#     print("Error")

###########################################
# \s => return space

# import re
# str = 'Iamabo65231122431myageis 56'
# x = re.findall('\s',str)
# print(x) #[' ']

###########################################
# \S => return everything without space

# import re
# str = 'I am a boy ,65 23 11 22 431 my age is 56'
# x = re.findall('\S',str)
# print(x)
# #output =>
# ['I', 'a', 'm', 'a', 'b', 'o', 'y', ',', '6', '5', '2', '3', '1', '1', '2', '2', '4', '3', '1', 'm', 'y', 'a', 'g', 'e', 'i', 's', '5', '6']

##########################################

#\w => return  alphabets , digit and underscore char but not  special char and space
#it return alphanumeric

# import re
# str = 'I am a boy_fg ,65 23 11 $ % @  22 431 my age is 56'
# x = re.findall('\w',str)
# print(x)

####################################
#\W => Return everything like char, space , except alphabet and digits
#return everything except alphanumeric

# import re
# str = 'I am a boy ,65 23 11  # $ %22 431 my age is 56'
# x = re.findall('\W',str)
# print(x)

##########################################
# \Z => String endswidth

# import re
# str = 'I am a boy , he is also a boy'
# x = re.findall('boy\Z',str)
# print(x)

#########################################
# [abc] => return only char enclosed in this []

# import re
# str = 'I am a boy ,65 23 11 22 431 my age is 56'
# x = re.findall('[aoy]',str)
# print(x) #['a', 'a', 'o', 'y', 'y', 'a']

#########################################
#[a-n] => give range

# import re
# str = 'I am a boy ,65 23 11 22 431 my age is 56'
# x = re.findall('[a-y]',str)
# print(x)
# # ['a', 'm', 'a', 'b', 'o', 'y', 'm', 'y', 'a', 'g', 'e', 'i', 's']

###############################
#[^arn] => return everything (digit,space,sp.char) except arn
# import re
# str = 'I am a boy ,65 23 11 22 431 my age is 56'
# x = re.findall('[^ary]',str)
# print(x)
#['I', ' ', 'm', ' ', ' ', 'b', 'o', ' ', ',', '6', '5', ' ', '2', '3', ' ', '1', '1', ' ', '2', '2', ' ', '4', '3', '1', ' ', 'm', ' ', 'g', 'e', ' ', 'i', 's', ' ', '5', '6']

#####################################
#[^a-n] => returns everything exceptt this range
#
# import re
# str = 'I am a boy ,65 23 11 22 431 my age is 56'
# x = re.findall('[^a-y]',str)
# print(x)
# ['I', ' ', ' ', ' ', ' ', ',', '6', '5', ' ', '2', '3', ' ', '1', '1', ' ', '2', '2', ' ', '4', '3', '1', ' ', ' ', ' ', ' ', '5', '6']

###################################
#[123] => returns 1 2 3
#
# import re
# str = 'I am a boy ,65 23 11 22 431 my age is 56'
# x = re.findall('[12345]',str)
# print(x)

##################################
#[0-9] => returns digit range from 0 to 9
#
# import re
# str = 'I am a boy ,65 23 11 22 431 my age is 56'
# x = re.findall('[2-6]',str)
# print(x)

# import re
# str = 'I am a boy ,65 23 11 22 431 my age is 56'
# x = re.findall('[2-6][2-4]',str)
# print(x) #['23', '22', '43']

#########################################
# import re
# str = "This is a sample string containing emails (user@domain.com), phone numbers (123-456-7890), and dates (DD/MM/YYYY). My email is alice@example.com and phone number is 555-123-4567. Today's date is 15/07/2024 and time 11 59 am. There are also some alphanumeric characters (A-z0-9) and special characters (!@#$%^&*)."
# x = re.findall('[0-9][0-9]',str)
# y = re.findall('[am]',str)
# print(f'x:{x} y:{y}')

#################################
#[a-zA-Z] => return small as well as capital alphabets
# import re
# str = "This is a sample string containing emails (user@domain.com), phone numbers (123-456-7890), and dates (DD/MM/YYYY). My email is alice@example.com and phone number is 555-123-4567. Today's date is 15/07/2024 and time 11 59 am. There are also some alphanumeric characters (A-z0-9) and special characters (!@#$%^&*)."
# x = re.findall('[a-zA-Z]',str)
# print(x)

#####################################
#[+] => Returns if any string contains + character

# import re
# str = 'This is a sample string containing emails (user@domain.com), phone numbers (123-456-7890), and dates (DD/MM/YYYY). My email is alice@example.com and phone number is 555+123+4567. Todays date is 15/07/2024.There are also some alphanumeric characters (A-z0-9) and special characters (!@=#$%^&*).'
# x = re.findall('[+]',str)
# print(x)


# import re
# str = 'This is a sample string containing emails (user@domain.com), phone numbers (123-456-7890), and dates (DD/MM/YYYY). My email is alice@example.com and phone number is 555+123+4567. Todays date is 15/07/2024.There are also some alphanumeric characters (A-z0-9) and special characters (!@=#$%^&*).'
# pattern = re.compile(r'[+]')
# x = pattern.finditer(str)
# print(x)
# for a in x:
#     print(a)

########################################
# '\.' or '[.]' => return the dot in the string

# import re
# str = 'This is a sample string containing emails (user@domain.com), phone numbers (123-456-7890), and dates (DD/MM/YYYY). My email is alice@example.com and phone number is 555+123+4567. Todays date is 15/07/2024.There are also some alphanumeric characters (A-z0-9) and special characters (!@=#$%^&*).'
# a = re.compile(r'\.')
# x =a.finditer(str)
# print(x)
# for b in x:
#     print(b)

# import re
# str = 'This is a sample string containing emails (user@domain.com), phone numbers (123-456-7890), and dates (DD/MM/YYYY). My email is alice@example.com and phone number is 555+123+4567. Todays date is 15/07/2024.There are also some alphanumeric characters (A-z0-9) and special characters (!@=#$%^&*).'
# a = re.compile(r'[.]')
# x =a.finditer(str)
# print(x)
# for b in x:
#     print(b)

#######################################
# '.' => return everything including space (alphabets,special characters , symbols and space

# import re
# str = 'This is a sample string containing emails (user@domain.com), phone numbers (123-456-7890), and dates (DD/MM/YYYY). My email is alice@example.com and phone number is 555+123+4567. Todays date is 15/07/2024.There are also some alphanumeric characters (A-z0-9) and special characters (!@=#$%^&*).'
# a = re.compile(r'.')
# x =a.finditer(str)
# print(x)
# for b in x:
#     print(b)

#####################################

# import re
# str = 'This is a sample string containing emails (user@domain.com), phone numbers (123-456-7890), and dates (DD/MM/YYYY). My email is alice@example.com,alice@exampleccom and phone number is 555+123+4567. Todays date is 15/07/2024.There are also some alphanumeric characters (A-z0-9) and special characters (!@=#$%^&*).'
# a = re.compile(r'alice@example.com')
# x =a.finditer(str)
# print(x)
# for b in x:
#     print(b)
#
# # . => any char
# # \. => only dot
# # [.] => only dot

#########################################

# import re
# str = 'This is a sample string containing emails (user@domain.com), phone numbers (123-456-7890), and dates (16/07/2024). My email is alice@example.com and phone number is 555+123+4567. Todays date is 15/07/2024.There are also some alphanumeric characters (A-z0-9) and special characters (!@=#$%^&*).'
# a = re.compile(r'\d{2}.\d{2}.\d{4}')
# x =a.finditer(str)
# print(x)
# for b in x:
#     print(b)

######################################
#
# import re
# str = 'This is a sample string containing emails (user@domain.com), phone numbers (123-456-7890), and dates (16/07/2024). My email is alice@example.com and phone number is 555+123+4567. Todays date is 15/07/2024.There are also some alphanumeric characters (A-z0-9) and special characters (!@=#$%^&*).'
# a = re.compile(r'\d{3}.\d{3}.\d{4}')
# x =a.finditer(str)
# print(x)
# for b in x:
#     print(b)

# import re
# str = 'This is a sample string containing emails (user@domain.com), phone numbers (123-456-7890), and dates (16/07/2024). My email is alice@example.com and phone number is 555+123+4567. Todays date is 15/07/2024.There are also some alphanumeric characters (A-z0-9) and special characters (!@=#$%^&*).'
# a = re.compile(r'\d{3}[+]\d{3}[+]\d{4}')
# x =a.finditer(str)
# print(x)
# for b in x:
#     print(b)

######################################

# import re
# pattern = re.compile(r'\d{3}[+]\d{3}[+]\d{4}')
# with open('data.txt') as f:
#     context = f.read()
#     x = pattern.finditer(context)
#     print(x)
#     for match in x:
#         print(match)

# import re
# pattern = re.compile(r'[^B]en')
# with open('data.txt') as f:
#     context = f.read()
#     x = pattern.finditer(context)
#     print(x)
#     for match in x:
#         print(match)
#
# print(context[83: 90])









