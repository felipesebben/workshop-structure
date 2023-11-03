import pandas as pd
from typing import List

def concatenate_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Function to transform a list of DataFrames to a single Dataframe.
    """
    return pd.concat(data_frame_list, ignore_index=True)