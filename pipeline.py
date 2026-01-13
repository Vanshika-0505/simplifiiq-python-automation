from data_cleaning import clean_data
from web_fetcher import fetch_web_data
from summarizer import summarize_content
import os

DATA_DIR = "data"
OUTPUT_DIR = "output"

INPUT_CSV = os.path.join(DATA_DIR, "messy_input.csv")
VALID_CSV = os.path.join(OUTPUT_DIR, "cleaned_data.csv")
INVALID_CSV = os.path.join(OUTPUT_DIR, "unreliable_data.csv")
SOURCES_FILE = os.path.join(DATA_DIR, "sources.txt")
EXTRACTED_JSON = os.path.join(OUTPUT_DIR, "extracted_info.json")
REPORT_FILE = os.path.join(OUTPUT_DIR, "final_report.txt")

def main():
    print("Starting data cleaning...")
    clean_data(INPUT_CSV,VALID_CSV,INVALID_CSV)

    print("Fetching web data...")
    web_data=fetch_web_data(SOURCES_FILE, EXTRACTED_JSON)

    print("Summarizing content...")
    summary=summarize_content(web_data)

    print("Generating final report..")
    with open(REPORT_FILE,"w",encoding="utf-8")as f:
        f.write("Automation pipeline report\n")
        f.write("=========================\n\n")
        f.write(summary)
    

if __name__ == "__main__":
    main()