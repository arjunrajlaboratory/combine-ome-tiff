import argparse
import tifffile as tiff

def combine_ome_tiff(input_file, output_file):
    with tiff.TiffFile(input_file) as input_tiff:
        image_data = input_tiff.asarray()

    with tiff.TiffWriter(output_file) as output_tiff:
        output_tiff.write(image_data)

    print(f"File '{output_file}' has been created.")

def main():
    parser = argparse.ArgumentParser(description='Combine OME-TIFF files.')
    parser.add_argument('-i', '--input', default='img000_000_000000_0000000000.ome.tif',
                        help='Input OME-TIFF file. Default is img000_000_000000_0000000000.ome.tif')
    parser.add_argument('-o', '--output', default='combined_file.ome.tif',
                        help='Output OME-TIFF file. Default is combined_file.ome.tif')

    args = parser.parse_args()

    combine_ome_tiff(args.input, args.output)

if __name__ == '__main__':
    main()
