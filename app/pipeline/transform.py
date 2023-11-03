"""This is our transform module."""
from typing import List

import pandas as pd


def concatenate_data_frames(
    data_frame_list: List[pd.DataFrame],
) -> pd.DataFrame:
    """Transform a list of DataFrames to a single Dataframe."""
    return pd.concat(data_frame_list, ignore_index=True)
