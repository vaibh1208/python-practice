# import time
# print(time.time())

# import time
# t =time.time()
# lt = time.localtime(t)
# print(t)
# print(lt)
# print(lt.tm_hour,'/',lt.tm_min,'/',lt.tm_sec)
# print(lt.tm_mday,'/',lt.tm_mon,'/',lt.tm_year)


# import time
# t = time.time()
# lt = time.localtime()
# at = time.asctime(lt)
# print(t)
# print(lt)
# print(at)

# import time
# print(time.asctime(time.localtime(time.time())))

# import time
# for i in range(100):
#     print(time.asctime(time.localtime(time.time())))
#     time.sleep(1)

# import datetime
# print(datetime.datetime.now())

# if you wanna show 10am to 2pm as working hours
# from datetime import datetime as dt
# d1 = dt(dt.now().year,dt.now().month,dt.now().day,10)
# d2 = dt.now()
# d3 = dt(dt.now().year,dt.now().month,dt.now().day,14)
# print(d1)
# print(d2)
# print(d3)
#
# if d1<d2<d3:
#     print("Working Hour")
# else:
#     print("Non Working Hours")


# alternative
# from datetime import datetime as dt
# if (dt.now().year,dt.now().month,dt.now().day,6) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,14):
#     print("Welcome to the office")
# else:
#     print("You ran out of the working hours")

# import datetime
# print(dir(datetime))
# d1 = datetime.timezone()
# print(d1)

# from datetime import datetime          #datetime --> class
# a = datetime(2024,7,4,21,45,56,78965)  #a --> object
# print('Timestamp =', a.timestamp())
# print('Year = ', a.year)
# print('month = ', a.month)
# print('date = ', a.date)
# print('hour = ', a.hour)
# print('minute = ', a.minute)
# print('second = ', a.second)
# print('microsecond = ', a.microsecond)


# from datetime import datetime, date #---> datetime and date are two classes
# where t1 t2 t3 t4 t5 t6 are objects
# t1 = date(year= 2017,month = 8,day = 28)
# t2 = date(year = 2017,month = 8,day = 30)
# t3 = t2 - t1
# print('t3 = ',t3)
#
# t4 = datetime(year= 2017,month = 8,day = 28,hour= 17,minute = 8,second = 28)
# t5 = datetime(year = 2017,month = 8,day = 30,hour = 17,minute = 8,second = 30)
# t6 = t4 - t5
# print('t6 = ',t6)
#
# print("TYPE OF THE OBJECT")
# print("Type of t3 =",t3)
# print("Type of t6 =",t6)


# from datetime import timedelta
# t1 = timedelta(weeks = 3,hours = 12,minutes = 54, seconds = 21)
# t2 = timedelta(hours = 10,minutes = 34)
# t3 = t1 - t2
# print('t3 = ',t3)     #t3 =  21 days, 2:20:21

from datetime import timedelta as td
t1 = td(seconds=54)
t2 =td(seconds = 59)
t3 = t1 - t2
print(f'Difference is ', t3)
print(f'Difference is ', abs(t3))
