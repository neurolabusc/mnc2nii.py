#!/usr/bin/env python3

import os
import sys
import subprocess

def batch_convert(input_folder, output_folder):
    """Convert all MNC files in input_folder and save to output_folder."""
    os.makedirs(output_folder, exist_ok=True)
    mnc_files = [f for f in os.listdir(input_folder) if f.endswith('.mnc')]
    if not mnc_files:
        print("No .mnc files found in the input folder.")
        sys.exit(1)
    # Convert each file using the existing mnc2nii.py script
    for mnc_file in mnc_files:
        input_path = os.path.join(input_folder, mnc_file)
        output_path = os.path.join(output_folder, os.path.splitext(mnc_file)[0] + '.nii.gz')
        print(f"Converting: {input_path} -> {output_path}")
        try:
            subprocess.run(['./mnc2nii.py', input_path, output_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error converting {mnc_file}: {e}")

if __name__ == "__main__":
    input_folder = "./In"
    output_folder = "./Out"
    if not os.path.isdir(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        sys.exit(1)
    batch_convert(input_folder, output_folder)
