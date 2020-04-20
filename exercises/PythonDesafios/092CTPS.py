from datetime import datetime
employee = {}
employee['name'] = str(input('Name: '))
birthday = int(input('Year of Birthday: '))
employee['age'] = datetime.now().year - birthday
employee['pps'] = int(input('PPS Number (0 for none): '))
if employee['pps'] != 0:
    employee['hire'] = int(input('Year of hire: '))
    employee['salary'] = float(input('Salary: '))
    employee['retirement'] = employee['hire'] - birthday + 35
print('-=' * 30)
for k, v in employee.items():
    print(f'{k} has the value {v}.')
