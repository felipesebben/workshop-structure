from pipeline.extract import extract_from_excel

dataframes_lists = extract_from_excel("data/input")
print(dataframes_lists)