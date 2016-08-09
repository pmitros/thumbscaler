Thumbnail Scaler
====

This is a set of scripts to convert a directory tree of images into an
identical directory tree of JPEGs, downscaling to reasonable
resolution. I needed this so that I could reasonably browse a
directory tree of 25 megapixel RAW files to pick out ones I liked (it
went from 120GB down to 1.2GB, and with appropriately faster previews). 

It picks out resolution from EXIF info (rather than the image
itself). This is slightly (bot noticeably) faster for some types of
RAW files.

Requirements: 

* Python
* ImageMagick
* exiv2
* ufraw (or another ImageMagick-supported RAW converter)
* For image previews, OpenCV and Python bindings

Usage (no preview): 

  python thumbs.py source_directory destination_directory

Usage (with preview): 

  python thumbs_preview.py source_directory destination_directory

It will downsamples to either a height of 1536 or a width of 2048,
whichever results in a smaller image. This can be changed in the
script (the lines HEIGHT= and WIDTH=). This may sound intimidating,
but it's easy enough -- just open the script in a text editor, and it
will be obvious.

It handles RAW+JPEG files correctly (it processes only the JPEG). It
will never overwrite files (which also means that if you stop it and
continue, it'll pick up where it last left off).

All code is Copyright (c) 2011. Piotr Mitros. It may be distributed
under the terms of the GNU GPL v3 or newer. 
