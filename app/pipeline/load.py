"""This is our load module."""
import os

import pandas as pd


def load_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> str:
    """
    Receive DataFrame and save it as an Excel file.

    args:
    data_frame (pd.DataFrame): dataframe to be exported as Excel file
    output_path (str): path in which the file will be exported
    file_name (str): name of file to be exported


    return "File successfully saved"
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    data_frame.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
    return 'File successfully saved'
