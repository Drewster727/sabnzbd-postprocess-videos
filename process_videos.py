# get job params
# determine if the folder has just one video file (.mkv, .avi, .mpg, .mp4, .wmv, .ts)
## if false... exit
## if true... name that file the job name

import os
import sys
import shutil
import subprocess

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
      file=directory + '/' + name
      size=os.path.getsize(file) >> 20
      if (size < threshold):
	print 'Removing File (size too small): ' + file
	os.remove(file)
   return;

def removeVideoMetaData(directory):
   files = getVideoFiles(directory)
   for f in files:
   	orig=directory + '/' + f
	withmeta=orig + '.withmeta'
   	os.rename(orig, withmeta)
	print 'Removing metadata from ' + orig
   	subprocess.call(['ffmpeg', '-loglevel', 'error', '-y', '-i', withmeta, '-c', 'copy', '-map_metadata', '-1', '-metadata', 'title=', '-metadata', 'comment=', orig])
   	os.remove(withmeta)
   	#ffmpeg -y -i "fwc.mp4" -c copy -map_metadata -1 -metadata title="" -metadata comments="" "fwc_test.mp4" 
   return;

try:
    (scriptname,directory,orgnzbname,jobname,reportnumber,category,group,postprocstatus,url) = sys.argv
except:
    try:
	directory = sys.argv[1]
	jobname = sys.argv[3]
    except:
        print "No commandline parameters found"
        sys.exit(1)

# remove files under 60MB
removeSmallFiles(directory, 60)

# handle obfuscated files
video_files = getVideoFiles(directory)

if len(video_files) == 1:
   fp=directory + '/' + video_files[0]
   ext=os.path.splitext(video_files[0])[-1]
   print 'Renaming ' + video_files[0] + ' to ' + jobname + ext
   shutil.move(fp, os.path.join(directory,jobname + ext))
   #os.rename(fp, os.path.join(directory,jobname + ext))

# remove metadata
removeVideoMetaData(directory)

print 'Completed'

# Success code
sys.exit(0)
