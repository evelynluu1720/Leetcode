import pandas as pd

# create example df
employees = pd.DataFrame({
    'emp_id':[1,1,1,2,2],
    'event_day':['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09'],
    'in_time':[4,55,1,3,47],
    'out_time':[32,200,42,33,74]
})

def total_time(employees: pd.DataFrame):
    employees['time_difference'] = employees['out_time'] - employees['in_time']
    total_time = employees.groupby(['event_day','emp_id']).sum()
    total_time = total_time.reset_index()[['event_day', 'emp_id', 'time_difference']].rename(columns={'event_day':'day', 'time_difference':'total_time'})
    return total_time

# print(total_time(employees))

def total_time2(employees: pd.DataFrame):
    employees['time_difference'] = employees['out_time'] - employees['in_time']
    total_time = employees.groupby(['event_day','emp_id'])['time_difference'].sum()
    total_time = total_time.reset_index().rename(columns={'event_day':'day','time_difference':'total_time'})
    return total_time

print(total_time2(employees))