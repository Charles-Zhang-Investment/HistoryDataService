"""Combines additional data with existing data and put it back to existing data"""
import os
import sys

import pandas

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Requires source file and appendix file.")
    else:
        source_file = os.path.abspath(sys.argv[1])
        appendix_file = os.path.abspath(sys.argv[2])

        df = pandas.read_csv(source_file) # TODO: Set index
        app = pandas.read_csv(appendix_file) # TODO: Set index, remove all NA rows
        # TODO: Just put the columns from app to df - picking only those columns that's already present in original df
        
        # Save the file back to source_file
        combined.to_csv(source_file)
        # TODO: Report how many rows are modified (or how many new rows are added)