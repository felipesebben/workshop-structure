"""This is our extraction module."""
import glob  # list files
import os  # to manipulate files and folders
from typing import List

import pandas as pd

path = 'data/input'


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Read files from a `data/input` folder and return a list of DataFrames.

    Args: `input_path (str): folder path with files

    Return: DataFrame list
    """
    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


if __name__ == '__main__':
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)
