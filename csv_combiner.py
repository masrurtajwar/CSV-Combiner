import csv
import sys
import os

def combine_csv(filenames): # Function to combine the rows from multiple CSV files

    combined = [] # List to store the combined rows

    for filename in filenames: # Iterate through each file

        with open(filename, 'r') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip the header row
            
            for row in reader: # Add each row from the file along with its filename

                combined.append(row + [os.path.basename(filename)])
    return combined

def write_csv(rows): # Function to write the combined rows to stdout

    writer = csv.writer(sys.stdout)
    writer.writerow(['email_hash', 'category', 'filename'])
    writer.writerows(rows)

if __name__ == '__main__':
    filenames = sys.argv[1:] # Get the filenames from command line arguments
    combined = combine_csv(filenames) # Combine the rows from multiple files
    write_csv(combined) # Write the combined rows to stdout
