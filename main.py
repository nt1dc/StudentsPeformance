import subprocess

from process import process
from quality import evaluate_data_quality

INPUT_CVS = "data/StudentsPerformance.csv"

DATA_PATH = "./data/customer_segmentation_data.csv"
PROCESSED_PATH = "./out/processed_data.csv"
DATABASE_PATH = "./out/database.db"


def run_streamlit_app(data_path):
    try:
        # Run the Streamlit script using subprocess
        subprocess.run(["streamlit", "run", "dash.py", "--", data_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError:
        print("Streamlit command not found. Ensure Streamlit is installed and added to your PATH.")


if __name__ == '__main__':
    df = process(INPUT_CVS, PROCESSED_PATH, DATABASE_PATH)
    evaluate_data_quality(df)
    run_streamlit_app(PROCESSED_PATH)
