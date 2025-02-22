#!/bin/bash

# Define folders
ORIGINAL_DIR="./Original"
IN_DIR="./In"
REF_DIR="./Ref"
MINC1_DIR="./Minc1"

# Ensure output directories exist
mkdir -p "$IN_DIR" "$REF_DIR" "$MINC1_DIR"

# Function to check for errors and exit if a command fails
check_error() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# Step 1: Convert NIfTI to MINC using nii2mnc
echo "Converting NIfTI to MINC..."
for nii_file in "$ORIGINAL_DIR"/*.nii.gz; do
    if [ -f "$nii_file" ]; then
        base_name=$(basename "$nii_file" .nii.gz)
        output_mnc="$IN_DIR/$base_name.mnc"
        echo "Converting: $nii_file -> $output_mnc"
        nii2mnc "$nii_file" "$output_mnc"
        check_error "Failed to convert $nii_file to MNC."
    fi
done

# Step 2: Convert MINC to NIfTI using mnc2nii
echo "Converting MINC to NIfTI..."
for mnc_file in "$IN_DIR"/*.mnc; do
    if [ -f "$mnc_file" ]; then
        base_name=$(basename "$mnc_file" .mnc)
        output_nii="$REF_DIR/$base_name.nii"
        echo "Converting: $mnc_file -> $output_nii"
        mnc2nii "$mnc_file" "$output_nii"
        check_error "Failed to convert $mnc_file to NIfTI."
    fi
done


echo "Conversion pipeline completed successfully!"
