from Q176_SecondHighestSalary import second_highest_salary
import pandas as pd
import pytest


# create data frame
employee = pd.DataFrame({
    'id': [1,2,3],
    'salary': [100,200,300]
})

employee2 = pd.DataFrame({
    'id': [1,2],
    'salary': [100,200]
})

def test_second_highest_salary():
    result = second_highest_salary(employee)
    assert result.iloc[0,0] == 200

def test_second_highest_salary2():
    result = second_highest_salary(employee2)
    assert result.iloc[0,0] == 100
