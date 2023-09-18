import os

def list_files_and_directories(directory):
    for root, _, files in os.walk(directory):
        print(f"Directory: {root}")
        for file in files:
            print(f"  File: {file}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    list_files_and_directories(current_directory)
