# import csv
#
# with open('student.txt') as csv_file :
#     csv_reader = csv.reader(csv_file, delimiter = ',')
#     line_count = 0
#     for row in csv_reader :
#         if line_count == 0:
#             print(f'Column Name are {",".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]},{row[1]},{row[2]}')
#             line_count += 1
#
# print(f'Processes line are {line_count} lines')



# import pandas
# df = pandas.read_csv('Python.csv')
# print(df)

#How to write the data

# import csv

# with open('Python1.csv','w') as csvfile:
#     fn = ['First Name','Last Name','Rank']
#     writer = csv.DictWriter(csvfile,fieldnames = fn)
#
#     writer.writeheader()
#     writer.writerow({'Rank':'B','First Name':'Onkar','Last Name':'Nakate'})
#     writer.writerow({'Rank':'B','First Name':'Parker','Last Name':'Brain'})
#     writer.writerow({'Rank':'B','First Name':'Shweta', 'Last Name':'Bhanap'})
#     writer.writerow({'Rank':'B','First Name':'Vaishanv','Last Name':'Dhotre'})
#
# print('Writing Complete')


# import csv
# with open('Python2.csv','w') as csvfile:
#     fn = ['First Name','Last Name','Rank']
#     writer = csv.DictWriter(csvfile, fieldnames= fn)
#     writer.writeheader()
#     data =[{'Rank':'B','First Name':'Onkar','Last Name':'Nakate'},{'Rank':'A','First Name':'Vaibhav','Last Name':'Dhotre'},{'Rank':'B','First Name':'Shweta','Last Name':'Bhanap'},{'Rank':'B','First Name':'Aarush','Last Name':'Gaikwad'}]
#
#     writer.writerows(data)
# print('Done')

###########################################
# import csv
# with open('student.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Coumn names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]},{row[1]},{row[2]}')
#             line_count += 1
# print(f'Processed {line_count} lines')

#
# import pandas
# df = pandas.read_csv('Python2.csv')
# print(df)

# import csv
# with open('Python45.csv','w') as csvfile:
#     fn = ['First Name','Last Name','Rank']
#     writer = csv.DictWriter(csvfile,fieldnames = fn)
#
#     writer.writeheader()
#     writer.writerow({'Rank':'B','First Name':'Vaibhav','Last Name':'Dhotre'})
#     writer.writerow({'Rank':'B','First Name':'Parker','Last Name':'Brain'})
#     writer.writerow({'Rank':'B','First Name':'Shweta', 'Last Name':'Bhanap'})
#     writer.writerow({'Rank':'B','First Name':'Vaishanv','Last Name':'Dhotre'})
#
# print('Writing Complete')


# import csv
# with open('Python56.csv','w') as csvfile:
#     fn = ['First Name','Last Name','Rank']
#     writer = csv.DictWriter(csvfile,fieldnames = fn)
#
#     writer.writeheader()
#     data =[{'Rank':'B','First Name':'Onkar','Last Name':'Nakate'},{'Rank':'A','First Name':'Vaibhav','Last Name':'Dhotre'},{'Rank':'B','First Name':'Shweta','Last Name':'Bhanap'},{'Rank':'B','First Name':'Aarush','Last Name':'Gaikwad'}]
#     writer.writerows(data)
#
# print('Writing Complete')