#!/bin/bash

# Name of the album artwork file present in the folder
album_art="Happier Than Ever Artwork.jpg"

# Loop through all MP3 files in the current directory
for file in *.mp3; do
    base_name=$(basename "$file" .mp3)
    intermediate_file="${base_name}_temp.m4a"
    output_file="${base_name}.m4a"
    
    # Convert the audio file to Apple Lossless with explicit quality settings
    # -ar sets the audio sample rate to 44100 Hz, adjust if your source has a different rate
    ffmpeg -i "$file" -vn -acodec alac -ar 44100 "$intermediate_file"
    
    # Attach the specified album art to the ALAC file and output to the final file
    ffmpeg -i "$intermediate_file" -i "$album_art" -map 0:a -map 1:v -c copy -disposition:v:0 attached_pic -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" "$output_file"

    # Remove the intermediate file as it's no longer needed
    rm "$intermediate_file"
done

echo "Conversion to ALAC with specified album art attached completed."
