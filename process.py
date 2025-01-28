import sqlite3
import pandas as pd
import json

def process(input_file_path, processed_file_path, data_base_path):
    df = pd.read_csv(filepath_or_buffer=input_file_path)
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Delete rows if the subject scores are not valid
    score_columns = ['math score', 'reading score', 'writing score']
    for col in score_columns:
        df = df[(df[col] >= 0) & (df[col] <= 100)]

    # Encode categorical values
    categorical_columns = ['gender', 'race/ethnicity', 'parental level of education', 'lunch',
                           'test preparation course']
    encoding_mapping = {}
    for col in categorical_columns:
        unique_values = df[col].unique()
        mapping = {val: idx for idx, val in enumerate(unique_values)}
        encoding_mapping[col] = mapping
        df[col] = df[col].map(mapping)

    # Save encoded values for reference
    encoding_path = 'out/encoding_mapping.json'
    with open(encoding_path, 'w') as f:
        json.dump(encoding_mapping, f, indent=4)

    # Save the processed dataset
    df.to_csv(processed_file_path, index=False)

    # Transfer data to the database
    with sqlite3.connect(data_base_path) as conn:
        df.to_sql('students_performance', conn, if_exists='replace', index=False, chunksize=500)
        print(f"The data has been successfully saved to DB {data_base_path} in the table students_performance.")
    return df
