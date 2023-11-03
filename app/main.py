from pipeline.extract import extract_from_excel
from pipeline.transform import concatenate_data_frames
from pipeline.load import load_excel

if __name__ == "__main__":
    dataframes_list = extract_from_excel("data/input")
    data_frame = concatenate_data_frames(dataframes_list)
    load_excel(data_frame, "data/output", "output")
