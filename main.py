import pandas as pd
from tabula import read_pdf

# Path to your PDF file
pdf_path = r"D:\Data\Library\Finance\Fiverr\2023_Q3.pdf"

# Read PDF file using tabula
try:
    # 'pages' argument is set to 'all' to read all pages; adjust as needed
    df = read_pdf(pdf_path, pages='2', multiple_tables=True)

    # Print each table found in the PDF
    for table in df:
        print(table)
        print("\n------------------\n")
except Exception as e:
    print(f"An error occurred: {e}")
