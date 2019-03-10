import moviepy.editor
import os
import random
import fnmatch 
from easygui import *
from random import randint
import sys



directory = './vid'
xdim = 1980
ydim = 1080
ext = "*mp4"
length = 5

outputs=[]

# compile list of videos
inputs = [os.path.join(directory,f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and fnmatch.fnmatch(f, ext)]

for i in inputs:

    # import to moviepy
    clip = moviepy.editor.VideoFileClip(i).resize( (xdim, ydim) ) 

    # select a random time point
    start = round(random.uniform(0,clip.duration-length), 2) 

    # cut a subclip
    out_clip = clip.subclip(start,start+randint(1,length))

    outputs.append(out_clip)


# combine clips from different videos
collage = moviepy.editor.concatenate_videoclips(outputs) 



msg = "Enter output File Name"
title = "Export Video"
fieldValues = enterbox(msg, title)
if fieldValues is None:
    sys.exit(0)

collage.write_videofile(str(fieldValues) +'.mp4')