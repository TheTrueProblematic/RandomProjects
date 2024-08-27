import os
import whisper
import shutil
import random
import string
import time
from pathlib import Path
import win32api
import win32file
import pywintypes

# Default working folder
wrkFolder = r"C:/Foldername/"

# Global variable for stats
stats = 0

class AudioFile:
    def __init__(self, identifier, apath):
        self.identifier = identifier
        self.apath = apath
        self.status = 0
        self.tpath = ""
        self.spath = ""
        self.name = ""

    def stage(self):
        t_filename = f"{self.identifier}-t.txt"
        s_filename = f"{self.identifier}-s.txt"
        self.tpath = os.path.join(os.path.dirname(self.apath), t_filename)
        self.spath = os.path.join(os.path.dirname(self.apath), s_filename)
        Path(self.tpath).touch()
        Path(self.spath).touch()

    def whisper(self, audio, text):
        model = "small.en"
        # Load the model
        model = whisper.load_model(model)

        # Transcribe the audio file
        result = model.transcribe(audio)

        # Write the transcription to the text file
        with open(text, 'w') as f:
            f.write(result["text"])

    def summarize(self, text_path):
        pass  # To be implemented by the programmer later

    def name(self, summ):
        pass  # To be implemented by the programmer later

    def rename(self, new_name):
        # Rename audio file
        new_audio_path = os.path.join(os.path.dirname(self.apath), new_name + os.path.splitext(self.apath)[1])
        os.rename(self.apath, new_audio_path)
        self.apath = new_audio_path

        # Rename text file
        new_text_path = os.path.join(os.path.dirname(self.tpath), new_name + "-t.txt")
        os.rename(self.tpath, new_text_path)
        self.tpath = new_text_path

        # Rename summary file
        new_summary_path = os.path.join(os.path.dirname(self.spath), new_name + "-s.txt")
        os.rename(self.spath, new_summary_path)
        self.spath = new_summary_path

    def sort(self):
        destination_folder = os.path.join(wrkFolder, f"{self.name}{self.identifier}")
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(self.apath, destination_folder)
        shutil.move(self.tpath, destination_folder)
        shutil.move(self.spath, destination_folder)

    def statup(self):
        global stats
        self.status += 1
        stats += 1
        display(totalStatus, stats)  # Call display function

    def process(self):
        self.stage()
        self.whisper(self.apath, self.tpath)
        self.spath = self.summarize(self.tpath)
        self.name = self.name(self.spath)
        self.rename(self.name)
        self.sort()
        self.statup()

def copy_and_process_files(drive_path):
    # Step 1: Copy files
    unprocessed_folder = os.path.join(wrkFolder, "Unprocessed")
    os.makedirs(unprocessed_folder, exist_ok=True)
    shutil.copytree(drive_path, unprocessed_folder, dirs_exist_ok=True)

    # Step 2: Delete files from the drive and eject it
    for root, dirs, files in os.walk(drive_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    win32api.DeviceIoControl(win32file.CreateFile(f"\\\\.\\{drive_path}", win32file.GENERIC_READ, win32file.FILE_SHARE_READ, None, win32file.OPEN_EXISTING, 0, None),
                             win32file.FSCTL_DISMOUNT_VOLUME, None, 0, None)

    # Step 3: Filter and process audio files
    files = [f for f in os.listdir(unprocessed_folder) if f.lower().endswith(('.mp3', '.wav', '.flac'))]
    for f in os.listdir(unprocessed_folder):
        if f not in files:
            os.remove(os.path.join(unprocessed_folder, f))

    # Step 4: Generate random numbers and rename files
    random_numbers = sorted(random.sample(range(10000000, 100000000), len(files)))
    audio_files = []
    for idx, filename in enumerate(files):
        old_path = os.path.join(unprocessed_folder, filename)
        new_name = f"{random_numbers[idx]}{os.path.splitext(filename)[1]}"
        new_path = os.path.join(unprocessed_folder, new_name)
        os.rename(old_path, new_path)
        audio_files.append(AudioFile(random_numbers[idx], new_path))

    # Step 5: Process each file
    totalStatus = 6 * len(audio_files)
    for audio_file in audio_files:
        audio_file.process()

    # Step 6: Folder management
    for folder1, folder2 in [(f1, f2) for f1 in os.listdir(wrkFolder) for f2 in os.listdir(wrkFolder) if f1 != f2 and f2.endswith(f1)]:
        shutil.move(os.path.join(wrkFolder, folder2), os.path.join(wrkFolder, folder1))
        global stats
        stats += 1
        display(totalStatus, stats)

    # Step 7: Rename folders
    day_number = 1
    for folder in sorted([f for f in os.listdir(wrkFolder) if not f.startswith("Day ")]):
        new_folder_name = f"Day {day_number}"
        os.rename(os.path.join(wrkFolder, folder), os.path.join(wrkFolder, new_folder_name))
        day_number += 1

    # Step 8: Clean up
    shutil.rmtree(unprocessed_folder)
    stats = 0
    display(totalStatus, stats)

def check_for_new_drive():
    drives_before = set(win32api.GetLogicalDriveStrings().split('\x00')[:-1])
    while True:
        drives_now = set(win32api.GetLogicalDriveStrings().split('\x00')[:-1])
        new_drives = drives_now - drives_before
        if new_drives:
            for drive in new_drives:
                drive_label = win32api.GetVolumeInformation(drive)[0]
                if drive_label.lower() == "crecord":
                    copy_and_process_files(drive)
        drives_before = drives_now
        time.sleep(5)  # Check every 5 seconds

def display(total, current):
    os.system('cls')
    output = "Progress: \n["
    perc = current / total
    comp = 100*(round(perc, 2))
    for x in range(100):
        if comp > 0:
            output = output + "%"
            comp -= 1
        else:
            output = output + "·"

    output += "]"

    print(output)

if __name__ == "__main__":
    check_for_new_drive()
