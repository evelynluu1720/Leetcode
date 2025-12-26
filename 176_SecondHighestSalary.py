import pandas as pd

# create data frame
employee = pd.DataFrame({
    'id': [1,2,3],
    'salary': [100,200,300]
})

# solution - define function
def second_highest_salary(employee: pd.DataFrame):
    sorted_salary = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(sorted_salary) <=1:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        return pd.DataFrame({'SecondHighestSalary': [sorted_salary[1]]})
    
result = second_highest_salary(employee)
print(result)
