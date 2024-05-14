import os


def process_folder(path):
    # List all files in the given directory
    try:
        files = [os.path.join(path, file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    except FileNotFoundError:
        print("The specified path does not exist.")
        return 0

    if len(files) == 1:
        # Only one file in the folder, do nothing
        return 1
    elif len(files) > 1:
        # Find the largest file by size
        largest_files = sorted(files, key=lambda x: os.path.getsize(x), reverse=True)
        max_size = os.path.getsize(largest_files[0])

        # Filter out files that are the largest if there are multiple
        largest_files = [file for file in largest_files if os.path.getsize(file) == max_size]

        # Delete all other files
        files_to_delete = [file for file in files if file not in largest_files]
        for file in files_to_delete:
            os.remove(file)

        return len(largest_files)


# Example usage
folder_path = 'T:\Shared\MoviesTBC\THE_GREAT_GATSBY'  # Replace this with your folder path
result = process_folder(folder_path)
print(f"Result: {result}")
