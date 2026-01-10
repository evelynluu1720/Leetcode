import pandas as pd

# create example table
account = pd.DataFrame({
    'account_id': [3,2,8,6],
    'income': [108939, 12747, 87709, 91796]
})

def count_salary_categories(account: pd.DataFrame):
    category = ['Low Salary', 'Average Salary', 'High Salary']
    account['category'] = account['income'].map(
        lambda x: 'Low Salary' if x <20000 else ('High Salary' if x >50000 else 'Average Salary'))
    account['category'] = pd.Categorical(account['category'], categories=category, ordered=True)
    category_counts = account['category'].value_counts().reset_index(name='accounts_count')
    return category_counts

# print(count_salary_categories(account))

def count_salary_categories2(account: pd.DataFrame):
    # count each category manually
    low = len(account[account['income'] <20000])
    high = len(account[account['income'] >50000])
    ave = len(account) - low - high

    # create value count df
    categories_count = pd.DataFrame({
        'category':['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count':[low, ave, high]
    })

    return categories_count

print(count_salary_categories2(account))