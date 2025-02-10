import os
import shutil
from datetime import datetime

# Global variables (cannot use 'from' keyword, so we use 'from_' and 'to_')
from_ = r"C:\path\to\your\source\folder"  # Change this to the source folder path
to_   = r"C:\path\to\your\destination\folder"  # Change this to the destination folder path

def ensure_files_exist():
    """
    Ensures that log.txt and record.txt exist in the current folder.
    Creates them if they do not exist.
    """
    if not os.path.isfile("log.txt"):
        with open("log.txt", "w", encoding="utf-8") as f:
            f.write("")  # Just create an empty file

    if not os.path.isfile("record.txt"):
        with open("record.txt", "w", encoding="utf-8") as f:
            f.write("")  # Just create an empty file

def add_daily_divider_if_needed():
    """
    Adds a divider to log.txt for a new day if today’s date hasn’t been logged yet.
    This helps keep daily logs separated with a clear marker.
    """
    today_str = datetime.now().strftime("%Y-%m-%d")
    with open("log.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Check if there's already a divider for today
    if any(today_str in line for line in lines):
        # Today’s date found somewhere in log, do not add new divider
        return

    # Otherwise, add a new divider for today
    divider_text = (
        f"\n----------------------------------------\n"
        f"|            {today_str}            |\n"
        f"----------------------------------------\n"
    )
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(divider_text)

def log_action(message):
    """
    Logs a message to log.txt with a timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def read_recorded_files():
    """
    Reads the record.txt file and returns a set of the recorded filenames.
    """
    with open("record.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return set(lines)

def write_to_record(filename):
    """
    Appends a filename to record.txt so we know it’s been copied before.
    """
    with open("record.txt", "a", encoding="utf-8") as f:
        f.write(filename + "\n")

def copy_new_files():
    """
    Copies files from the folder in 'from_' to the folder in 'to_'.
    - Only copies files that have not been copied before (based on record.txt).
    - Logs each action in log.txt.
    - Appends the name of each newly-copied file to record.txt.
    """
    ensure_files_exist()      # Make sure log.txt and record.txt exist
    add_daily_divider_if_needed()  # Add a daily divider in log.txt if necessary

    recorded_files = read_recorded_files()  # Already-copied files

    # List all files in the 'from_' directory
    if not os.path.isdir(from_):
        log_action(f"Source folder does not exist: {from_}")
        return

    if not os.path.isdir(to_):
        log_action(f"Destination folder does not exist: {to_}")
        return

    files_in_source = os.listdir(from_)

    # Filter out any directories; we only want files
    files_to_copy = [f for f in files_in_source 
                     if os.path.isfile(os.path.join(from_, f))]

    if not files_to_copy:
        log_action("No files found in source directory to process.")
        return

    # Go through each file, copy it if it’s not in record.txt
    for file_name in files_to_copy:
        if file_name in recorded_files:
            # Already copied before, skip
            continue
        
        source_file = os.path.join(from_, file_name)
        dest_file   = os.path.join(to_, file_name)

        try:
            shutil.copy2(source_file, dest_file)
            log_action(f"Copied file: {file_name} from {from_} to {to_}")
            write_to_record(file_name)
        except Exception as e:
            log_action(f"Error copying file: {file_name} - {str(e)}")

if __name__ == "__main__":
    copy_new_files()
