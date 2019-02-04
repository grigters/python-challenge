import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

#-------------------
# Set variable for output file
output_file = os.path.join("Resources", "output.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])