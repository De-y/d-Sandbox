"""
Create a setup application with a progress bar. As well the setup asking questions to the user about what you would like to call a certain project and move files from 'quantum_root_files' to the current users working directory. Do NOT use argparse, just use input
"""

import os
import sys
import shutil
import time

# Import the progress bar from the progress_bar.py file.
from tqdm import tqdm

# Get the current working directory.
cwd = os.getcwd()

# Get the path to the quantum_root_files folder.
quantum_root_files_path = './quantum_root_files'


def main():
    print("Welcome to Quantum Setup.")

    # Ask the user what they would like to call their project.
    project_name = input("What would you like to call your project? ")

    # Create a new folder with the name of the project.
    os.mkdir(project_name)

    # Move all the files from the quantum_root_files folder to the new project folder.
    for file in os.listdir(quantum_root_files_path):
        shutil.move(f'{quantum_root_files_path}/{file}', f'{cwd}/{project_name}/{file}')
    
    # Remove the quantum_root_files folder.
    os.rmdir(quantum_root_files_path)

main()