# Import the single_output function from the single_output module
from single_output import single_output
import csv
from tqdm import tqdm

# Get user input
input_file_name = input("What is the name of your TSV file located in folder 'input' that you would like to process (do not include .tsv)? ")
output_file_name = input("What is the name of your output CSV file should be (do not include .csv)? ")
has_header = input("Does the TSV file have a header? (yes/no): ").strip().lower()

input_file_path = f"input/{input_file_name}.tsv"

# Specify the tab character as the delimiter
delimiter = '\t'

# Count the number of rows in the file for progress tracking
with open(input_file_path, 'r') as tsv_file:
    row_count = sum(1 for _ in tsv_file)

if has_header == 'yes':
    print(f"Total amount of rows: {row_count-1}")
    # The TSV file has a header, so we read it and skip the first row
    header = None
    with open(input_file_path, 'r') as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter=delimiter)
        header = next(tsv_reader)  # Read the header row

    # Process the data (excluding the header) with a progress bar
    with open(input_file_path, 'r') as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter=delimiter)
        next(tsv_reader)  # Skip the header row
        for row in tqdm(tsv_reader, total=row_count - 1, desc="Processing"):
            # Process each data row here
            single_output(row, output_file_name)  # Call single_output function with row and output_file_name
else:
    print(f"Total amount of rows: {row_count}")
    # The TSV file does not have a header, so we process it as-is with a progress bar
    with open(input_file_path, 'r') as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter=delimiter)
        for row in tqdm(tsv_reader, total=row_count, desc="Processing"):
            # Process each data row here
            single_output(row, output_file_name)  # Call single_output function with row and output_file_name
            
print("All done! 🎉 Thank you!")