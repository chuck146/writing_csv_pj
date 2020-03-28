import csv
import urllib.request as request
r = request.urlopen(https://raw.githubusercontent.com/jamiec83/Stats-Calculator/commits/master)
reader = csv.reader(r)
for line in reader:
    print(line)
with open('employee_file_dict.csv', mode='w') as employee_file:
    fieldnames = ['name', 'dept', 'birth_month']
    employee_writer = csv.DictWriter(employee_file, fieldnames=fieldnames)

    employee_writer.writeheader()
    employee_writer.writerow({'name':'John Smith', 'dept':'Accounting', 'birth_month':'November'})
    employee_writer.writerow({'name':'Erica Meyers', 'dept':'IT', 'birth_month':'March'})
    

