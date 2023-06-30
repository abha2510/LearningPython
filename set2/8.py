employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
dict = {}

for emp in employees:
    dict[emp] = defaults.copy()

print(dict)
