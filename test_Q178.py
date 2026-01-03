import pandas as pd
from Q178_RankScores import order_scores

# create example df
scores = pd.DataFrame({
    'id':[1,2,3,4,5,6],
    'score':[3.5,3.65,4.0,3.85,4,3.65]
})

def test_order_scores():
    result = order_scores(scores)
    expected = pd.DataFrame({
        'score':[4.,4.,3.85,3.65,3.65,3.5],
        'rank':[1,1,2,3,3,4]
    })
    expected['rank'] = expected['rank'].astype('float64')
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
