import pandas as pd

# create example df
employee = pd.DataFrame({
    'id':[1,2,3,4,5],
    'name':['Joe','Jim','Henry','Sam','Max'],
    'salary':[70000,90000,80000,60000,90000],
    'departmentId':[1,1,2,2,1]
})

department = pd.DataFrame({
    'id':[1,2],
    'name':['IT','Sales']
})

# define function
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame):
    '''
    find higest salary per each department <- sort by salary and departmentId <- split into separate search for each department
    join with department table to get department name
    '''