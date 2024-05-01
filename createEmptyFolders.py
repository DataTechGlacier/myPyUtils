import os
import sys


def create_folders(target_location, folder_names):
    try:
        # Check if target location exists
        if not os.path.exists(target_location):
            print("Target location does not exist.")
            return

        # Create folders
        for folder_name in folder_names:
            folder_path = os.path.join(target_location, folder_name)
            os.makedirs(folder_path)
            print(f"Folder '{folder_name}' created at {folder_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Check if arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python program.py <target_location> <folder_name1> <folder_name2> ...")
        sys.exit(1)

    # Extract target location and folder names from command-line arguments
    target_location = sys.argv[1]
    folder_names = sys.argv[2:]

    # Call create_folders function
    create_folders(target_location, folder_names)