import os
import pandas as pd

def pandas_operation():
    while True:
        print("\nEnter one of the Options:")
        print("1.Open/Read CSV")
        print("2.Exit")
        choice = input("Enter 
                       +
                       1your choice:").strip()

        if choice == "1":
            file_name = input("Enter the File Name.Extension:").strip()
            if not os.path.exists(file_name):
                print("No such file")
            else:
                try:
                    df = pd.read_csv(file_name)
                    print("\nCSV Content:")
                    print(df)
                except Exception as e:
                    print(f"Error reading file: {e}")

        elif choice == "2":
            print("Exit")
            break

        else:
            print("Invalid. Please try again.")
