#!/usr/bin/env python
# Batch thumbnail generation script using PIL

import sys
import os
import Image

scale_size = (500)

# Loop through all provided arguments
for i in range(1, len(sys.argv)):
    try:
        # Attempt to open an image file
        filepath = sys.argv[i]
        image = Image.open(filepath)
    except IOError, e:
        # Report error, and then skip to the next argument
        print "Problem opening", filepath, ":", e
        continue

    # Resize the image
    y = image.size
    ratio = (float(y[0]) / float(y[1]))
    image = image.resize((scale_size, int((scale_size / ratio)) ))


    # Split our original filename into name and extension
    (name, extension) = os.path.splitext(filepath)

    # Save the thumbnail as "(original_name)_small.(extension)"
    image.save(name + '_small.'+ extension)
