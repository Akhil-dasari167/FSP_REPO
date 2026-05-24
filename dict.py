emp = dict(name = 'akhil', roll_no = 417)
print(emp)
emp1 = {'name': 'akhil',
            'roll_no': 417,
            'class': 'Btrch'
        }
print(emp1['class'])
print(emp1.get('phone_number' , ' not   found'))
emp1['cphone_number']= 12345566788
print(emp1.keys())
print(emp1.values())
print(emp1.items())