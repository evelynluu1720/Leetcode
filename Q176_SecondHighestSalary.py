import pandas as pd

# solution - define function
def second_highest_salary(employee: pd.DataFrame):
    sorted_salary = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(sorted_salary) <=1:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        return pd.DataFrame({'SecondHighestSalary': [sorted_salary.iloc[1]]})
