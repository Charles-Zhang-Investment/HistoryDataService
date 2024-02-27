"""
Validate time series data in a folder.
"""

import os
import sys

import pandas

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Not enough arguments")
    else:
        source_folder = sys.argv[1]
        # Enumerate files in folder and see whether there is any NA present
        for name in os.listdir(source_folder):
            filename, file_extension = os.path.splitext(name)
            # Only process csv files
            if file_extension == ".csv":
                # Read as pandas df and let df decide whether data is valid
                df = pandas.read_csv(os.path.join(source_folder, name))
                if df.isnull().values.any():
                    print(f"{name} contains invalid data.")