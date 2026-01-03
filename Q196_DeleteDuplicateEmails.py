import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame):
    # person = person.sort_values(by='email', ascending=True)
    person['rank'] = person.groupby('email').rank(method='first', ascending=True)
    person = person[person['rank']==1.0]
    return person[['id','email']]

def delete_duplicate_emails_2(person: pd.DataFrame):
    person = person.sort_values(by='id', ascending=True)
    person['rank'] = person.groupby('email').cumcount()
    person = person[person['rank']==0] # only keep first unique record
    return person[['id','email']]