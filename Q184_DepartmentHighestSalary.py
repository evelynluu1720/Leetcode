import pandas as pd

# define function
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame):
    '''
    find higest salary per each department <- sort by salary and departmentId <- split into separate search for each department
    join with department table to get department name
    '''
    employee['salaryRank'] = employee.groupby('departmentId')['salary'].rank(ascending=False, method='min')
    df_filter = employee[employee['salaryRank'] == 1]
    df_merged = pd.merge(df_filter, department, left_on='departmentId', right_on='id', how='left')
    df_reordered = df_merged[['name_y','name_x','salary']].rename(columns={
        'name_y':'Department',
        'name_x':'Employee',
        'salary':'Salary'
    })
    return df_reordered