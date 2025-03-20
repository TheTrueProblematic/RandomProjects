import os

def list_files():
    folder = os.getcwd()  # Get the current working directory
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and f not in ["filenames.py", "file_list.txt", ".DS_Store"]]

    with open("file_list.txt", "w", encoding="utf-8") as f:
        for file in files:
            f.write(file + "\n")

    print("file_list.txt has been created with all filenames.")

if __name__ == "__main__":
    list_files()