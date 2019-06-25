import csv


# lista
with open('employee.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',',
                                 quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accouting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
    employee_writer.writerow(['Elvis Presley', 'Music', 'March'])

print('Feito...')