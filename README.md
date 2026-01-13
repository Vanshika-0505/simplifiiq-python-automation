# SimplifiIQ Python Automation Assignment

## Overview
This project is a Python-based automation pipeline developed for the SimplifiIQ internship assignment.  
It demonstrates data cleaning, web data extraction, and AI-based summarization using a modular and scalable design.

## Contents
- `pipeline.py` — Main automation controller that runs the full workflow end-to-end  
- `data_cleaning.py` — Cleans and validates messy CSV data and separates unreliable records  
- `web_fetcher.py` — Fetches and extracts content from online sources  
- `summarizer.py` — Summarizes extracted content using Gemini AI  
- `data/messy_input.csv` — Sample messy input dataset (10+ rows with invalid entries)  
- `data/sources.txt` — List of URLs used for web data extraction  
- `output/cleaned_data.csv` — Cleaned and validated records  
- `output/unreliable_data.csv` — Invalid records with rejection reasons  
- `output/extracted_info.json` — Extracted web content  
- `output/final_report.txt` — Final automated summary report  
- `requirements.txt` — Python dependencies  
- `README.md` — Project documentation  
- `reflection.txt` — Short reflection on learning and challenges  

---

## How to Run (Setup)

### 1. Create a Python Virtual Environment 
```bash
python -m venv venv
venv\Scripts\activate           

### 2. Install Dependencies
```bash
pip install -r requirements.txt

Dependencies used:
pandas
requests
beautifulsoup4
google-generativeai
python-dotenv

### 3.Configure Environment Variables
Create a .env file in the project root and add:
GEMINI_API_KEY=your_api_key_here

## Part A — Data Cleaning & Automation
Files:
data_cleaning.py, pipeline.py, data/messy_input.csv
Run:
```bash
python pipeline.py

###Description
- Reads messy CSV input data
- Validates each record using defined rules
- Separates valid and unreliable records
- Assigns a quality tag (High / Medium / Low)
- Writes cleaned and rejected data to the output/ directory

###Validation Rules
- Name must not be empty
- Email must match a regex pattern
- Age must be between 18 and 60
- Score must be between 0 and 100

###Outputs
- output/cleaned_data.csv
- output/unreliable_data.csv

##Assumptions
- Invalid records are excluded rather than corrected
- Missing or malformed values are treated as data errors
- No data imputation is performed

##Part B — Web Data Extraction & AI Summarization

###Description
- Reads URLs from data/sources.txt
- Fetches and parses web pages
- Extracts page title and first meaningful paragraph
- Summarizes extracted content using Gemini AI
- Generates a final automated report

###Outputs
- output/extracted_info.json
- output/final_report.txt

###Notes
- Only publicly accessible web pages are used
- Timeout and error handling are implemented
- Failure of one URL does not stop the pipeline
- AI summarization depends on Gemini API availability

##Design Choices
- Modular file structure for clarity and maintainability
- Regex-based email validation for accuracy
- Defensive programming to prevent pipeline failures
- Environment variables used for secure API handling

##Limitations
- Web scraping is basic and text-focused
- No advanced logging or unit tests included
- AI-generated summaries depend on external API responses