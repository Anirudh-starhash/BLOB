#!/bin/bash

# Get the file name from the first argument
FILE_NAME=$1

# Define the source and destination folders
SOURCE_FOLDER="."  # Assuming the file is in the current directory (adjust if it's in another location)
DESTINATION_FOLDER="../../BLOB-FRONTEND/src/assets/images"

# Ensure the destination folder exists
mkdir -p "$DESTINATION_FOLDER"

# Define the full source and destination paths
SOURCE_PATH="${SOURCE_FOLDER}/${FILE_NAME}"
DESTINATION_PATH="${DESTINATION_FOLDER}/${FILE_NAME}"

# Move the file from the source to the destination folder
if [ -f "$SOURCE_PATH" ]; then
    mv "$SOURCE_PATH" "$DESTINATION_PATH"
    echo "File '$FILE_NAME' successfully moved to '$DESTINATION_FOLDER'."
else
    echo "Error: Source file '$SOURCE_PATH' not found."
    exit 1
fi
