# Drew McMinn, Copyright 2017

import os
import sys
import itertools
import shutil
import subprocess

def flattenDirectory(destination):
    all_files = []
    for root, _dirs, files in itertools.islice(os.walk(destination), 1, None):
        for filename in files:
            all_files.append(os.path.join(root, filename))
    for filename in all_files:
	newpath=os.path.join(destination, os.path.basename(filename))
	if (os.path.exists(newpath)):
	   os.remove(newpath)
        shutil.move(filename, destination)

def getAllFiles(directory):
   all_files = os.listdir(directory)
   return all_files;

def getVideoFiles(directory):
   all_files = getAllFiles(directory)
   video_files = []
   for name in all_files:
      if (name.endswith((".mkv", ".avi", ".mpg", ".mpeg", ".mp4", ".wmv", ".ts"))):
         video_files.append(name)
   return video_files;

def removeSmallFiles(directory, threshold):
   all_files = getAllFiles(directory)
   for name in all_files:
      file=os.path.join(directory, name)
      isFolder=os.path.isdir(file)

      if (os.path.isdir(file)):
	shutil.rmtree(file)
	continue

      size=os.path.getsize(file) >> 20

      if (size < threshold):
	print 'Removing File (size too small): ' + file
	os.remove(file)

def removeVideoMetaData(directory):
   files = getVideoFiles(directory)
   for f in files:
   	orig=os.path.join(directory, f)
	withmeta=orig + '.withmeta'
   	os.rename(orig, withmeta)
	print 'Removing metadata from ' + f
   	subprocess.call(['ffmpeg', '-loglevel', 'error', '-y', '-i', withmeta, '-map', '0:v', '-map', '0:m:language:eng', '-c', 'copy', '-map_metadata', '-1', '-metadata', 'title=', '-metadata', 'comment=', orig])
   	os.remove(withmeta)
   	#ffmpeg -y -i "fwc.mp4" -c copy -map_metadata -1 -metadata title="" -metadata comments="" "fwc_test.mp4" 

try:
    (scriptname,directory,orgnzbname,jobname,reportnumber,category,group,postprocstatus,url) = sys.argv
except:
    try:
	directory = sys.argv[1]
	jobname = sys.argv[3]
    except:
        print "No commandline parameters found"
        sys.exit(1)

# flatten
print 'Flattening contents of ' + directory
flattenDirectory(directory)

# remove files under 60MB
removeSmallFiles(directory, 60)

# handle obfuscated files
video_files = getVideoFiles(directory)

if len(video_files) == 1:
   existing=video_files[0]
   fp=directory + '/' + existing
   ext=os.path.splitext(existing)[-1]
   new=jobname + ext
   if (new.lower() != existing.lower()):
      print 'Renaming ' + existing + ' to ' + new
      shutil.move(fp, os.path.join(directory,new))

# remove metadata
removeVideoMetaData(directory)

# Success code
print 'Completed'
sys.exit(0)
