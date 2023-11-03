import pandas as pd
from app.pipeline.transform import concatenate_data_frames
from pandas.testing import assert_frame_equal

df_1 = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
df_2 = pd.DataFrame({"col1": [5, 6], "col2": [7, 8]})

def test_df_list_concatenation():
    """
    Use arrange-act-assert with `pandas.testing.assert_frame_equal` and compare size of dataframes
    for the function `concatenate_data_frames`.
    """
    
    df_list = [df_1, df_2]
    arrange = pd.concat(df_list, ignore_index=True)

    act = concatenate_data_frames(df_list)

    assert act.shape == (4, 2)
    assert_frame_equal(arrange, act)
  