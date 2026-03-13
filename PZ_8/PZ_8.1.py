#Измените зарплату 'Brad' на 8500
sample_dict = {
 'emp1': {'name': 'Jhon', 'salary': 7500},
 'emp2': {'name': 'Emma', 'salary': 8000},
 'emp3': {'name': 'Brad', 'salary': 6500}
}
for key, value in sample_dict.items():
    if value['name'] == 'Brad':
        value['salary'] = 8500
        break
print(sample_dict)