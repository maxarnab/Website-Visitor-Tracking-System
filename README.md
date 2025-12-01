# Website Visitor Tracking System

A Python mini project that processes a website visit CSV file to track unique users per website.  
This project demonstrates practical data cleaning, CSV handling, and use of Python data structures to analyze real-world website traffic.

---

## Features

- Reads and processes a website visit CSV file
- Removes duplicate `(user_id, website)` entries
- Counts unique users per website
- Handles multiple websites in a single dataset
- Uses only standard Python libraries
- Outputs results as a list of tuples: `(website, unique_visitor_count)`

---

## Project Structure

project/
├── main.py
├── example.csv
└── README.md

---

## Requirements

- Python 3.7 or higher  
- No external packages required

---

## CSV Format

The script expects a CSV file with the following columns:

- `user_id`  
- `website`  

If your column names differ, you can adjust the code in `main.py` accordingly.

**Example `example.csv`:**

user_id,website  
101,google.com  
102,openai.com  
101,google.com  
103,github.com  
102,openai.com  

---

## How to Use

1. Place your CSV file in the project directory.  
2. Update the filename inside `main.py` if needed.  
3. Run the script:



##Purpose

This project is designed to demonstrate core data processing techniques in Python, including CSV parsing, data cleaning, and the use of sets and dictionaries.
It is suitable for learners and anyone exploring basic web analytics or data engineering tasks.

```bash
python main.py
