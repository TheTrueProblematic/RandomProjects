import os
import re
import sys
import math
import shutil
import random
import string
import cv2

try:
    import pytesseract
    from PIL import Image
except ImportError:
    print("Please install pytesseract and Pillow before running this script.")
    sys.exit(1)

# Sanitize folder name
def sanitize_filename(filename):
    # Remove invalid characters
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply thresholding to get a binary image
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Save the preprocessed image (overwrite the original image)
    cv2.imwrite(image_path, thresh)

def main():
    # Get current directory
    root_dir = os.getcwd()
    root_folder_name = os.path.basename(root_dir)

    # Extract showName
    if root_folder_name.endswith(" PRE"):
        showName = root_folder_name[:-4]
    else:
        print("Root folder name does not end with ' PRE'. Exiting.")
        sys.exit(1)

    # Prompt user for input seconds
    sec_input = input("Enter number of seconds: ")
    try:
        sec = float(sec_input)
    except ValueError:
        print("Invalid input for seconds.")
        sys.exit(1)

    # Initialize skip counter and process counter
    skip_counter = 1
    process_counter = 1

    # Iterate over subfolders in root_dir
    for subdir_name in os.listdir(root_dir):
        subdir_path = os.path.join(root_dir, subdir_name)
        if os.path.isdir(subdir_path):
            # Determine season number
            season_match = re.search(r'S(\d+)', subdir_name, re.IGNORECASE)
            if season_match:
                season_num = season_match.group(1)
            else:
                season_match = re.search(r'Season\s+(\d+)', subdir_name, re.IGNORECASE)
                if season_match:
                    season_num = season_match.group(1)
                else:
                    print(f"Could not find season number in folder {subdir_name}")
                    continue
            # Convert season_num to two-digit string
            season = f"{int(season_num):02d}"

            # Process .mkv files in subdir
            for filename in os.listdir(subdir_path):
                if filename.lower().endswith('.mkv'):
                    video_path = os.path.join(subdir_path, filename)
                    # Create InProgress folder
                    inprogress_folder_name = "InProgress"
                    inprogress_path = os.path.join(subdir_path, inprogress_folder_name)
                    os.makedirs(inprogress_path, exist_ok=True)
                    # Move video file into InProgress
                    new_video_path = os.path.join(inprogress_path, filename)
                    shutil.move(video_path, new_video_path)
                    # Rename video file
                    new_video_name = f"{showName} - S{season}E.mkv"
                    renamed_video_path = os.path.join(inprogress_path, new_video_name)
                    os.rename(new_video_path, renamed_video_path)

                    # Calculate frame
                    # Get frame rate
                    try:
                        cap = cv2.VideoCapture(renamed_video_path)
                        fps = cap.get(cv2.CAP_PROP_FPS)
                        total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                        if fps == 0:
                            print(f"Could not get frame rate for video {renamed_video_path}")
                            cap.release()
                            continue
                        # Calculate frame number
                        frame_num = math.ceil(fps * sec)
                        if frame_num > total_frames:
                            # Video is shorter than requested frame
                            skip_folder_name = f"SKIP {skip_counter:03d}"
                            skip_folder_path = os.path.join(subdir_path, skip_folder_name)
                            os.rename(inprogress_path, skip_folder_path)
                            skip_counter += 1
                            cap.release()
                            continue
                        # Set video to frame_num
                        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
                        ret, frame = cap.read()
                        if ret:
                            # Save frame as RefrenceImage.png
                            image_path = os.path.join(inprogress_path, "RefrenceImage.png")
                            cv2.imwrite(image_path, frame)
                            cap.release()

                            # Preprocess the image
                            preprocess_image(image_path)

                            # Run OCR
                            ocr_text = pytesseract.image_to_string(Image.open(image_path))

                            # Remove numbers and non-alphabet characters (including space)
                            ocr_text_clean = re.sub(r'[^A-Za-z]', '', ocr_text)
                            # Truncate to first 30 characters
                            if len(ocr_text_clean) > 30:
                                ocr_text_clean = ocr_text_clean[:30]
                            # If OCR fails (empty string), generate 30 random characters
                            if not ocr_text_clean:
                                ocr_text_clean = ''.join(random.choices(string.ascii_letters, k=30))

                            # Sanitize the folder name
                            ocr_folder_name = sanitize_filename(ocr_text_clean)
                            if not ocr_folder_name:
                                ocr_folder_name = ''.join(random.choices(string.ascii_letters, k=30))

                            # Append sequential counter to folder name
                            ocr_folder_name_with_counter = f"{ocr_folder_name}_{process_counter}"

                            # Rename InProgress folder to OCR value with counter
                            new_folder_path = os.path.join(subdir_path, ocr_folder_name_with_counter)
                            os.rename(inprogress_path, new_folder_path)

                            process_counter += 1

                        else:
                            print(f"Could not read frame {frame_num} from video {renamed_video_path}")
                            cap.release()
                            continue

                    except Exception as e:
                        print(f"Error processing video {renamed_video_path}: {e}")
                        cap.release()
                        continue

    print("Processing complete.")

if __name__ == "__main__":
    main()
