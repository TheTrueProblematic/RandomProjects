import os
import shutil
import time
from datetime import datetime

# ====== Global Variables ======
from_ = r"C:\path\to\your\source\folder"  # Change this to the source folder path
to_   = r"C:\path\to\your\destination\folder"  # Change this to the destination folder path

# Default run time: 4:00 AM
SCHEDULED_TIME = "04:00"  # Format "HH:MM" (24-hour time)


# ====== Functions ======
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
    Adds a divider to log.txt for a new day if today's date hasn't been logged yet.
    Helps keep daily logs separated with a clear marker.
    """
    today_str = datetime.now().strftime("%Y-%m-%d")
    with open("log.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Check if there's already a divider for today
    if any(today_str in line for line in lines):
        # Today's date found somewhere in log, do not add new divider
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
    Reads the record.txt file and returns a set of recorded filenames.
    """
    with open("record.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return set(lines)


def write_to_record(filename):
    """
    Appends a filename to record.txt so we know it's been copied before.
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
    ensure_files_exist()           # Make sure log.txt and record.txt exist
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

    # Go through each file, copy it if it's not in record.txt
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


def run_daily():
    """
    Keeps the script alive and runs `copy_new_files()` each day at SCHEDULED_TIME.
    """
    # Parse the scheduled time (HH:MM)
    run_hour, run_minute = map(int, SCHEDULED_TIME.split(":"))
    log_action(f"Bot started. Will run daily at {SCHEDULED_TIME}.")

    while True:
        now = datetime.now()
        # Check if the current time matches the scheduled time
        if now.hour == run_hour and now.minute == run_minute:
            # Run the copying process
            copy_new_files()

            # Sleep for 60 seconds so we don't trigger multiple times in the same minute
            time.sleep(60)
        else:
            # Check again in 30 seconds
            time.sleep(30)


# ====== Main Entry Point ======
if __name__ == "__main__":
    run_daily()
