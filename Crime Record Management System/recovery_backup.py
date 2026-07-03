# Import shutil module for copying files
import shutil

# Import os module to work with files and directories
import os


# Function to create backup of project data files
def create_backup():

    try:

        # List of all files that need to be backed up
        files = [
            "criminals.txt",
            "fir.txt",
            "cases.txt",
            "evidence.txt",
            "wanted.txt",
            "victims.txt"
        ]

        # Traverse each file in the list
        for file in files:

            # Create backup file name by replacing .txt with _backup.txt
            backup_file = file.replace(".txt", "_backup.txt")

            # Copy original file to backup file
            shutil.copy(file, backup_file)

        # Display success message after backup completion
        print("Backup Created Successfully!")

    # Handle error if one or more files are missing
    except FileNotFoundError:

        print("Some files not found! Backup failed.")


# Function to restore original files from backup
def restore_backup():

    try:

        # List of original project files
        files = [
            "criminals.txt",
            "fir.txt",
            "cases.txt",
            "evidence.txt",
            "wanted.txt",
            "victims.txt"
        ]

        # Traverse each original file
        for file in files:

            # Generate corresponding backup file name
            backup_file = file.replace(".txt", "_backup.txt")

            # Check whether backup file exists
            if os.path.exists(backup_file):

                # Restore original file by copying backup file
                shutil.copy(backup_file, file)

        # Display success message after restoration
        print("Data Restored Successfully!")

    # Handle any unexpected errors during restoration
    except Exception as e:

        # Display the error message
        print("Restore Failed:", e)