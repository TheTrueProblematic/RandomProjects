#!/bin/bash

SOURCE_DIR="Convert"
DEST_DIR="Converted"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Function to convert a single file and maintain album art
convert_file() {
    local srcFile="$1"
    local outFile="${srcFile/$SOURCE_DIR/$DEST_DIR}"
    outFile="${outFile%.m4a}.mp3"

    # Ensure the output directory exists
    mkdir -p "$(dirname "$outFile")"

    # Convert the file and try to maintain album art
    ffmpeg -i "$srcFile" -codec:v copy -map 0:0 -map 0:1 -id3v2_version 3 \
           -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" \
           -codec:a libmp3lame -q:a 0 "$outFile"
}

export -f convert_file
export SOURCE_DIR
export DEST_DIR

# Find all .m4a files and convert them, attempting to maintain album art
find "$SOURCE_DIR" -type f -name "*.m4a" -exec bash -c 'convert_file "$0"' {} \;

echo "Conversion complete!"
