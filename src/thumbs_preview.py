import os
import posixpath
import sys
import thumbs_ui

import warnings
warnings.simplefilter('ignore')

extensions=[".3fr",".ari",".arw",".srf",".sr2",".bay",".crw",".cr2",".cap",".iiq",".eip",".dcs",".dcr",".drf",".k25",".kdc",".dng",".erf",".fff",".mef",".mos",".mrw",".nef",".nrw",".orf",".ptx",".pef",".pxn",".R3D",".raf",".raw",".rw2",".raw",".rwl",".dng",".rwz",".x3f",".jpeg",".jpg"]

# Rescale to a maximum of 3MP
HEIGHT=1536
WIDTH=2048

def desired_size(size):
    scale_x=float(WIDTH)/float(size[0])
    scale_y=float(HEIGHT)/float(size[1])
    scale=min(scale_x, scale_y, 1)
    new_size=[int(round(s*scale)) for s in size]
    #print scale, new_size
    return new_size

# Convert is slow on RAW files. exiv2 requires exif info, but seems better
def img_size_magick(filename):
    (i,o)=os.popen2(["identify", filename])
    data=o.readlines()
    data=map(int,data[0].split(' ')[2].split('x'))
    i.close()
    o.close()
    return data

def img_size(filename):
    (i,o)=os.popen2(["exiv2", filename])
    data=o.readlines()
    data=[d for d in data if d[:10]=='Image size']
    data=map(int,data[0].split(':')[1].split('x'))
    i.close()
    o.close()
    return data

def process_img(source_img, dest_img):
    basename, extension = os.path.splitext(dest_img)
    dest_img=basename+".jpg"

    if os.path.isfile(dest_img):
        print "Skipping",dest_img," -- destination exists"
        return

    basename, extension = os.path.splitext(source_img)
    # If it's a RAW file, and there's a JPG already, skip processing
    if extension.lower()!='.jpg':
        if os.path.isfile(basename+".jpg") or os.path.isfile(basename+".JPG"):
            print "skipping", basename, extension, "JPEG exists"
            return
    if extension.lower() not in extensions: 
        #print "Unknown file format ", source_img
        return
    size=img_size(source_img)
    new_size=desired_size(size)
    new_size="%ix%i"%(new_size[0], new_size[1])

    cmd=["convert", "-scale", new_size, source_img, dest_img]
    print cmd
    (i,o)=os.popen2(cmd)
    data=o.readlines()
    print data
    i.close()
    o.close()
    thumbs_ui.ui_update_image(dest_img)
    #print size, cmd

def process_dir(source_dir, dest_dir):
    if not posixpath.isdir(dest_dir):
        os.mkdir(dest_dir)
    #print source_dir, dest_dir
    for f in os.listdir(source_dir):
        #print "process", f,
        filename_in=posixpath.join(source_dir, f)
        filename_out=posixpath.join(dest_dir, f)
        #print filename_in, filename_out
        if posixpath.isdir(filename_in):
            #print "dir"
            process_dir(filename_in, filename_out)
        else:
            #print "file"
            process_img(filename_in, filename_out)

process_dir(sys.argv[1], sys.argv[2])
thumbs_ui.terminate_ui()

