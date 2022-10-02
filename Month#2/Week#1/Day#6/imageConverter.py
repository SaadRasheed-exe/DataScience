from PIL import Image
import sys
import os

if len(sys.argv) > 2:
    infile = sys.argv[1]
    outfile = sys.argv[2]
else:
    print('One or more arguments are missing. Please refer to the documentation for details.')
    exit()

supported_ext = ['.png', '.jpg']


def jpg_to_png(infile, outfile):
    img = Image.open(infile)
    img.save(outfile)


def png_to_jpg(infile, outfile):
    png = Image.open(infile)
    jpg = png.convert('RGB')
    jpg.save(outfile, quality=95)


def check_types(intype, outtype):
    if intype not in supported_ext:
        print('Input file type is not supported.')
        exit()
    if outtype not in supported_ext:
        print('Output file type is not supported.')
        exit()
    if outtype == intype:
        print('Converting to same file format as input file.')
        exit()


def main():
    infile_ext = os.path.splitext(infile)[-1]
    outfile_ext = os.path.splitext(outfile)[-1]
    check_types(infile_ext, outfile_ext)
    if infile_ext == '.png':
        png_to_jpg(infile, outfile)
    else:
        jpg_to_png(infile, outfile)


if __name__ == '__main__':
    main()
