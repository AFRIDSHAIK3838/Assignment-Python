import sys
from file_op import file_operation
from pandas_op import pandas_operation

def main():
    if len(sys.argv) < 2:
        print("No argument provided")
        print("Use --fo for File Operations (.txt)")
        print("Use --p for Pandas Operations (.csv)")
        return

    arg = sys.argv[1]
    if arg in ["--fo", "file-ops"]:
        file_operation()
    elif arg in ["--p", "Pandas"]:
        pandas_operation()
    else:
        print("Invalid argument provided.")

if __name__ == "__main__":
    main()
