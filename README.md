# mnc2nii

This repository provides reference images for converting between [NIfTI](https://brainder.org/2012/09/23/the-nifti-file-format/) and MINC file formats. The `Original` files are the source NIfTI images used for subsequent conversions. 

Each of the folders that contain images. The `In` folder provides MINC conversions as created with the gold standard [nii2mnc](https://bic-mni.github.io/man-pages/man/nii2mnc.html). The `Reference` folder provides the NIfTI images as converted back by the gold standard [mnc2nii](https://bic-mni.github.io/man-pages/man/mnc2nii.html). Finally, the `Out` folder contains NIfTI images converted back using nibabel.

Several scripts facilitate and replicate the conversion process.  The bash script `create_reference_images.sh` will re-create the images in both the `In` and `Reference` folders with any NIfTI images in the `Original` folder - the output of this conversion is provided in the `notes.txt` file. The file `batch_mnc2nii.py` will re-create the NIfTI images in the `Out` folder with any MINC images in the `In` folder. The Python script `mnc2nii.py` allows you to manually convert MINC images to NIfTI.

```
Original/
├── ax.nii.gz
├── cor.nii.gz
└── ...
In/
├── ax.mnc
├── cor.mnc
└── ...
Out/
├── ax.nii.gz
├── cor.nii.gz
└── ...
Reference/
├── ax.nii.gz
├── cor.nii.gz
└── ...
notes.txt
create_reference_images.sh
batch_mnc2nii.py
mnc2nii.py
```
# Links

 - [nii2mnc](https://bic-mni.github.io/man-pages/man/nii2mnc.html) command line tool to convert NIfTI images to MINC (e.g. `Original`->`In`)
 - [mnc2nii](https://bic-mni.github.io/man-pages/man/mnc2nii.html) reference command line tool to convert MINC images to NIfTI (e.g. `In`->`Ref`)
 - [mincconvert](https://bic-mni.github.io/man-pages/man/mincconvert.html) command line tool for converting between MINC1 (netcdf) and MINC2 (HDF5) formats.
 - [minc2.py](https://github.com/nipy/nibabel/blob/84294f4e05e0f10f9cc64d3474f94ad3e243f682/nibabel/minc2.py#L144) nibabel Python class for reading MINC2 (HDF5) images.
 - [minc1.py](https://github.com/nipy/nibabel/blob/84294f4e05e0f10f9cc64d3474f94ad3e243f682/nibabel/minc1.py) nibabel Python class for reading MINC1 (netcdf) images.
 - [minc_to_nifti.py](https://gist.github.com/ofgulban/46d5c51ea010611cbb53123bb5906ca9) is a minimal nibabel wrapper for converting MINC images to NIfTI, but unlike `mnc2nii.py` it does not preserve details such as the spatial transfomation affine matrix.
 