import pandas as pd
from typing import List

"""
Function to transform a list of DataFrames to a single Dataframe.
"""

def concatenate_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)