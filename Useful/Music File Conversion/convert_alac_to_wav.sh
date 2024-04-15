#!/bin/bash

SOURCE_DIR="Convert"
DEST_DIR="ConvertedWAV"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Function to convert a single file to WAV
convert_file() {
    local srcFile="$1"
    local outFile="${srcFile/$SOURCE_DIR/$DEST_DIR}"
    outFile="${outFile%.m4a}.wav"

    # Ensure the output directory exists
    mkdir -p "$(dirname "$outFile")"

    # Convert the file to WAV
    ffmpeg -i "$srcFile" -vn -codec:a pcm_s16le "$outFile"
}

export -f convert_file
export SOURCE_DIR
export DEST_DIR

# Find all .m4a files and convert them to WAV
find "$SOURCE_DIR" -type f -name "*.m4a" -exec bash -c 'convert_file "$0"' {} \;

echo "Conversion complete!"
