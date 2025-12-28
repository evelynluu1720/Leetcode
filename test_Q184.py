import pandas as pd
from Q184_DepartmentHighestSalary import department_highest_salary

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

def test_department_highest_salary():
    result = department_highest_salary(employee, department)
    expected = pd.DataFrame({
        'Department':['IT','Sales','IT'],
        'Employee':['Jim','Henry','Max'],
        'Salary':[90000,80000,90000]
    })
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
