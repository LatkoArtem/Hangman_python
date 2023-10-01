salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
increase = 30
new_salary_list = []
indexsation_list = []
for salary in salary_list:
    indexation = round(salary * increase / 100, 2)
    new_salary = round(salary + indexation, 2)
    indexsation_list.append(indexation)
    new_salary_list.append(new_salary)
l = len(salary_list)
print("Salary table:")
for a in range(l):
    print("%s   %s   %s" % (salary_list[a], new_salary_list[a], indexsation_list[a]))