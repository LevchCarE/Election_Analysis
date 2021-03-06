

import csv
import os


# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources_modulo_3", "election_results.csv")

 # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)