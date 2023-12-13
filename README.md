# combine-ome-tiff
Combines files spread across multiple OME TIFFs into a single TIFF


This package provides a simple tool to combine multiple OME TIFFS into a single OME TIFF file for subsequent handling.

## Installation

Make sure you have `tifffile` installed. You can install it using pip:

`pip install tifffile`


## Usage

Run the script from the command line, specifying the input and output file names as needed.

`python combine_ome_tiff.py -i <input_file> -o <output_file>`


### Arguments

- `-i` or `--input`: Path to the input OME-TIFF file. Default is 'img000_000_000000_0000000000.ome.tif'.
- `-o` or `--output`: Path to the output OME-TIFF file. Default is 'combined_file.ome.tif'.

## Example

To combine a set of default image files and save it as 'new_file.ome.tif':

python remove_metadata.py -o new_file.ome.tif





