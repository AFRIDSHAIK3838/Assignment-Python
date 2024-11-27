import os
from datetime import datetime

INSTRUCTIONSFILE = "instructions.txt"

def file_operation():
    while True:
        print("\nOptions:")
        print("1. Adding an instruction")
        print("2. Execute instructions")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            instruction = input("Enter your instruction: ").strip()
            with open(INSTRUCTIONSFILE, "a") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{instruction} | {timestamp}\n")
            print("Instruction logged!")

        elif choice == "2":
            if not os.path.exists(INSTRUCTIONSFILE):
                print("No instructions")
            else:
                with open(INSTRUCTIONSFILE, "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        
                        try:
                            instruction, timestamp = line.strip().rsplit(" | ", 1)
                            if instruction.lower() == "time":
                                print(f"Current Time: {datetime.now().strftime('%H:%M:%S')}")
                            elif instruction.lower() == "date":
                                print(f"Current Date: {datetime.now().strftime('%Y-%m-%d')}")
                            else:
                                raise ValueError("Unknown instruction")
                        except Exception as error:
                            print(f"Error with instruction: {instruction}")
                            print(f"Error details: {error}")
        
        elif choice == "3":
            print("Exit")
            break

        else:
            print("Invalid choice. Please try again.")
