from Q196_DeleteDuplicateEmails import delete_duplicate_emails
import pandas as pd

test_df = pd.DataFrame({
    'id':[1,2,3,4,5],
    'email':['john@example.com','bob@example.com','john@example.com','bob@example.com','john@example.com']
})

def test_delete_duplicate_emails():
    result = delete_duplicate_emails(test_df)
    expected = pd.DataFrame({
        'id':[1,2],
        'email':['john@example.com','bob@example.com']
})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))