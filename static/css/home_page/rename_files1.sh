#!/bin/bash

# Function to rename files with unique names
rename_files() {
    for file in *; do
        # Skip if it's not a regular file
        if [[ ! -f "$file" ]]; then
            continue
        fi

        # Remove version suffix (e.g., _ver=6.7)
        clean_name="${file%%_ver=*}"

        # Extract the base name and extension
        base_name="${clean_name%.*}"
        extension="${clean_name##*.}"

        # Initialize counter
        counter=1
        new_name="$clean_name"

        # Check if the file already exists and append a number if it does
        while [[ -e "$new_name" ]]; do
            new_name="${base_name}${counter}.${extension}"
            counter=$((counter + 1))
        done

        # Rename the file
        if [[ "$new_name" != "$file" ]]; then
            mv "$file" "$new_name"
            echo "Renamed: $file -> $new_name"
        fi
    done
}

# Call the function
rename_files
