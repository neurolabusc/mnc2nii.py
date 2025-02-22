#!/usr/bin/env python3

import nibabel as nib
import os
import sys

def convert_mnc_to_nifti(input_file, output_file=None):
    if not input_file.endswith('.mnc'):
        print("Error: Input file must have a '.mnc' extension.")
        sys.exit(1)
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.nii.gz'
    if not (output_file.endswith('.nii') or output_file.endswith('.nii.gz')):
        print("Error: Output file must have a '.nii' or '.nii.gz' extension.")
        sys.exit(1)
    try:
        img = nib.load(input_file)
        data = img.get_fdata()
        affine = img.affine
        nifti_img = nib.Nifti1Image(data, affine)
        nifti_img.header.set_qform(affine)
        nifti_img.header.set_sform(affine)
        nifti_img.header['cal_min'] = data.min()
        nifti_img.header['cal_max'] = data.max()
        nib.save(nifti_img, output_file)
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage:")
        print("  ./mnc2nii.py input.mnc                # Default output: input.nii.gz")
        print("  ./mnc2nii.py input.mnc output.nii.gz  # Custom output path")
        sys.exit(1)
    input_mnc_file = sys.argv[1]
    output_nii_file = sys.argv[2] if len(sys.argv) == 3 else None
    convert_mnc_to_nifti(input_mnc_file, output_nii_file)
