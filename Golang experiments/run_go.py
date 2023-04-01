"""
Create a python application that can run any go application in any directory when inputted the file of the application.
"""

import os
import sys

def run_go(file):
    """
    Run a go application
    """
    os.system("go run " + file)

if __name__ == "__main__":
    run_go(sys.argv[1])