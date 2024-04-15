#!/bin/bash

# Name of the album artwork file present in the folder
album_art="Happier Than Ever Artwork.jpg"

# Loop through all MP3 files in the current directory
for file in *.mp3; do
    base_name=$(basename "$file" .mp3)
    output_file="${base_name}.flac"
    
    # Convert the audio file to FLAC with explicit quality settings
    # -ar sets the audio sample rate to 44100 Hz, adjust if your source has a different rate
    ffmpeg -i "$file" -vn -acodec flac -ar 44100 "$output_file"

    # Attach the specified album art to the FLAC file
    # Note: FLAC supports embedding pictures in a different way than ALAC. We'll use metaflac to attach the album art.
    metaflac --import-picture-from="$album_art" "$output_file"

done

echo "Conversion to FLAC with specified album art attached completed."
